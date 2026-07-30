"""
Master Orchestrator Pipeline for Flow-Graph VAPT.
Ties together Crawler, Extraction, Classification, Inventory, Flow Graph, Replay, and Analysis modules.
"""

from typing import Dict, List, Optional
from loguru import logger

from flow_graph_vapt.analyzer import DifferentialResponseAnalyzer
from flow_graph_vapt.classifier import ObjectClassificationEngine
from flow_graph_vapt.crawler import PlaywrightCrawler
from flow_graph_vapt.extractor import IdentifierExtractorEngine
from flow_graph_vapt.graph import ApplicationFlowGraph
from flow_graph_vapt.inventory import ObjectInventory
from flow_graph_vapt.models import BOLAFinding, HTTPInteraction
from flow_graph_vapt.replay import ReplayEngine
from flow_graph_vapt.reporter import ReportGenerator


class FlowGraphVAPTPipeline:
    """End-to-end automated BOLA scanner pipeline."""

    def __init__(self, target_base_url: str, output_dir: str = "./reports") -> None:
        self.target_base_url = target_base_url
        self.extractor = IdentifierExtractorEngine()
        self.classifier = ObjectClassificationEngine()
        self.inventory = ObjectInventory()
        self.graph = ApplicationFlowGraph()
        self.replay_engine = ReplayEngine()
        self.analyzer = DifferentialResponseAnalyzer()
        self.reporter = ReportGenerator(output_dir=output_dir)

    async def run_hybrid_assessment(
        self,
        user_a_interactions: List[HTTPInteraction],
        user_b_interactions: List[HTTPInteraction],
        user_a_auth_headers: Optional[Dict[str, str]] = None,
        enable_active_crawler: bool = True
    ) -> List[BOLAFinding]:
        """
        Executes hybrid BOLA assessment combining manually captured proxy interactions
        AND active Playwright crawler discovery.
        """
        if enable_active_crawler:
            logger.info("Triggering Playwright Active Crawler for automated endpoint discovery...")
            crawler = PlaywrightCrawler(target_base_url=self.target_base_url)
            crawled_interactions = await crawler.crawl(max_pages=15)
            # Merge crawled interactions into User_A's interaction pool
            user_a_interactions.extend(crawled_interactions)

        return await self.run_full_assessment(
            user_a_interactions=user_a_interactions,
            user_b_interactions=user_b_interactions,
            user_a_auth_headers=user_a_auth_headers
        )

    async def run_full_assessment(
        self,
        user_a_interactions: List[HTTPInteraction],
        user_b_interactions: List[HTTPInteraction],
        user_a_auth_headers: Optional[Dict[str, str]] = None
    ) -> List[BOLAFinding]:
        """
        Executes complete BOLA assessment using captured dual-session interactions.
        """
        logger.info("Initializing Flow-Graph VAPT Scanner Pipeline...")
        confirmed_findings: List[BOLAFinding] = []

        # Step 1: Process User B (Victim) Interactions to populate Inventory & Graph
        logger.info("Step 1: Parsing Victim Persona (User B) traffic into Object Inventory...")
        for interaction in user_b_interactions:
            candidates = self.extractor.extract_from_interaction(interaction)
            for cand in candidates:
                entity_type = self.classifier.infer_entity_type(cand, interaction)
                cand.inferred_entity_type = entity_type
                self.inventory.add_identifier(entity_type, session_id="User_B", candidate=cand)
                
                # Build Graph Nodes & Edges
                ep_node = self.graph.add_endpoint_node(interaction.request.url, interaction.request.method.value, interaction.request.url)
                ent_node = self.graph.add_entity_node(entity_type)
                self.graph.add_consumes_edge(ent_node, ep_node, cand.key_name, cand.location.value)
                self.graph.attach_discovered_identifier(entity_type, cand.raw_value)

        # Step 2: Process User A (Attacker) Interactions & Perform Mutation Replays
        logger.info("Step 2: Analyzing Attacker Persona (User A) endpoints and executing BOLA Replays...")
        for interaction in user_a_interactions:
            candidates = self.extractor.extract_from_interaction(interaction)
            for cand in candidates:
                entity_type = self.classifier.infer_entity_type(cand, interaction)
                cand.inferred_entity_type = entity_type
                self.inventory.add_identifier(entity_type, session_id="User_A", candidate=cand)

                # Find alternative identifiers belonging to User B (Victim)
                alt_ids = self.inventory.get_alternative_identifiers(entity_type, exclude_session_id="User_A")
                for alt_val in alt_ids:
                    if alt_val == cand.raw_value:
                        continue  # Skip substituting exact same ID

                    # Execute Replay Mutation
                    try:
                        replay_res = await self.replay_engine.execute_replay(
                            baseline_interaction=interaction,
                            target_id=cand,
                            alternate_id_value=alt_val,
                            attacker_auth_headers=user_a_auth_headers
                        )

                        # Differential Response Analysis
                        finding = self.analyzer.analyze_replay_pair(replay_res)
                        if finding:
                            confirmed_findings.append(finding)

                    except Exception as e:
                        logger.error(f"Replay pipeline execution error: {e}")

        # Step 3: Export Assessment Reports
        logger.info(f"Step 3: Exporting reports for {len(confirmed_findings)} confirmed findings...")
        self.reporter.export_json(confirmed_findings)
        self.reporter.export_markdown(confirmed_findings)
        self.reporter.export_html(confirmed_findings)

        logger.info("Flow-Graph VAPT Assessment Completed Successfully.")
        return confirmed_findings

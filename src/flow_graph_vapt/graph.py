"""
Application Flow Graph Engine.
Uses NetworkX to build a directed property multigraph representing endpoints, entities,
and request sequences for correlation and context-aware BOLA security testing.

Design Explanation & Educational Insights:
- Why NetworkX? NetworkX allows rapidly constructing and querying directed graphs in Python memory with full support for pathfinding, topological sorting, and metadata attributes on nodes/edges.
- Abstract Architecture: Graph operations are encapsulated inside an abstract interface/class so Neo4j or Memgraph can replace NetworkX without altering upstream scanner logic.
"""

from typing import Any, Dict, List, Optional, Set
import networkx as nx
from loguru import logger
from flow_graph_vapt.models import CandidateIdentifier, HTTPInteraction
from flow_graph_vapt.exceptions import GraphStoreError


class ApplicationFlowGraph:
    """
    Core Directed Property Graph modeling the target application's attack surface.
    
    Node Types:
    - ENDPOINT: Canonical API paths (e.g., 'GET /api/v1/orders/{id}')
    - ENTITY: Inferred object types (e.g., 'Order', 'User')
    
    Edge Types:
    - PRODUCES: Endpoint -> Entity (Endpoint response exposes entity IDs)
    - CONSUMES: Entity -> Endpoint (Endpoint requires entity ID to execute)
    - DEPENDS_ON: Endpoint -> Endpoint (Sequential state dependency)
    """

    def __init__(self) -> None:
        self._graph = nx.DiGraph()

    @property
    def raw_graph(self) -> nx.DiGraph:
        return self._graph

    def add_endpoint_node(self, canonical_path: str, method: str, sample_url: str) -> str:
        """Adds or updates an Endpoint Node in the graph."""
        node_id = f"ENDPOINT:{method}:{canonical_path}"
        if not self._graph.has_node(node_id):
            self._graph.add_node(
                node_id,
                type="ENDPOINT",
                canonical_path=canonical_path,
                method=method,
                sample_url=sample_url,
                visit_count=1
            )
            logger.debug(f"Added Endpoint Node: {node_id}")
        else:
            self._graph.nodes[node_id]["visit_count"] += 1
        return node_id

    def add_entity_node(self, entity_type: str) -> str:
        """Adds or updates an Entity Node in the graph."""
        node_id = f"ENTITY:{entity_type}"
        if not self._graph.has_node(node_id):
            self._graph.add_node(
                node_id,
                type="ENTITY",
                entity_type=entity_type,
                discovered_ids=set()
            )
            logger.debug(f"Added Entity Node: {node_id}")
        return node_id

    def add_produces_edge(self, endpoint_node_id: str, entity_node_id: str, identifier_key: str) -> None:
        """Creates an edge indicating that an Endpoint response exposes identifiers for an Entity."""
        self._graph.add_edge(
            endpoint_node_id,
            entity_node_id,
            relation="PRODUCES",
            key=identifier_key
        )

    def add_consumes_edge(self, entity_node_id: str, endpoint_node_id: str, identifier_key: str, location: str) -> None:
        """Creates an edge indicating that an Endpoint requires an Entity identifier."""
        self._graph.add_edge(
            entity_node_id,
            endpoint_node_id,
            relation="CONSUMES",
            key=identifier_key,
            location=location
        )

    def add_sequence_edge(self, source_endpoint_id: str, target_endpoint_id: str, session_id: str) -> None:
        """Records temporal execution sequence between two endpoints."""
        if source_endpoint_id != target_endpoint_id:
            self._graph.add_edge(
                source_endpoint_id,
                target_endpoint_id,
                relation="DEPENDS_ON",
                session_id=session_id
            )

    def attach_discovered_identifier(self, entity_type: str, identifier_val: str) -> None:
        """Attaches a discovered valid identifier value to the Entity node."""
        node_id = f"ENTITY:{entity_type}"
        if self._graph.has_node(node_id):
            self._graph.nodes[node_id]["discovered_ids"].add(identifier_val)

    def get_endpoints_consuming_entity(self, entity_type: str) -> List[Dict[str, Any]]:
        """Returns all endpoint nodes that consume a given Entity type."""
        entity_node_id = f"ENTITY:{entity_type}"
        consuming_endpoints = []
        if not self._graph.has_node(entity_node_id):
            return consuming_endpoints

        for target in self._graph.successors(entity_node_id):
            edge_data = self._graph.get_edge_data(entity_node_id, target)
            if edge_data and edge_data.get("relation") == "CONSUMES":
                node_data = self._graph.nodes[target]
                consuming_endpoints.append({
                    "endpoint_id": target,
                    "canonical_path": node_data.get("canonical_path"),
                    "method": node_data.get("method"),
                    "key": edge_data.get("key"),
                    "location": edge_data.get("location")
                })
        return consuming_endpoints

    def export_graph_metrics(self) -> Dict[str, Any]:
        """Calculates topological metrics for graph visualization and analysis."""
        return {
            "total_nodes": self._graph.number_of_nodes(),
            "total_edges": self._graph.number_of_edges(),
            "endpoint_nodes": len([n for n, d in self._graph.nodes(data=True) if d.get("type") == "ENDPOINT"]),
            "entity_nodes": len([n for n, d in self._graph.nodes(data=True) if d.get("type") == "ENTITY"]),
            "is_directed": self._graph.is_directed()
        }

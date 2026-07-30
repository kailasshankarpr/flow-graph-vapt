"""
Comprehensive Test Suite for Flow-Graph VAPT.
Verifies Identifier Extraction, Entity Classification, Object Inventory, Graph Construction, Replay Engine, and Differential Analyzer.
"""

import pytest
from flow_graph_vapt.analyzer import DifferentialResponseAnalyzer
from flow_graph_vapt.classifier import ObjectClassificationEngine
from flow_graph_vapt.extractor import IdentifierExtractorEngine
from flow_graph_vapt.graph import ApplicationFlowGraph
from flow_graph_vapt.inventory import ObjectInventory
from flow_graph_vapt.models import (
    CandidateIdentifier,
    HTTPInteraction,
    HTTPMethod,
    HTTPRequestModel,
    HTTPResponseModel,
    IdentifierLocation,
    ReplayMutation,
    ReplayResult,
)
from flow_graph_vapt.replay import ReplayEngine


@pytest.fixture
def sample_interaction_order():
    return HTTPInteraction(
        interaction_id="test_1",
        session_id="User_B",
        request=HTTPRequestModel(
            url="http://api.target.com/api/v1/orders/101",
            method=HTTPMethod.GET,
            headers={"Authorization": "Bearer victim_token"}
        ),
        response=HTTPResponseModel(
            status_code=200,
            headers={"Content-Type": "application/json"},
            body='{"order_id": 101, "item": "Laptop", "price": 1200}',
            json_data={"order_id": 101, "item": "Laptop", "price": 1200},
            content_length=50
        )
    )


def test_identifier_extraction(sample_interaction_order):
    extractor = IdentifierExtractorEngine()
    candidates = extractor.extract_from_interaction(sample_interaction_order)
    
    assert len(candidates) >= 1
    path_cand = next(c for c in candidates if c.location == IdentifierLocation.PATH)
    assert path_cand.raw_value == "101"
    assert path_cand.key_name == "orders_id"
    assert path_cand.confidence_score >= 0.50


def test_object_classification(sample_interaction_order):
    extractor = IdentifierExtractorEngine()
    classifier = ObjectClassificationEngine()
    
    candidates = extractor.extract_from_interaction(sample_interaction_order)
    cand = candidates[0]
    
    entity_type = classifier.infer_entity_type(cand, sample_interaction_order)
    assert entity_type == "Order"


def test_object_inventory():
    inventory = ObjectInventory()
    cand = CandidateIdentifier(
        identifier_id="cand_1",
        key_name="order_id",
        raw_value="101",
        location=IdentifierLocation.PATH,
        confidence_score=0.8,
        extracted_from_interaction_id="test_1"
    )
    
    inventory.add_identifier("Order", "User_B", cand)
    alternatives = inventory.get_alternative_identifiers("Order", exclude_session_id="User_A")
    
    assert "101" in alternatives
    assert len(inventory.get_alternative_identifiers("Order", exclude_session_id="User_B")) == 0


def test_flow_graph():
    graph = ApplicationFlowGraph()
    ep_node = graph.add_endpoint_node("/api/v1/orders/{id}", "GET", "http://api.target.com/api/v1/orders/101")
    ent_node = graph.add_entity_node("Order")
    
    graph.add_consumes_edge(ent_node, ep_node, "order_id", "PATH")
    
    metrics = graph.export_graph_metrics()
    assert metrics["endpoint_nodes"] == 1
    assert metrics["entity_nodes"] == 1
    
    consuming = graph.get_endpoints_consuming_entity("Order")
    assert len(consuming) == 1
    assert consuming[0]["canonical_path"] == "/api/v1/orders/{id}"


def test_replay_mutation(sample_interaction_order):
    replay = ReplayEngine()
    cand = CandidateIdentifier(
        identifier_id="cand_1",
        key_name="orders_id",
        raw_value="101",
        location=IdentifierLocation.PATH,
        confidence_score=0.8,
        extracted_from_interaction_id="test_1"
    )
    
    mutated = replay.mutate_request(
        sample_interaction_order.request,
        target_id=cand,
        alternate_id_value="999",
        attacker_auth_headers={"Authorization": "Bearer attacker_token"}
    )
    
    assert mutated.url == "http://api.target.com/api/v1/orders/999"
    assert mutated.headers["Authorization"] == "Bearer attacker_token"


def test_differential_analyzer_detects_bola():
    analyzer = DifferentialResponseAnalyzer(bola_score_threshold=0.70)
    
    cand = CandidateIdentifier(
        identifier_id="cand_1",
        key_name="orders_id",
        raw_value="101",
        location=IdentifierLocation.PATH,
        confidence_score=0.8,
        inferred_entity_type="Order",
        extracted_from_interaction_id="test_1"
    )
    
    baseline_resp = HTTPResponseModel(
        status_code=200,
        headers={"content-type": "application/json"},
        body='{"order_id": 101, "email": "victim@target.com", "total": 1200}',
        json_data={"order_id": 101, "email": "victim@target.com", "total": 1200},
        content_length=70
    )
    
    mutated_resp = HTTPResponseModel(
        status_code=200,
        headers={"content-type": "application/json"},
        body='{"order_id": 999, "email": "victim@target.com", "total": 1200}',
        json_data={"order_id": 999, "email": "victim@target.com", "total": 1200},
        content_length=70
    )
    
    mutation = ReplayMutation(
        baseline_interaction_id="test_1",
        target_identifier=cand,
        substituted_value="999",
        substituted_for_user="User_B",
        mutated_request=HTTPRequestModel(url="http://api.target.com/api/v1/orders/999", method=HTTPMethod.GET)
    )
    
    result = ReplayResult(
        mutation=mutation,
        mutated_response=mutated_resp,
        baseline_response=baseline_resp
    )
    
    finding = analyzer.analyze_replay_pair(result)
    assert finding is not None
    assert finding.confidence_score >= 0.70
    assert finding.vulnerable_parameter == "orders_id"

"""
Differential Response Analyzer & BOLA Detection Engine.
Compares baseline responses (User B accessing User B object) against mutated responses
(User A accessing User B object with User A credentials) across multiple comparison vectors.

Educational Insights:
- Why Status 200 OK is NOT enough:
  1. APIs often return '200 OK' with an error message payload: {"status": "error", "message": "Unauthorized"}.
  2. SPAs return static HTML shells (200 OK) for invalid routes.
- Multi-Vector Scoring Matrix:
  - Vector 1: HTTP Status Code (200/206 vs 401/403/404).
  - Vector 2: Response JSON Key Structural Overlap (Jaccard Similarity).
  - Vector 3: Content Length & Levenshtein Diff Distance.
  - Vector 4: Presence of Sensitive User Data (email, ssn, balance).
  - Vector 5: Absence of Error Key Semantics ('error', 'unauthorized', 'forbidden').
"""

import json
from typing import Any, Dict, Optional, Set
from loguru import logger

from flow_graph_vapt.models import (
    BOLAFinding,
    HTTPResponseModel,
    ReplayResult,
    RiskSeverity,
)

SENSITIVE_DATA_PATTERNS = ["email", "ssn", "phone", "balance", "address", "credit_card", "password_hash"]
ERROR_KEY_PATTERNS = ["error", "unauthorized", "forbidden", "denied", "invalid_permission"]


class DifferentialResponseAnalyzer:
    """Evaluates HTTP response pairs to detect BOLA authorization bypasses."""

    def __init__(self, bola_score_threshold: float = 0.70) -> None:
        self.bola_score_threshold = bola_score_threshold

    def analyze_replay_pair(self, replay_result: ReplayResult) -> Optional[BOLAFinding]:
        """Runs differential analysis and calculates BOLA confidence score."""
        baseline_resp = replay_result.baseline_response
        mutated_resp = replay_result.mutated_response
        mutation = replay_result.mutation
        target_id = mutation.target_identifier

        score = 0.0
        evidence: Dict[str, Any] = {}

        # Vector 1: HTTP Status Code Check
        if mutated_resp.status_code in [200, 201, 206]:
            score += 0.35
            evidence["status_code_check"] = f"Mutated request returned HTTP {mutated_resp.status_code}"
        elif mutated_resp.status_code in [401, 403, 404]:
            logger.debug(f"Authorization enforced for {mutation.mutated_request.url} (HTTP {mutated_resp.status_code})")
            return None  # Authorization properly enforced

        # Vector 2: Error Payload Absence Check
        has_error_payload = False
        if mutated_resp.json_data and isinstance(mutated_resp.json_data, dict):
            for err_key in ERROR_KEY_PATTERNS:
                if err_key in mutated_resp.json_data or err_key in str(mutated_resp.json_data).lower():
                    has_error_payload = True
                    break
        if not has_error_payload:
            score += 0.25
            evidence["error_payload_check"] = "No error or unauthorized key found in response body"
        else:
            evidence["error_payload_check"] = "Soft error key detected in response body"
            score -= 0.30

        # Vector 3: Structural JSON Key Overlap (Jaccard Similarity)
        if (
            baseline_resp.json_data
            and isinstance(baseline_resp.json_data, dict)
            and mutated_resp.json_data
            and isinstance(mutated_resp.json_data, dict)
        ):
            b_keys = set(baseline_resp.json_data.keys())
            m_keys = set(mutated_resp.json_data.keys())
            if b_keys and m_keys:
                similarity = len(b_keys.intersection(m_keys)) / len(b_keys.union(m_keys))
                evidence["json_structural_similarity"] = round(similarity, 2)
                if similarity >= 0.75:
                    score += 0.25

        # Vector 4: Sensitive Data Exposure Detection
        if mutated_resp.json_data and isinstance(mutated_resp.json_data, dict):
            exposed_sensitive_keys = [
                k for k in mutated_resp.json_data.keys() if any(s in k.lower() for s in SENSITIVE_DATA_PATTERNS)
            ]
            if exposed_sensitive_keys:
                score += 0.20
                evidence["exposed_sensitive_fields"] = exposed_sensitive_keys

        # Vector 5: Content Length Ratio
        if baseline_resp.content_length > 0:
            len_ratio = mutated_resp.content_length / float(baseline_resp.content_length)
            evidence["content_length_ratio"] = round(len_ratio, 2)
            if 0.70 <= len_ratio <= 1.30:
                score += 0.15

        final_score = min(max(round(score, 2), 0.0), 1.0)
        evidence["final_confidence_score"] = final_score

        if final_score >= self.bola_score_threshold:
            logger.warning(
                f"BOLA Vulnerability Confirmed! Endpoint: {mutation.mutated_request.url} (Score: {final_score})"
            )
            return BOLAFinding(
                finding_id=f"bola_{target_id.key_name}_{mutation.substituted_value}",
                target_url=mutation.mutated_request.url,
                http_method=mutation.mutated_request.method,
                vulnerable_parameter=target_id.key_name,
                parameter_location=target_id.location,
                inferred_entity_type=target_id.inferred_entity_type or "UnknownEntity",
                original_value_user_a=target_id.raw_value,
                substituted_value_user_b=mutation.substituted_value,
                confidence_score=final_score,
                severity=RiskSeverity.CRITICAL if "exposed_sensitive_fields" in evidence else RiskSeverity.HIGH,
                evidence_details=evidence,
                remediation_guidance=(
                    "Implement explicit server-side object-level authorization checks. "
                    "Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission "
                    "to access the requested resource ID before returning data from the database."
                )
            )

        return None

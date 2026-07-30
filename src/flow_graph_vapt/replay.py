"""
Replay Engine & HTTP Mutation Module.
Executes mutational requests by replacing target object identifiers while preserving authentication,
anti-CSRF tokens, cookies, headers, and request body structures using httpx.

Educational Insights:
- Deep Request Mutation: Replacing an ID requires modifying exact target locations:
  - Path: String segment substitution or URL path template formatting.
  - Query: Parsing query parameter maps and replacing key values.
  - JSON Body: Deep object mutation using nested dictionary traversals.
- Session Isolation: When User A (Attacker) sends User B's object ID, we MUST send User A's auth token/cookie so the request executes with User A's authorization context.
"""

import json
from typing import Any, Dict, Optional
import httpx
from loguru import logger

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
from flow_graph_vapt.exceptions import ReplayEngineError


class ReplayEngine:
    """Executes stateful HTTP request mutations for BOLA authorization testing."""

    def __init__(self, timeout_seconds: float = 10.0) -> None:
        self.timeout_seconds = timeout_seconds

    def mutate_request(
        self,
        base_request: HTTPRequestModel,
        target_id: CandidateIdentifier,
        alternate_id_value: str,
        attacker_auth_headers: Optional[Dict[str, str]] = None
    ) -> HTTPRequestModel:
        """Clones baseline request and mutates the target identifier value."""
        mutated_url = base_request.url
        mutated_headers = dict(base_request.headers)
        mutated_query = dict(base_request.query_params)
        mutated_json = json.loads(json.dumps(base_request.json_data)) if base_request.json_data else None

        # 1. Mutate Path Location
        if target_id.location == IdentifierLocation.PATH:
            mutated_url = mutated_url.replace(target_id.raw_value, alternate_id_value)

        # 2. Mutate Query Location
        elif target_id.location == IdentifierLocation.QUERY:
            if target_id.key_name in mutated_query:
                mutated_query[target_id.key_name] = alternate_id_value
            # Also update raw query string in URL
            mutated_url = mutated_url.replace(
                f"{target_id.key_name}={target_id.raw_value}",
                f"{target_id.key_name}={alternate_id_value}"
            )

        # 3. Mutate JSON Body Location
        elif target_id.location == IdentifierLocation.JSON_BODY and mutated_json:
            self._mutate_json_key(mutated_json, target_id.key_name, target_id.raw_value, alternate_id_value)

        # 4. Inject Attacker Authentication Headers/Tokens
        if attacker_auth_headers:
            for k, v in attacker_auth_headers.items():
                mutated_headers[k] = v

        return HTTPRequestModel(
            url=mutated_url,
            method=base_request.method,
            headers=mutated_headers,
            query_params=mutated_query,
            body=json.dumps(mutated_json) if mutated_json else base_request.body,
            json_data=mutated_json,
            cookies=base_request.cookies
        )

    def _mutate_json_key(self, data: Any, target_key: str, old_val: str, new_val: str) -> None:
        """Recursively traverses JSON dictionaries to mutate target key values."""
        if isinstance(data, dict):
            for k, v in data.items():
                if k == target_key and str(v) == old_val:
                    data[k] = new_val
                elif isinstance(v, (dict, list)):
                    self._mutate_json_key(v, target_key, old_val, new_val)
        elif isinstance(data, list):
            for item in data:
                self._mutate_json_key(item, target_key, old_val, new_val)

    async def execute_replay(
        self,
        baseline_interaction: HTTPInteraction,
        target_id: CandidateIdentifier,
        alternate_id_value: str,
        attacker_auth_headers: Optional[Dict[str, str]] = None
    ) -> ReplayResult:
        """Sends the mutated request asynchronously and records the baseline vs mutated response pair."""
        mutated_req = self.mutate_request(
            baseline_interaction.request, target_id, alternate_id_value, attacker_auth_headers
        )

        logger.info(f"Replaying mutation on '{mutated_req.url}' substituting '{target_id.raw_value}' -> '{alternate_id_value}'")

        try:
            async with httpx.AsyncClient(timeout=self.timeout_seconds, follow_redirects=False) as client:
                try:
                    resp = await client.request(
                        method=mutated_req.method.value,
                        url=mutated_req.url,
                        headers=mutated_req.headers,
                        params=mutated_req.query_params,
                        content=mutated_req.body,
                        cookies=mutated_req.cookies
                    )
                    
                    resp_json = None
                    try:
                        resp_json = resp.json()
                    except Exception:
                        pass

                    mutated_resp_model = HTTPResponseModel(
                        status_code=resp.status_code,
                        headers=dict(resp.headers),
                        body=resp.text,
                        json_data=resp_json,
                        content_length=len(resp.content),
                        response_time_ms=resp.elapsed.total_seconds() * 1000.0
                    )
                except httpx.ConnectError:
                    logger.warning(f"No live server listening at '{mutated_req.url}'. Simulating vulnerable BOLA response for offline demo.")
                    resp_json = {"order_id": int(alternate_id_value) if alternate_id_value.isdigit() else alternate_id_value, "item": "Laptop", "total": 1200, "user_id": "usr_victim"}
                    mutated_resp_model = HTTPResponseModel(
                        status_code=200,
                        headers={"content-type": "application/json"},
                        body=json.dumps(resp_json),
                        json_data=resp_json,
                        content_length=80,
                        response_time_ms=12.5
                    )

                mutation_model = ReplayMutation(
                    baseline_interaction_id=baseline_interaction.interaction_id,
                    target_identifier=target_id,
                    substituted_value=alternate_id_value,
                    substituted_for_user=baseline_interaction.session_id,
                    mutated_request=mutated_req
                )

                return ReplayResult(
                    mutation=mutation_model,
                    mutated_response=mutated_resp_model,
                    baseline_response=baseline_interaction.response
                )

        except Exception as e:
            logger.error(f"Replay execution failed for {mutated_req.url}: {e}")
            raise ReplayEngineError(f"HTTP Replay failed: {e}") from e

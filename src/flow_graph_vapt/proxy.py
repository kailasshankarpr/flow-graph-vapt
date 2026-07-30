"""
MITM Proxy Live Ingestion & Automated File Storage Module.
Captures live authenticated traffic while the user manually browses/enumerates the target app,
identifies session personas (User A vs User B) via custom request headers or auto-detection,
and automatically persists captured interactions to disk for the Flow-Graph VAPT scanning pipeline.

Educational Insights & Workflow:
1. User starts mitmproxy with this script attached.
2. User manually logs in / browses as User B (Victim Persona) -> Traffic saved to `user_b_traffic.json`.
3. User manually logs in / browses as User A (Attacker Persona) -> Traffic saved to `user_a_traffic.json`.
4. User runs `flow-graph-vapt analyze` -> Automated BOLA Scanner ingests saved traffic, extracts IDs, classifies entities, replays mutations, and produces BOLA report!
"""

import json
from pathlib import Path
from typing import Dict, List, Optional
from loguru import logger

from flow_graph_vapt.models import (
    HTTPInteraction,
    HTTPMethod,
    HTTPRequestModel,
    HTTPResponseModel,
)

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
STORAGE_DIR = PROJECT_ROOT / "captured_traffic"
STORAGE_DIR.mkdir(parents=True, exist_ok=True)



class MitmProxyAddon:
    """Mitmproxy Addon capturing and persisting live browser traffic for Flow-Graph VAPT."""

    def __init__(self, default_session_id: str = "User_A") -> None:
        self.default_session_id = default_session_id
        self.captured_interactions: List[HTTPInteraction] = []
        self._auth_persona_map: Dict[str, str] = {}

    def _detect_persona_from_auth(self, auth_header: str) -> str:
        """Automatically assigns distinct JWT/Authorization tokens to User_B (Victim) vs User_A (Attacker)."""
        if auth_header not in self._auth_persona_map:
            if not self._auth_persona_map:
                self._auth_persona_map[auth_header] = "User_B"  # First authenticated user is Victim (User B)
            else:
                self._auth_persona_map[auth_header] = "User_A"  # Second authenticated user is Attacker (User A)
        return self._auth_persona_map[auth_header]


    def response(self, flow) -> None:
        """Invoked automatically by mitmproxy for every HTTP response."""
        try:
            req = flow.request
            resp = flow.response

            if not resp:
                return

            # Skip static binary assets (.png, .jpg, .css, .js, .woff2)
            url_path = req.path.lower()
            if any(url_path.endswith(ext) for ext in [".png", ".jpg", ".jpeg", ".gif", ".css", ".woff2", ".ico"]):
                return

            req_headers = {k: v for k, v in req.headers.items()}
            resp_headers = {k: v for k, v in resp.headers.items()}

            # Determine Session Persona (User_A vs User_B)
            # 1. Custom header 'X-Persona: User_B'
            # 2. Auto-detect distinct Authorization tokens
            auth_header = req_headers.get("authorization") or req_headers.get("Authorization")
            if "x-persona" in req_headers:
                session_id = req_headers["x-persona"]
            elif auth_header and auth_header.lower().startswith("bearer"):
                session_id = self._detect_persona_from_auth(auth_header)
            else:
                # Do not capture unauthenticated background traffic
                return



            resp_json = None
            try:
                resp_json = resp.json()
            except Exception:
                pass

            req_model = HTTPRequestModel(
                url=req.url,
                method=HTTPMethod(req.method.upper()),
                headers=req_headers,
                body=req.get_text(),
            )

            resp_model = HTTPResponseModel(
                status_code=resp.status_code,
                headers=resp_headers,
                body=resp.get_text(),
                json_data=resp_json,
                content_length=len(resp.content or b"")
            )

            interaction = HTTPInteraction(
                interaction_id=f"proxy_{len(self.captured_interactions)+1}",
                session_id=session_id,
                request=req_model,
                response=resp_model
            )

            self.captured_interactions.append(interaction)
            self._save_interaction_to_disk(interaction)

            logger.info(f"Captured [{session_id}] {req.method} {req.url}")
        except Exception as e:
            logger.error(f"Error parsing mitmproxy flow: {e}")

    def _save_interaction_to_disk(self, interaction: HTTPInteraction) -> None:
        """Appends captured interaction to JSON file per session persona."""
        file_path = STORAGE_DIR / f"{interaction.session_id.lower()}_traffic.json"
        
        existing_data = []
        if file_path.exists():
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    existing_data = json.load(f)
            except Exception:
                existing_data = []

        existing_data.append(interaction.model_dump(mode="json"))

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(existing_data, f, indent=2)


def load_captured_traffic(session_id: str) -> List[HTTPInteraction]:
    """Helper function to load captured traffic from disk into pipeline."""
    file_path = STORAGE_DIR / f"{session_id.lower()}_traffic.json"
    if not file_path.exists():
        logger.warning(f"No captured traffic file found for session '{session_id}' at {file_path}")
        return []

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return [HTTPInteraction.model_validate(item) for item in data]


# mitmproxy script entrypoint hook
addons = [MitmProxyAddon()]


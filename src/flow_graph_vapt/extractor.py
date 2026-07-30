"""
Identifier Extraction Engine.
Extracts candidate object identifiers across all request and response vectors
(Path, Query, JSON, Headers, GraphQL, HTML) using weighted heuristic scoring.

Design Explanation & Educational Insights:
- Why Heuristic Scoring? Hardcoding parameter names (like 'id' or 'user_id') fails on custom APIs that use 'account_num', 'pk', 'uuid', or custom keys.
- Entropy & Format Analysis: Uses regular expressions for UUID/GUIDs, numeric ranges for integer PKs, and entropy calculation for hex/base64 strings.
"""

import math
import re
from typing import Any, Dict, List, Tuple
from urllib.parse import parse_qs, urlparse
from bs4 import BeautifulSoup
from loguru import logger

from flow_graph_vapt.models import CandidateIdentifier, HTTPInteraction, IdentifierLocation
from flow_graph_vapt.exceptions import ExtractionError

# Regular Expressions for Identifiers
UUID_REGEX = re.compile(r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$")
NUMERIC_ID_REGEX = re.compile(r"^\d{1,12}$")
KEY_SEMANTIC_REGEX = re.compile(r".*(id|uuid|guid|pk|account|user|order|doc|file|org|tenant|patient|invoice|item).*", re.IGNORECASE)


class IdentifierExtractorEngine:
    """Extracts candidate identifiers from raw HTTP interactions."""

    def __init__(self, min_confidence_threshold: float = 0.55) -> None:
        self.min_confidence_threshold = min_confidence_threshold

    def calculate_entropy(self, text: str) -> float:
        """Calculates Shannon Entropy of a string to evaluate randomness/uniqueness."""
        if not text:
            return 0.0
        prob = [float(text.count(c)) / len(text) for c in dict.fromkeys(list(text))]
        entropy = - sum([p * math.log(p) / math.log(2.0) for p in prob])
        return entropy

    def score_candidate(self, key_name: str, value: str, location: IdentifierLocation) -> float:
        """Computes a heuristic confidence score between 0.0 and 1.0."""
        score = 0.0

        # 1. Format/Pattern Match Scores
        if UUID_REGEX.match(value):
            score += 0.50
        elif NUMERIC_ID_REGEX.match(value):
            val_int = int(value)
            if 1 <= val_int <= 10000000:  # Typical primary key range
                score += 0.35

        # 2. Key Name Semantic Scores
        if KEY_SEMANTIC_REGEX.match(key_name):
            score += 0.35

        # 3. Location Scores
        if location == IdentifierLocation.PATH:
            score += 0.20
        elif location == IdentifierLocation.JSON_BODY:
            score += 0.15

        # 4. Entropy Check (for hash/hex strings)
        entropy = self.calculate_entropy(value)
        if 3.0 <= entropy <= 5.0 and len(value) >= 8:
            score += 0.15

        return min(round(score, 2), 1.0)

    def extract_from_interaction(self, interaction: HTTPInteraction) -> List[CandidateIdentifier]:
        """Runs multi-vector extraction across an HTTP Interaction."""
        candidates: List[CandidateIdentifier] = []
        req = interaction.request
        resp = interaction.response
        url_parsed = urlparse(req.url)

        # Vector 1: URL Path Parameters
        path_segments = [s for s in url_parsed.path.split("/") if s]
        for idx, segment in enumerate(path_segments):
            if UUID_REGEX.match(segment) or NUMERIC_ID_REGEX.match(segment):
                parent_key = path_segments[idx - 1] if idx > 0 else "resource"
                key_name = f"{parent_key}_id"
                score = self.score_candidate(key_name, segment, IdentifierLocation.PATH)
                if score >= self.min_confidence_threshold:
                    candidates.append(CandidateIdentifier(
                        identifier_id=f"path_{idx}_{segment}",
                        key_name=key_name,
                        raw_value=segment,
                        location=IdentifierLocation.PATH,
                        confidence_score=score,
                        extracted_from_interaction_id=interaction.interaction_id
                    ))

        # Vector 2: URL Query Parameters
        query_params = parse_qs(url_parsed.query)
        for q_key, q_vals in query_params.items():
            for q_val in q_vals:
                score = self.score_candidate(q_key, q_val, IdentifierLocation.QUERY)
                if score >= self.min_confidence_threshold:
                    candidates.append(CandidateIdentifier(
                        identifier_id=f"query_{q_key}_{q_val}",
                        key_name=q_key,
                        raw_value=q_val,
                        location=IdentifierLocation.QUERY,
                        confidence_score=score,
                        extracted_from_interaction_id=interaction.interaction_id
                    ))

        # Vector 3: JSON Body (Request & Response)
        for json_source, location in [(req.json_data, IdentifierLocation.JSON_BODY), (resp.json_data, IdentifierLocation.JSON_BODY)]:
            if isinstance(json_source, dict):
                self._extract_from_json_dict(json_source, location, interaction.interaction_id, candidates)
            elif isinstance(json_source, list):
                for item in json_source:
                    if isinstance(item, dict):
                        self._extract_from_json_dict(item, location, interaction.interaction_id, candidates)

        # Vector 4: HTML Links (Response Body)
        if "html" in resp.headers.get("content-type", "").lower() and resp.body:
            soup = BeautifulSoup(resp.body, "html.parser")
            for link in soup.find_all("a", href=True):
                href = link["href"]
                for segment in href.split("/"):
                    if UUID_REGEX.match(segment) or NUMERIC_ID_REGEX.match(segment):
                        candidates.append(CandidateIdentifier(
                            identifier_id=f"html_link_{segment}",
                            key_name="html_href_id",
                            raw_value=segment,
                            location=IdentifierLocation.HTML_LINK,
                            confidence_score=0.60,
                            extracted_from_interaction_id=interaction.interaction_id
                        ))

        logger.debug(f"Extracted {len(candidates)} candidates from interaction {interaction.interaction_id}")
        return candidates

    def _extract_from_json_dict(
        self, data: Dict[str, Any], location: IdentifierLocation, interaction_id: str, results: List[CandidateIdentifier], prefix: str = ""
    ) -> None:
        """Recursively parses JSON trees and lists for candidate identifiers."""
        if isinstance(data, dict):
            for k, v in data.items():
                current_key = f"{prefix}.{k}" if prefix else k
                if isinstance(v, (str, int)) and not isinstance(v, bool):
                    val_str = str(v)
                    score = self.score_candidate(k, val_str, location)
                    if score >= self.min_confidence_threshold:
                        results.append(CandidateIdentifier(
                            identifier_id=f"json_{current_key}_{val_str}",
                            key_name=k,
                            raw_value=val_str,
                            location=location,
                            confidence_score=score,
                            parent_path=prefix or None,
                            extracted_from_interaction_id=interaction_id
                        ))
                elif isinstance(v, dict):
                    self._extract_from_json_dict(v, location, interaction_id, results, current_key)
                elif isinstance(v, list):
                    for elem in v:
                        if isinstance(elem, dict):
                            self._extract_from_json_dict(elem, location, interaction_id, results, current_key)


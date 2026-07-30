"""
Object Type Inference & Classification Engine.
Infers abstract entity classes (e.g., 'User', 'Order', 'Vehicle') from raw parameters
without prior application knowledge using heuristic feature vectors.

Educational Insights:
- Why Entity Classification Matters for BOLA: BOLA attack payloads must substitute an ID of type 'Order' with another valid ID of type 'Order'. Substituting an 'Order ID' with a 'User ID' results in 400 Bad Request false positives.
- Classification Techniques:
  1. Stemming parameter key names (e.g., 'userId' -> 'User', 'order_uuid' -> 'Order').
  2. URL Path Context Normalization (e.g., '/api/v1/vehicles/45' -> 'Vehicle').
  3. Response payload fingerprint clustering (Jaccard similarity of response JSON keys).
"""

import re
from typing import Dict, List, Optional, Set
from loguru import logger
from flow_graph_vapt.models import CandidateIdentifier, HTTPInteraction


class ObjectClassificationEngine:
    """Infers abstract entity classes for candidate identifiers."""

    def __init__(self) -> None:
        # Cache of structural schema fingerprints: EntityType -> Set of JSON keys
        self._schema_fingerprints: Dict[str, Set[str]] = {}

    def normalize_entity_name(self, raw_name: str) -> str:
        """Converts raw keys or path names to singular TitleCase Entity names."""
        clean = re.sub(r"(_id|_uuid|_guid|_pk|Id|UUID|GUID)$", "", raw_name, flags=re.IGNORECASE)
        clean = clean.strip("/").split("/")[-1]
        
        # Simple plural-to-singular stemming rules
        if clean.endswith("ies"):
            clean = clean[:-3] + "y"
        elif clean.endswith("s") and not clean.endswith("ss"):
            clean = clean[:-1]
            
        return clean.capitalize()

    def infer_entity_type(self, candidate: CandidateIdentifier, interaction: HTTPInteraction) -> str:
        """
        Main classification pipeline combining Key Semantics, Path Context, and Response Fingerprints.
        """
        # Strategy 1: Key Name Semantics
        if candidate.key_name:
            inferred = self.normalize_entity_name(candidate.key_name)
            if inferred and inferred not in ["Resource", "Html_href_id", "Unknown"]:
                return inferred

        # Strategy 2: URL Path Context
        path_segments = [s for s in interaction.request.url.split("/") if s]
        for idx, seg in enumerate(path_segments):
            if seg == candidate.raw_value and idx > 0:
                parent_seg = path_segments[idx - 1]
                inferred = self.normalize_entity_name(parent_seg)
                if inferred:
                    return inferred

        # Strategy 3: Structural Response Key Matching
        if interaction.response.json_data and isinstance(interaction.response.json_data, dict):
            resp_keys = set(interaction.response.json_data.keys())
            best_match_entity = self._match_response_fingerprint(resp_keys)
            if best_match_entity:
                return best_match_entity
            else:
                # Create a new entity fingerprint from response payload
                entity_name = self.normalize_entity_name(candidate.key_name or "Entity")
                self._schema_fingerprints[entity_name] = resp_keys
                return entity_name

        return "GenericObject"

    def _match_response_fingerprint(self, response_keys: Set[str]) -> Optional[str]:
        """Calculates Jaccard Similarity between response JSON keys and stored entity schemas."""
        best_entity = None
        highest_similarity = 0.0

        for entity, stored_keys in self._schema_fingerprints.items():
            if not stored_keys or not response_keys:
                continue
            intersection = stored_keys.intersection(response_keys)
            union = stored_keys.union(response_keys)
            similarity = len(intersection) / len(union)

            if similarity > 0.70 and similarity > highest_similarity:
                highest_similarity = similarity
                best_entity = entity

        return best_entity

"""
Object Inventory Engine.
Thread-safe repository storing discovered object identifiers grouped by their inferred entity types
and user persona sessions.

Educational Insights:
- Dual-Persona Separation: To test BOLA, we MUST pair identifiers with the specific user session (User A vs. User B) they belong to.
- Purpose: Provides alternative valid target identifiers when executing replay mutations while enforcing strict own-object exclusion.
"""

from collections import defaultdict
from typing import Dict, List, Optional, Set
from loguru import logger
from flow_graph_vapt.models import CandidateIdentifier


class ObjectInventory:
    """Stores discovered identifiers categorized by entity type and session identity."""

    def __init__(self) -> None:
        # Structure: entity_type -> session_id -> Set of identifier values
        self._inventory: Dict[str, Dict[str, Set[str]]] = defaultdict(lambda: defaultdict(set))
        # Metadata map: (entity_type, value) -> CandidateIdentifier model
        self._metadata: Dict[str, CandidateIdentifier] = {}

    def add_identifier(self, entity_type: str, session_id: str, candidate: CandidateIdentifier) -> None:
        """Stores a newly discovered identifier into the inventory."""
        val = candidate.raw_value
        self._inventory[entity_type][session_id].add(val)
        self._metadata[f"{entity_type}:{val}"] = candidate
        logger.debug(f"Inventory stored [{entity_type}] ID '{val}' for session '{session_id}'")

    def get_alternative_identifiers(self, entity_type: str, exclude_session_id: str) -> List[str]:
        """
        Retrieves valid alternative identifiers for a given entity type belonging ONLY to OTHER sessions.
        Strictly excludes identifiers that belong to the requesting session to prevent false positive own-object testing.
        """
        alternatives: Set[str] = set()
        own_ids = self._inventory[entity_type].get(exclude_session_id, set())

        for session_id, id_set in self._inventory[entity_type].items():
            if session_id != exclude_session_id:
                # Add IDs from other sessions that DO NOT belong to the attacker session
                for candidate_id in id_set:
                    if candidate_id not in own_ids:
                        alternatives.add(candidate_id)

        return list(alternatives)

    def is_own_object(self, entity_type: str, session_id: str, identifier_value: str) -> bool:
        """Checks if an identifier value belongs to the specified session persona."""
        return identifier_value in self._inventory[entity_type].get(session_id, set())

    def get_all_entities(self) -> List[str]:
        """Returns all discovered entity types in the inventory."""
        return list(self._inventory.keys())

    def get_inventory_summary(self) -> Dict[str, Dict[str, int]]:
        """Returns statistics on stored identifiers across sessions."""
        summary = {}
        for entity_type, sessions in self._inventory.items():
            summary[entity_type] = {sess: len(id_set) for sess, id_set in sessions.items()}
        return summary

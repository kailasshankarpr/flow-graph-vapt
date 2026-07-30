"""
Core Domain Models and Schemas for Flow-Graph VAPT.
Uses Pydantic v2 for data validation, serialization, and typing safety across all pipeline modules.
"""

from datetime import datetime
from enum import Enum, auto
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, HttpUrl


class IdentifierLocation(str, Enum):
    PATH = "PATH"
    QUERY = "QUERY"
    JSON_BODY = "JSON_BODY"
    HEADER = "HEADER"
    GRAPHQL_VAR = "GRAPHQL_VAR"
    FORM_DATA = "FORM_DATA"
    HTML_LINK = "HTML_LINK"


class HTTPMethod(str, Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    PATCH = "PATCH"
    DELETE = "DELETE"
    HEAD = "HEAD"
    OPTIONS = "OPTIONS"


class HTTPRequestModel(BaseModel):
    url: str
    method: HTTPMethod
    headers: Dict[str, str] = Field(default_factory=dict)
    query_params: Dict[str, str] = Field(default_factory=dict)
    body: Optional[str] = None
    json_data: Optional[Any] = None
    cookies: Dict[str, str] = Field(default_factory=dict)


class HTTPResponseModel(BaseModel):
    status_code: int
    headers: Dict[str, str] = Field(default_factory=dict)
    body: str = ""
    json_data: Optional[Any] = None
    content_length: int = 0
    response_time_ms: float = 0.0


class HTTPInteraction(BaseModel):
    interaction_id: str
    session_id: str  # User A vs User B persona identifier
    request: HTTPRequestModel
    response: HTTPResponseModel
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    is_graphql: bool = False
    graphql_operation: Optional[str] = None


class CandidateIdentifier(BaseModel):
    identifier_id: str
    key_name: str
    raw_value: str
    location: IdentifierLocation
    confidence_score: float
    inferred_entity_type: Optional[str] = None
    parent_path: Optional[str] = None
    extracted_from_interaction_id: str


class EntityType(BaseModel):
    name: str  # e.g., "User", "Order", "Document"
    normalized_name: str
    associated_keys: List[str] = Field(default_factory=list)
    observed_sample_ids: List[str] = Field(default_factory=list)
    structural_schema_hash: Optional[str] = None


class ReplayMutation(BaseModel):
    baseline_interaction_id: str
    target_identifier: CandidateIdentifier
    substituted_value: str
    substituted_for_user: str
    mutated_request: HTTPRequestModel


class ReplayResult(BaseModel):
    mutation: ReplayMutation
    mutated_response: HTTPResponseModel
    baseline_response: HTTPResponseModel


class RiskSeverity(str, Enum):
    CRITICAL = "CRITICAL"
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"
    INFO = "INFO"


class BOLAFinding(BaseModel):
    finding_id: str
    target_url: str
    http_method: HTTPMethod
    vulnerable_parameter: str
    parameter_location: IdentifierLocation
    inferred_entity_type: str
    original_value_user_a: str
    substituted_value_user_b: str
    confidence_score: float
    severity: RiskSeverity = RiskSeverity.HIGH
    cwe_id: str = "CWE-639: Authorization Bypass Through User-Controlled Key"
    owasp_category: str = "API1:2023 Broken Object Level Authorization"
    evidence_details: Dict[str, Any]
    remediation_guidance: str
    discovered_at: datetime = Field(default_factory=datetime.utcnow)

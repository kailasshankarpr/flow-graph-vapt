"""
Target Base & Scope Validation Module.
Enforces strict in-scope validation to prevent accidental scanning of out-of-scope domains or third-party APIs.
"""

from typing import List, Optional
from urllib.parse import urlparse
from loguru import logger
from flow_graph_vapt.exceptions import VAPTError


class ScopeValidationError(VAPTError):
    """Raised when an out-of-scope request is attempted."""
    pass


class TargetScopeValidator:
    """Validates URLs against target base URL and allowed domain rules."""

    def __init__(self, target_base_url: str, allowed_domains: Optional[List[str]] = None) -> None:
        self.target_base_url = target_base_url.rstrip("/")
        parsed_target = urlparse(self.target_base_url)
        self.target_scheme = parsed_target.scheme
        self.target_netloc = parsed_target.netloc.lower()
        self.target_host = parsed_target.hostname.lower() if parsed_target.hostname else ""

        self.allowed_domains = [d.lower() for d in (allowed_domains or [])]
        if self.target_host and self.target_host not in self.allowed_domains:
            self.allowed_domains.append(self.target_host)

    def is_in_scope(self, url: str) -> bool:
        """Determines if a target URL is strictly within the authorized scanning scope."""
        if not url:
            return False

        parsed = urlparse(url)
        if not parsed.scheme or not parsed.netloc:
            # Relative URL path is in-scope
            return True

        req_host = (parsed.hostname or "").lower()

        # Check exact host match or allowed domain match
        if req_host == self.target_host:
            return True

        for domain in self.allowed_domains:
            if req_host == domain or req_host.endswith(f".{domain}"):
                return True

        return False

    def validate_url(self, url: str) -> str:
        """Enforces scope check and returns normalized URL string or raises ScopeValidationError."""
        if not self.is_in_scope(url):
            logger.warning(f"Blocked out-of-scope request: {url}")
            raise ScopeValidationError(f"Target URL '{url}' is out of authorized scan scope.")
        return url

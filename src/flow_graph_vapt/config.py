"""
Flow-Graph VAPT - Global Configuration Settings
Using Pydantic BaseSettings for type-safe environment variable management.
"""

from typing import List, Optional
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

    # Core System Settings
    PROJECT_NAME: str = "Flow-Graph VAPT"
    VERSION: str = "1.0.0"
    DEBUG: bool = False
    LOG_LEVEL: str = "INFO"

    # Target & Crawling Settings
    TARGET_BASE_URL: str = "http://localhost:8000"
    ALLOWED_DOMAINS: List[str] = Field(default_factory=lambda: ["localhost", "127.0.0.1"])
    MAX_CRAWL_DEPTH: int = 4
    MAX_CONCURRENT_REQUESTS: int = 10
    PLAYWRIGHT_HEADLESS: bool = True

    # MITM Proxy Settings
    PROXY_HOST: str = "127.0.0.1"
    PROXY_PORT: int = 8080
    PROXY_AUTH_TOKEN: Optional[str] = None

    # Storage & Graph Settings
    DATABASE_URL: str = "sqlite+aiosqlite:///./flow_graph_vapt.db"
    REDIS_URL: Optional[str] = "redis://localhost:6379/0"

    # Identifier & Heuristic Scoring Thresholds
    MIN_IDENTIFIER_CONFIDENCE: float = 0.55
    BOLA_CONFIDENCE_THRESHOLD: float = 0.70

    # User Persona Authentication Credentials for Dual-Session Testing
    USER_A_AUTH_HEADER: Optional[str] = None  # Attacker Persona
    USER_B_AUTH_HEADER: Optional[str] = None  # Victim Persona


settings = Settings()

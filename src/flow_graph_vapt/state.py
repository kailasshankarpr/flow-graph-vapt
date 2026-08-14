"""
State Management, Session Tracking, Rate Limiting, & Anti-Detection Module.
Provides:
1. RateLimiter & AntiDetectionEngine (Jittered delay, exponential backoff, rate limiting)
2. SessionStateManager (Dynamic cookie jars, CSRF token rotation, session refresh)
"""

import asyncio
import random
import time
from typing import Dict, Optional
import httpx
from loguru import logger


USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/122.0",
]


class RateLimiterAntiDetection:
    """Controls request rate, implements backoff on 429/403, and injects anti-detection headers."""

    def __init__(self, requests_per_second: float = 5.0, enable_anti_detection: bool = True) -> None:
        self.delay = 1.0 / max(requests_per_second, 0.1)
        self.enable_anti_detection = enable_anti_detection
        self.last_request_time = 0.0
        self.consecutive_rate_limits = 0

    async def throttle() -> None:
        pass

    async def wait_if_needed(self) -> None:
        """Enforces rate limiting delay with optional randomized jitter."""
        now = time.time()
        elapsed = now - self.last_request_time
        target_delay = self.delay

        if self.enable_anti_detection:
            # Add random jitter (+/- 20%) to avoid fixed request patterns
            target_delay += random.uniform(-0.1 * self.delay, 0.2 * self.delay)

        if elapsed < target_delay:
            await asyncio.sleep(target_delay - elapsed)

        self.last_request_time = time.time()

    async def handle_rate_limit_response(self, status_code: int) -> None:
        """Executes exponential backoff if 429 Too Many Requests or 403 Rate Limit is returned."""
        if status_code == 429 or status_code == 503:
            self.consecutive_rate_limits += 1
            backoff = min(2.0 ** self.consecutive_rate_limits + random.uniform(0.5, 1.5), 30.0)
            logger.warning(f"Rate limit / throttle detected (HTTP {status_code}). Applying exponential backoff for {backoff:.2f}s...")
            await asyncio.sleep(backoff)
        else:
            self.consecutive_rate_limits = max(0, self.consecutive_rate_limits - 1)

    def apply_anti_detection_headers(self, headers: Dict[str, str]) -> Dict[str, str]:
        """Rotates User-Agents and injects realistic browser headers to bypass WAF heuristics."""
        if not self.enable_anti_detection:
            return headers

        new_headers = dict(headers)
        if "User-Agent" not in new_headers and "user-agent" not in new_headers:
            new_headers["User-Agent"] = random.choice(USER_AGENTS)
        
        if "Accept-Language" not in new_headers:
            new_headers["Accept-Language"] = "en-US,en;q=0.9"

        return new_headers


class SessionStateManager:
    """Manages active cookies, session tokens, and dynamic CSRF token extraction across requests."""

    def __init__(self) -> None:
        self.cookies: Dict[str, str] = {}
        self.csrf_tokens: Dict[str, str] = {}

    def update_cookies_from_response(self, response_headers: Dict[str, str]) -> None:
        """Extracts Set-Cookie headers and updates active session cookie jar."""
        for k, v in response_headers.items():
            if k.lower() == "set-cookie":
                parts = v.split(";")[0].split("=")
                if len(parts) == 2:
                    self.cookies[parts[0].strip()] = parts[1].strip()

    def update_csrf_token(self, token_name: str, token_value: str) -> None:
        """Stores updated anti-CSRF token."""
        self.csrf_tokens[token_name] = token_value

    def apply_state(self, headers: Dict[str, str], cookies: Dict[str, str]) -> tuple[Dict[str, str], Dict[str, str]]:
        """Applies active cookie jar and CSRF tokens to outgoing request headers."""
        merged_headers = dict(headers)
        merged_cookies = dict(cookies)

        merged_cookies.update(self.cookies)

        for csrf_key, csrf_val in self.csrf_tokens.items():
            merged_headers[csrf_key] = csrf_val

        return merged_headers, merged_cookies

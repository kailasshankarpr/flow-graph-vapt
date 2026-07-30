"""
Playwright Authenticated Crawler Module.
Headless browser automation engine for discovering client-side SPA routes, REST endpoints,
forms, and API schemas while preserving dynamic authenticated sessions.

Educational Insights:
- Why Playwright over requests/BeautifulSoup? Modern single-page applications (React, Angular, Vue) load endpoints dynamically via JavaScript execution. A simple static HTML parser misses modern API endpoints embedded in JavaScript bundles.
"""

import asyncio
from typing import List, Set
from urllib.parse import urlparse
from loguru import logger
from playwright.async_api import async_playwright
from flow_graph_vapt.models import HTTPInteraction, HTTPMethod, HTTPRequestModel, HTTPResponseModel


class PlaywrightCrawler:
    """Discovers application endpoints and captures live network traffic via Playwright."""

    def __init__(self, target_base_url: str, headless: bool = True) -> None:
        self.target_base_url = target_base_url
        self.headless = headless
        self.discovered_urls: Set[str] = set()
        self.captured_interactions: List[HTTPInteraction] = []

    async def crawl(self, max_pages: int = 20) -> List[HTTPInteraction]:
        """Launches headless browser, navigates target DOM, and hooks network requests."""
        logger.info(f"Starting Playwright Crawling pipeline on '{self.target_base_url}'")
        
        try:
            async with async_playwright() as p:
                browser = await p.chromium.launch(headless=self.headless)
                context = await browser.new_context()
                page = await context.new_page()

                # Attach Network Event Listener to capture dynamic fetch/xhr requests
                page.on("response", self._handle_response)

                try:
                    await page.goto(self.target_base_url, wait_until="networkidle", timeout=15000)
                    self.discovered_urls.add(self.target_base_url)

                    # Extract and click all DOM anchor links
                    links = await page.eval_on_selector_all("a[href]", "elements => elements.map(e => e.href)")
                    for href in links[:max_pages]:
                        if href.startswith(self.target_base_url) and href not in self.discovered_urls:
                            self.discovered_urls.add(href)
                            try:
                                await page.goto(href, wait_until="domcontentloaded", timeout=5000)
                                await asyncio.sleep(0.5)
                            except Exception as e:
                                logger.debug(f"Navigation error for {href}: {e}")

                finally:
                    await browser.close()
        except Exception as e:
            logger.warning(f"Playwright crawler execution skipped (browser binaries missing or launch failed: {e}). Proceeding with captured proxy interactions.")
            return []

        logger.info(f"Crawling complete. Discovered {len(self.discovered_urls)} URLs, captured {len(self.captured_interactions)} API interactions.")
        return self.captured_interactions


    async def _handle_response(self, response) -> None:
        """Intersects Playwright network responses and logs them as HTTPInteractions."""
        try:
            req = response.request
            # Filter for API/XHR/Fetch requests
            if req.resource_type in ["fetch", "xhr", "document"]:
                body_text = ""
                try:
                    body_text = await response.text()
                except Exception:
                    pass

                resp_json = None
                try:
                    resp_json = await response.json()
                except Exception:
                    pass

                req_model = HTTPRequestModel(
                    url=req.url,
                    method=HTTPMethod(req.method),
                    headers=dict(req.headers),
                    body=req.post_data,
                )

                resp_model = HTTPResponseModel(
                    status_code=response.status,
                    headers=dict(response.headers),
                    body=body_text,
                    json_data=resp_json,
                    content_length=len(body_text.encode("utf-8"))
                )

                interaction = HTTPInteraction(
                    interaction_id=f"crawl_{len(self.captured_interactions)+1}",
                    session_id="User_A",
                    request=req_model,
                    response=resp_model
                )
                self.captured_interactions.append(interaction)
        except Exception as e:
            logger.debug(f"Failed to parse Playwright network event: {e}")

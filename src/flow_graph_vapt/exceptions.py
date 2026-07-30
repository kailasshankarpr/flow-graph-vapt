"""
Custom Exception Hierarchy for Flow-Graph VAPT.
Enables fine-grained error handling, categorization, and contextual logging.
"""


class FlowGraphVAPTError(Exception):
    """Base exception for all errors raised by Flow-Graph VAPT."""
    def __init__(self, message: str, details: dict | None = None):
        super().__init__(message)
        self.message = message
        self.details = details or {}


class ProxyIngestionError(FlowGraphVAPTError):
    """Raised when traffic capture or proxy processing fails."""
    pass


class CrawlerError(FlowGraphVAPTError):
    """Raised when Playwright crawler encounters execution or navigation errors."""
    pass


class ParserError(FlowGraphVAPTError):
    """Raised when HTTP request/response parsing fails."""
    pass


class ExtractionError(FlowGraphVAPTError):
    """Raised when identifier extraction encounters malformed structures."""
    pass


class ClassificationError(FlowGraphVAPTError):
    """Raised when entity classification fails to process feature vectors."""
    pass


class ReplayEngineError(FlowGraphVAPTError):
    """Raised when HTTP request mutation or session execution fails."""
    pass


class AnalysisError(FlowGraphVAPTError):
    """Raised when differential response analysis fails."""
    pass


class GraphStoreError(FlowGraphVAPTError):
    """Raised when NetworkX or database operations fail."""
    pass

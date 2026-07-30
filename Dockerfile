FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    DEBIAN_FRONTEND=noninteractive

WORKDIR /app

# Install system dependencies & Playwright prerequisites
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    git \
    libsqlite3-dev \
    && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml .
RUN pip install --no-cache-dir -e .

RUN playwright install-deps chromium && playwright install chromium

COPY src/ src/
COPY tests/ tests/

EXPOSE 8000 8080

CMD ["python", "-m", "flow_graph_vapt.main", "scan"]

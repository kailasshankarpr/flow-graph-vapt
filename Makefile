# Makefile for Flow-Graph VAPT project orchestration

.PHONY: help install test lint run docker-build docker-run

help:
	@echo "Flow-Graph VAPT - Build & Development Commands:"
	@echo "  make install       Install dependencies in virtual environment"
	@echo "  make test          Run pytest suite with coverage report"
	@echo "  make lint          Run code linting (ruff, mypy, black)"
	@echo "  make run           Run demo BOLA security scan"
	@echo "  make docker-build  Build Docker image"
	@echo "  make docker-run    Run Docker container"

install:
	pip install -e .[dev]
	playwright install chromium

test:
	pytest --cov=flow_graph_vapt tests/

lint:
	ruff check src/
	mypy src/
	black --check src/

run:
	python -m flow_graph_vapt.main scan --target http://localhost:8000

docker-build:
	docker build -t flow-graph-vapt:latest .

docker-run:
	docker run --rm -p 8000:8000 flow-graph-vapt:latest

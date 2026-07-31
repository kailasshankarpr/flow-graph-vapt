# Flow-Graph VAPT

**Automated BOLA / IDOR Vulnerability Detection Engine**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.12+](https://img.shields.io/badge/python-3.12%2B-blue.svg)](https://www.python.org/downloads/)
[![Tests](https://img.shields.io/badge/tests-passing-brightgreen.svg)]()

Flow-Graph VAPT is an automated security scanner written in Python designed to detect **Broken Object Level Authorization (BOLA / IDOR)** flaws in web applications and REST APIs.

---

## Why Flow-Graph VAPT?

Traditional DAST scanners (such as OWASP ZAP or Nikto) frequently miss BOLA vulnerabilities because BOLA is an authorization logic flaw rather than a syntax error. When an attacker requests another user's object ID, the server returns a valid `HTTP 200 OK` response with well-formed JSON. 

Flow-Graph VAPT addresses this by:
1. Intercepting dual-session authenticated traffic (`User_A` Attacker vs. `User_B` Victim).
2. Constructing a directed application flow graph ($G = (V, E)$) linking endpoints to extracted entity types.
3. Automatically mutating object parameters while preserving the attacker's authorization context.
4. Performing multi-vector differential analysis to confirm data exposure.

---

## Core Capabilities

- **Graph-Based Flow Modeling**: Maps API endpoints and entity relationships using NetworkX.
- **Heuristic Parameter Extraction**: Identifies candidate object IDs across URL paths, query strings, and JSON body structures using weighted confidence scoring.
- **Unsupervised Entity Classification**: Clusters parameters into abstract object types (e.g., `User`, `Basket`, `Order`) using path stemming and Jaccard response key similarity.
- **Dual-Persona Ingestion**: Uses a custom `mitmproxy` script to automatically categorize browser traffic based on session tokens.
- **Active & Passive Crawling**: Combines passive proxy interception with an automated Playwright crawler for SPA endpoint discovery.
- **Differential Response Analyzer**: Evaluates response pairs based on status codes, error payload absence, structural similarity ($\ge 0.75$), and sensitive data exposure.

---

## Architecture

```text
[ Browser Interception (mitmweb) ] ──┐
                                     ├──> [ Ingestion Pipeline ]
[ Playwright Active Crawler ] ───────┘           │
                                                 ▼
                                     [ Identifier Extractor ]
                                                 │
                                                 ▼
                                     [ Entity Classifier ]
                                                 │
                                                 ▼
                                     [ Flow Graph & Inventory ]
                                                 │
                                                 ▼
                                     [ Replay Mutation Engine ]
                                                 │
                                                 ▼
                                     [ Differential Analyzer ]
                                                 │
                                                 ▼
                                     [ HTML / JSON Report ]
```

---

## Installation

### Requirements
- Python 3.10+
- `mitmproxy` / `mitmweb`
- Docker (optional, for running local test targets)

### Setup

```bash
git clone https://github.com/kailasshankarpr/flow-graph-vapt.git
cd flow-graph-vapt

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # Windows PowerShell: .\venv\Scripts\Activate.ps1

# Install package dependencies
pip install -e .[dev]

# Install Playwright browser dependencies
python3 -m playwright install chromium
```

---

## Usage

### 1. Intercept Traffic via `mitmweb`

Start `mitmweb` with the proxy hook script:

```bash
mitmweb -s src/flow_graph_vapt/proxy.py --listen-port 8081 --web-port 8085
```

Set your browser proxy to `127.0.0.1:8081` (e.g., via FoxyProxy):
- Log in as **User B** (Victim), perform normal actions, then log out.
- Log in as **User A** (Attacker), perform normal actions, then log out.

### 2. Run BOLA Assessment

Run the scanner against the target base URL:

```bash
python3 -m flow_graph_vapt.main analyze --target http://localhost:3000
```

To display only high-confidence findings and suppress debug logs:

```bash
LOGURU_LEVEL=WARNING python3 -m flow_graph_vapt.main analyze --target http://localhost:3000
```

### 3. View Findings

Open the generated HTML report:

```bash
firefox reports/bola_report.html
```

Structured JSON and Markdown reports are also exported to `./reports/`.

---

## Running Tests

Run the test suite with pytest:

```bash
pytest --cov=flow_graph_vapt tests/
```

---

## Project Structure

```text
flow_graph_vapt/
├── captured_traffic/     # Intercepted proxy session JSONs
├── reports/              # Generated HTML/JSON assessment reports
├── src/flow_graph_vapt/
│   ├── analyzer.py       # Differential Response Analyzer
│   ├── classifier.py     # Unsupervised Entity Type Classifier
│   ├── crawler.py        # Playwright SPA Crawler
│   ├── extractor.py      # Heuristic Identifier Extractor
│   ├── graph.py          # NetworkX Directed Flow Graph
│   ├── inventory.py      # Dual-Persona Identifier Inventory
│   ├── main.py           # CLI & API Server Entrypoint
│   ├── models.py         # Pydantic Schemas
│   ├── orchestrator.py   # Scanner Pipeline Manager
│   ├── proxy.py          # mitmproxy Ingestion Hook
│   ├── replay.py         # Stateful Replay Mutation Engine
│   └── reporter.py       # Executive Report Generator
├── tests/                # Test Suite
├── pyproject.toml        # Package Metadata
├── README.md
└── LICENSE
```

---

## License

Distributed under the [MIT License](LICENSE).

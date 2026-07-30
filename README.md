# 🛡️ Flow-Graph VAPT: Enterprise Automated BOLA / IDOR Detection Framework

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.12+](https://img.shields.io/badge/python-3.12%2B-blue.svg)](https://www.python.org/downloads/)
[![Tests](https://img.shields.io/badge/tests-passing-brightgreen.svg)]()
[![OWASP API1:2023](https://img.shields.io/badge/OWASP-API1%3A2023-red.svg)](https://owasp.org/API-Security/editions/2023/en/0xa1-broken-object-level-authorization/)

**Flow-Graph VAPT** is a modular, scalable cybersecurity framework written in Python 3.12+ designed to automate the discovery, graph-based flow mapping, and differential verification of **Broken Object Level Authorization (BOLA / IDOR)** vulnerabilities in modern Single Page Applications (SPAs) and REST APIs.

---

## 🌟 Key Features

- **Directed Application Flow Graph ($G = (V, E)$)**: Maps endpoints, inferred entity types, and request dependencies using NetworkX.
- **Multi-Vector Identifier Extraction Engine**: Detects candidate IDs across URL paths, query parameters, JSON payloads, and HTML links using weighted heuristic confidence scoring.
- **Unsupervised Object Classification**: Groups parameters into entity classes (e.g., `User`, `Order`, `Basket`, `Vehicle`) using URL path stemming and JSON structural response key clustering (Jaccard similarity).
- **Dual-Persona Identifier Inventory**: Stores valid identifiers captured across distinct user sessions (`User_A` Attacker vs. `User_B` Victim).
- **Hybrid Ingestion Pipeline**: Combines passive interception via `mitmproxy`/`mitmweb` with active headless browser crawling via `Playwright`.
- **Stateful Replay Engine**: Mutates requests using `httpx` while preserving authentication headers, anti-CSRF tokens, cookies, and deep JSON body structures.
- **Differential Response Analyzer**: Evaluates baseline vs. mutated responses using a multi-vector matrix (Status codes, error payload absence, structural similarity $\ge 0.75$, sensitive data exposure, and content length ratio).
- **Multi-Format Executive Reporting**: Produces structured JSON, Markdown, and Jinja2-rendered executive HTML reports mapped to OWASP API1:2023 and CWE-639.

---

## 🏗️ Architecture Overview

```text
  [ Live Browser Traffic ]           [ Active Crawler ]
             │                               │
             ▼                               ▼
     1. Interception Hook           2. Playwright Discovery
        (proxy.py)                       (crawler.py)
             │                               │
             └───────────────┬───────────────┘
                             │
                             ▼
              3. Hybrid Ingestion Pipeline
                     (orchestrator.py)
                             │
                             ▼
             4. Identifier Extraction Engine
                       (extractor.py)
                             │
                             ▼
            5. Object Type Classification Engine
                      (classifier.py)
                             │
                             ▼
        6. Object Inventory       7. Application Flow Graph
            (inventory.py)             (graph.py)
                             │
                             ▼
              8. Stateful Replay Mutation Engine
                        (replay.py)
                             │
                             ▼
             9. Differential Response Analyzer
                       (analyzer.py)
                             │
                             ▼
            10. Multi-Format Report Generator
                       (reporter.py)
                             │
                             ▼
            [ reports/bola_report.html ]
```

---

## 🚀 Installation

### Prerequisites
- Python 3.10+
- `mitmproxy` / `mitmweb`
- Docker (for target benchmarks like OWASP Juice Shop, crAPI, VAmPI)

### Setup Instructions

```bash
# 1. Clone the repository
git clone https://github.com/kailasshankarpr/flow-graph-vapt.git
cd flow-graph-vapt

# 2. Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows PowerShell: .\venv\Scripts\Activate.ps1

# 3. Install package and dependencies
pip install -e .[dev]

# 4. Install Playwright browser dependencies
python3 -m playwright install chromium
```

---

## 💻 Usage Walkthrough

### Step 1: Start `mitmweb` Proxy Interception

Launch `mitmweb` with the `proxy.py` script attached to capture live browser traffic:

```bash
mitmweb -s src/flow_graph_vapt/proxy.py --listen-port 8081 --web-port 8085
```
- Proxy Listening Port: `8081`
- Web Interface: `http://127.0.0.1:8085`

### Step 2: Browse the Target Application

Configure your browser (e.g., Firefox with FoxyProxy set to HTTP Proxy `127.0.0.1:8081`):

1. **Victim Session (`User_B`)**: Log into the target application as User B, view private resources (baskets, orders, vehicles, profiles), then log out.
2. **Attacker Session (`User_A`)**: Log into the target application as User A, view resources, then log out.

`proxy.py` automatically isolates authenticated JWT sessions into `captured_traffic/user_b_traffic.json` and `user_a_traffic.json`.

### Step 3: Run Automated BOLA Assessment

Run the analyzer against your target base URL:

```bash
python3 -m flow_graph_vapt.main analyze --target http://localhost:3000
```

#### Clean Output Mode (Recommended for Testers)
To silence verbose debug logs and display only high-confidence BOLA findings and summary tables:

```bash
LOGURU_LEVEL=WARNING python3 -m flow_graph_vapt.main analyze --target http://localhost:3000
```

---

## 📊 Viewing Assessment Reports

After scan completion, open the Jinja2-rendered Executive HTML report in your browser:

```bash
firefox reports/bola_report.html
```

The report provides:
- **Executive Vulnerability Dashboard** (Scored $0.0 - 1.0$)
- **OWASP API1:2023 & CWE-639 Mapping**
- **Side-by-Side Baseline vs. Mutated Request/Response Diffs**
- **Developer Remediation Guidance**



---

## 🧪 Test Suite

Run unit and integration tests with coverage reporting:

```bash
pytest --cov=flow_graph_vapt tests/
```

---

## 📜 Project Structure

```text
flow_graph_vapt/
├── captured_traffic/        # Auto-saved captured proxy traffic JSONs
├── reports/                 # Output directory for HTML, JSON, and MD reports
├── src/flow_graph_vapt/
│   ├── analyzer.py          # Differential Response Analyzer
│   ├── classifier.py        # Unsupervised Object Type Classifier
│   ├── config.py            # Global Settings
│   ├── crawler.py           # Playwright Authenticated Crawler
│   ├── exceptions.py        # Custom Exception Hierarchy
│   ├── extractor.py         # Multi-Vector Identifier Extractor
│   ├── graph.py             # NetworkX Application Flow Graph
│   ├── inventory.py         # Dual-Persona Object Inventory
│   ├── main.py              # CLI & REST Server Entrypoint
│   ├── models.py            # Pydantic v2 Models
│   ├── orchestrator.py      # Master Scanner Pipeline
│   ├── proxy.py             # mitmproxy Ingestion Addon
│   ├── replay.py            # Stateful Replay Mutation Engine
│   └── reporter.py          # Report Generator (Jinja2)
├── tests/                   # Pytest Test Suite
├── pyproject.toml           # Package Metadata & Dependencies
├── README.md                # Project Documentation
└── LICENSE                  # MIT License
```

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

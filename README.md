# Flow-Graph VAPT

**Automated BOLA / IDOR Vulnerability Detection Engine**

[![CI](https://github.com/kailasshankarpr/flow-graph-vapt/actions/workflows/ci.yml/badge.svg)](https://github.com/kailasshankarpr/flow-graph-vapt/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![Coverage](https://img.shields.io/badge/coverage-68%25-green.svg)]()

Flow-Graph VAPT is a Python tool that detects **Broken Object Level Authorization (BOLA / IDOR)** vulnerabilities in REST APIs and Single Page Applications (SPAs) using NetworkX flow graphs and differential response analysis.

---

## ⚠️ Authorized Use Disclaimer

> **IMPORTANT**: This tool is designed strictly for authorized security testing, academic research, and defensive evaluation. Use this tool only on systems you own or have explicit, written permission to test. Unauthorized security testing is illegal.

---

## Why Flow-Graph VAPT?

Traditional DAST scanners (such as OWASP ZAP or Nikto) frequently miss BOLA vulnerabilities because BOLA is an authorization logic flaw rather than a syntax error. When an attacker requests another user's object ID, the server returns a valid `HTTP 200 OK` response with well-formed JSON syntax. 

Flow-Graph VAPT addresses this by:
1. Intercepting dual-session authenticated traffic (`User_A` Attacker vs. `User_B` Victim).
2. Constructing a directed application flow graph ($G = (V, E)$) linking endpoints to extracted entity types.
3. Automatically mutating object parameters while preserving the attacker's authorization context.
4. Performing multi-vector differential analysis to confirm data exposure.

---

## 📊 Benchmark Validation & Results

The scanner logic was evaluated across two vulnerable target environments: **OWASP Juice Shop** and **OWASP crAPI**.

| Target Benchmark | Architecture | Candidates Detected | False Positives Filtered | Confirmed BOLA Flaws | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **OWASP Juice Shop** | Node.js / Angular SPA (`:3000`) | 4 | **2** (Own-object & Session-scoped) | **2** | ✅ Verified |
| **OWASP crAPI** | Microservices REST API (`:8888`) | 1 | 0 | **1** | ✅ Verified |

### Confirmed Vulnerabilities Identified:
- **OWASP Juice Shop**:
  - `GET /rest/basket/6` — Basket BOLA (User A accessed User B's shopping cart)
  - `GET /api/BasketItems/11` — Basket Items BOLA (Cross-tenant modification/view of cart items)
- **OWASP crAPI**:
  - `GET /identity/api/v2/vehicle/{vehicle_id}/location` — Vehicle GPS Location BOLA

### False Positive Analysis & Elimination:
During initial test runs, 2 raw candidates were flagged on Juice Shop:
1. `GET /rest/basket/7`: The attacker persona (`User_A`) accessed basket 7 in their own session. Replaying User A's token against basket 7 is legitimate own-object access. **Fixed by**: `ObjectInventory.get_alternative_identifiers()` which explicitly excludes object IDs belonging to the requesting persona.
2. `GET /rest/user/whoami`: Takes no target object ID parameter and returns whichever user owns the session token. **Fixed by**: `DifferentialResponseAnalyzer.is_public_or_session_scoped_endpoint()` which filters out session-scoped endpoints (`/whoami`, `/me`).

### Automated Test Coverage
- **Unit & Integration Test Suite**: 68% statement coverage (`pytest --cov=flow_graph_vapt tests/`).

---

## 🔬 Detection Logic & False Positive Reduction

A potential BOLA finding is evaluated against a 5-vector comparison matrix to calculate a BOLA Confidence Score ($0.0 - 1.0$):

1. **HTTP Status Code Check**: Evaluates `200/201/206 OK` vs expected `401/403/404` enforcement.
2. **Error Payload Absence**: Scans response bodies for soft-error keys (`"unauthorized"`, `"forbidden"`, `"denied"`, `"invalid_permission"`). Soft-error detection applies a score penalty (-0.35).
3. **Structural JSON Key Similarity (Jaccard Index $\ge 0.75$)**: Compares key sets of baseline ($B$) and mutated ($M$) responses:
   $$J(B, M) = \frac{|B \cap M|}{|B \cup M|}$$
   If key structures match ($\ge 0.75$), the response is confirmed to return actual object data rather than a generic error schema.
4. **Sensitive Data Check**: Scans for fields like `email`, `ssn`, `phone`, `balance`, `address`, `credit_card`.
5. **Content Length Ratio**: Verifies payload size consistency ($0.70 \le \text{ratio} \le 1.30$).

---

## 🛠️ Reproducible Benchmark Target Setup

To reproduce the benchmark scan locally against OWASP Juice Shop:

### 1. Launch Target Application
```bash
docker run -d -p 3000:3000 bkimminich/juice-shop:v15.3.0
```

### 2. Capture Dual Sessions with `mitmweb`
Launch proxy interception hook:
```bash
mitmweb -s src/flow_graph_vapt/proxy.py --listen-port 8081 --web-port 8085
```

Configure browser proxy (`127.0.0.1:8081`):
1. **User B (Victim)**: Log into Juice Shop with lab account `admin@juice-sh.op` / `admin123` *(intentionally vulnerable lab application; local use only)*, view basket `/rest/basket/6`, then log out.
2. **User A (Attacker)**: Log into Juice Shop with lab account `user2@juice-sh.op` / `user2123`, view basket `/rest/basket/7`, then log out.

### 3. Execute Assessment
```bash
LOGURU_LEVEL=WARNING python3 -m flow_graph_vapt.main analyze --target http://localhost:3000
```

---

## 🚀 Installation & Setup

### Prerequisites
- Python 3.10+
- `mitmproxy` / `mitmweb`
- Docker (optional)

### Installation
```bash
git clone https://github.com/kailasshankarpr/flow-graph-vapt.git
cd flow-graph-vapt

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # Windows PowerShell: .\venv\Scripts\Activate.ps1

# Install package dependencies
pip install -e .[dev]

# Install Playwright chromium browser
python3 -m playwright install chromium
```

---

## 💻 Usage via Makefile or Docker

### Local Commands (Makefile)
```bash
make install       # Install package and browser dependencies
make test          # Run pytest suite with coverage report
make lint          # Run ruff, mypy, and black checks
make run           # Run scanner on target
```

### Containerized Execution (Docker)
```bash
# Build Docker image
docker build -t flow-graph-vapt:latest .

# Launch FastAPI REST API Management Server & Scanner Service on port 8000
docker run --rm -p 8000:8000 flow-graph-vapt:latest
```

---

## ⚠️ Technical Limitations

1. **Dual-Session Dependency**: Requires active captured traffic from two distinct authenticated sessions (`User_A` and `User_B`).
2. **Static Token Lifetimes**: Does not automatically re-authenticate if session tokens/JWTs expire during long offline replay runs.
3. **Heuristic Thresholding**: The Jaccard similarity threshold ($\ge 0.75$) and confidence scores ($\ge 0.55$) are empirical heuristics tuned for JSON APIs and may require adjustment for custom non-standard data formats.
4. **Scope Boundaries**: Focuses specifically on Broken Object Level Authorization (OWASP API1:2023); does not test for Broken Function Level Authorization (BFLA) or Mass Assignment out-of-the-box.

---

## 📜 Project Structure

```text
flow_graph_vapt/
├── .github/
│   └── workflows/
│       └── ci.yml             # GitHub Actions CI workflow
├── captured_traffic/          # Intercepted proxy session JSONs (gitignored)
├── reports/                   # Output directory for HTML/JSON reports (gitignored)
├── src/flow_graph_vapt/
│   ├── analyzer.py            # Differential Response Analyzer & FP Filters
│   ├── classifier.py          # Heuristic Schema Classifier
│   ├── config.py              # System Settings
│   ├── crawler.py             # Playwright SPA Crawler
│   ├── exceptions.py          # Custom Exception Classes
│   ├── extractor.py           # Weighted Identifier Extractor
│   ├── graph.py               # NetworkX Directed Flow Graph
│   ├── inventory.py           # Dual-Persona Identifier Repository
│   ├── main.py                # CLI & API Server Entrypoint
│   ├── models.py              # Pydantic v2 Models
│   ├── orchestrator.py        # Scanner Pipeline Manager
│   ├── proxy.py               # mitmproxy Ingestion Hook
│   ├── replay.py              # Stateful Replay Mutation Engine
│   ├── reporter.py            # Executive Report Generator
│   ├── state.py               # Request Throttling & Session State Manager
│   └── validator.py           # Target Scope Validator
├── tests/                     # Pytest Test Suite
├── Dockerfile                 # Container Build Configuration
├── Makefile                   # Developer Task Automation
├── pyproject.toml             # Package Metadata & Dependencies
├── README.md                  # Project Documentation
└── LICENSE                    # MIT License
```

---

## 📄 License

Distributed under the [MIT License](LICENSE).

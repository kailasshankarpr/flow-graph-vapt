"""
Multi-Format Reporting Generator.
Exports confirmed BOLA vulnerability findings into JSON, Markdown, and Jinja2-rendered HTML executive reports.
"""

import json
from datetime import datetime
from pathlib import Path
from typing import List
from jinja2 import Template
from loguru import logger
from flow_graph_vapt.models import BOLAFinding


HTML_REPORT_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Flow-Graph VAPT - BOLA Assessment Report</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #0f172a; color: #f8fafc; margin: 0; padding: 20px; }
        .container { max-width: 1200px; margin: 0 auto; }
        .header { border-bottom: 2px solid #38bdf8; padding-bottom: 10px; margin-bottom: 30px; }
        .card { background-color: #1e293b; border-radius: 8px; padding: 20px; margin-bottom: 20px; border: 1px solid #334155; }
        .badge { padding: 4px 12px; border-radius: 4px; font-weight: bold; font-size: 0.85em; }
        .badge-critical { background-color: #ef4444; color: white; }
        .badge-high { background-color: #f97316; color: white; }
        code { background-color: #0f172a; padding: 2px 6px; border-radius: 4px; color: #38bdf8; }
        pre { background-color: #0f172a; padding: 15px; border-radius: 6px; overflow-x: auto; color: #e2e8f0; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Flow-Graph VAPT: Vulnerability Assessment Report</h1>
            <p>Target: Automated BOLA / IDOR Security Audit | Generated: {{ generated_at }}</p>
        </div>
        
        <h2>Executive Summary</h2>
        <div class="card">
            <p>Total BOLA Findings Confirmed: <strong>{{ findings|length }}</strong></p>
        </div>

        <h2>Detailed Vulnerability Findings</h2>
        {% for f in findings %}
        <div class="card">
            <h3>
                <span class="badge badge-{{ f.severity.lower() }}">{{ f.severity }}</span>
                {{ f.http_method }} {{ f.target_url }}
            </h3>
            <p><strong>CWE:</strong> {{ f.cwe_id }} | <strong>OWASP:</strong> {{ f.owasp_category }}</p>
            <p><strong>Vulnerable Parameter:</strong> <code>{{ f.vulnerable_parameter }}</code> (Location: {{ f.parameter_location }})</p>
            <p><strong>Inferred Entity Type:</strong> <code>{{ f.inferred_entity_type }}</code></p>
            <p><strong>BOLA Confidence Score:</strong> {{ f.confidence_score }}</p>
            
            <h4>Attack Vector Proof of Concept</h4>
            <p>Original ID (User A): <code>{{ f.original_value_user_a }}</code></p>
            <p>Substituted ID (User B): <code>{{ f.substituted_value_user_b }}</code></p>
            
            <h4>Evidence Details</h4>
            <pre>{{ f.evidence_details | tojson(indent=2) }}</pre>

            <h4>Remediation Guidance</h4>
            <p>{{ f.remediation_guidance }}</p>
        </div>
        {% endfor %}
    </div>
</body>
</html>
"""


class ReportGenerator:
    """Exports assessment reports in multiple formats."""

    def __init__(self, output_dir: str = "./reports") -> None:
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def export_json(self, findings: List[BOLAFinding], filename: str = "bola_report.json") -> Path:
        """Exports findings to structured JSON."""
        file_path = self.output_dir / filename
        data = [f.model_dump(mode="json") for f in findings]
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        logger.info(f"JSON Report exported to: {file_path.resolve()}")
        return file_path

    def export_markdown(self, findings: List[BOLAFinding], filename: str = "bola_report.md") -> Path:
        """Exports findings to Markdown format."""
        file_path = self.output_dir / filename
        lines = [
            "# Flow-Graph VAPT: BOLA Vulnerability Report\n",
            f"**Generated At:** {datetime.utcnow().isoformat()}\n",
            f"**Total Findings:** {len(findings)}\n",
            "---\n"
        ]
        for f in findings:
            lines.extend([
                f"## [{f.severity}] {f.http_method} {f.target_url}\n",
                f"- **Vulnerable Parameter:** `{f.vulnerable_parameter}` ({f.parameter_location})\n",
                f"- **Inferred Entity:** `{f.inferred_entity_type}`\n",
                f"- **Confidence Score:** `{f.confidence_score}`\n",
                f"- **Substitution:** `{f.original_value_user_a}` -> `{f.substituted_value_user_b}`\n",
                "### Remediation Guidance\n",
                f"{f.remediation_guidance}\n\n",
                "---\n"
            ])
        with open(file_path, "w", encoding="utf-8") as f:
            f.writelines(lines)
        logger.info(f"Markdown Report exported to: {file_path.resolve()}")
        return file_path

    def export_html(self, findings: List[BOLAFinding], filename: str = "bola_report.html") -> Path:
        """Exports findings to HTML report using Jinja2."""
        file_path = self.output_dir / filename
        template = Template(HTML_REPORT_TEMPLATE)
        rendered_html = template.render(
            findings=findings,
            generated_at=datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
        )
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(rendered_html)
        logger.info(f"HTML Executive Report exported to: {file_path.resolve()}")
        return file_path

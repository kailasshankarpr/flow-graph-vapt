"""
CLI Application & REST Server Entrypoint for Flow-Graph VAPT.
Provides CLI commands for:
  1. 'demo': Run demonstration synthetic scan
  2. 'analyze': Ingest captured live browser proxy traffic and run automated BOLA assessment!
"""

import asyncio
from pathlib import Path
import typer
from fastapi import FastAPI
from loguru import logger
from rich.console import Console

from flow_graph_vapt.config import settings
from flow_graph_vapt.models import HTTPInteraction, HTTPMethod, HTTPRequestModel, HTTPResponseModel
from flow_graph_vapt.orchestrator import FlowGraphVAPTPipeline
from flow_graph_vapt.proxy import load_captured_traffic

cli_app = typer.Typer(name="Flow-Graph VAPT", help="Enterprise Automated BOLA Detection Engine")
console = Console()

api_server = FastAPI(
    title="Flow-Graph VAPT API",
    version=settings.VERSION,
    description="REST management interface for triggering and inspecting BOLA security assessments."
)


@api_server.get("/health")
def health_check():
    return {"status": "online", "version": settings.VERSION}


@cli_app.callback()
def callback():
    """Flow-Graph VAPT - Enterprise Automated BOLA Security Scanner"""
    pass


@cli_app.command("analyze")
def analyze_captured_traffic(
    target: str = typer.Option("http://localhost:8000", "--target", "-t", help="Target Base URL"),
    output: str = typer.Option("./reports", "--output", "-o", help="Report Output Directory")
):
    """
    Ingests live browser traffic captured via mitmproxy during manual enumeration/browsing,
    extracts object identifiers, builds the Flow Graph, and runs automated BOLA mutation testing!
    """
    console.print(f"[bold green]Ingesting captured browser traffic for BOLA Assessment...[/bold green]")

    user_a_interactions = load_captured_traffic("User_A")
    user_b_interactions = load_captured_traffic("User_B")

    if not user_a_interactions and not user_b_interactions:
        console.print("[bold red]No captured traffic found in ./captured_traffic directory.[/bold red]")
        console.print("Please browse your target application via mitmproxy first to capture traffic.")
        return

    console.print(f"Loaded [cyan]{len(user_a_interactions)}[/cyan] User_A (Attacker) interactions and [cyan]{len(user_b_interactions)}[/cyan] User_B (Victim) interactions.")

    # Extract User_A authorization headers automatically from first captured request
    user_a_headers = {}
    if user_a_interactions:
        auth_header = user_a_interactions[0].request.headers.get("authorization") or user_a_interactions[0].request.headers.get("Authorization")
        if auth_header:
            user_a_headers["Authorization"] = auth_header

    pipeline = FlowGraphVAPTPipeline(target_base_url=target, output_dir=output)

    findings = asyncio.run(pipeline.run_hybrid_assessment(
        user_a_interactions=user_a_interactions,
        user_b_interactions=user_b_interactions,
        user_a_auth_headers=user_a_headers,
        enable_active_crawler=True
    ))


    console.print(f"\n[bold yellow]Automated Scan Completed. Confirmed BOLA Vulnerabilities:[/bold yellow] {len(findings)}")
    for f in findings:
        console.print(f"[bold red][+] [CONFIRMED BOLA][/bold red] {f.http_method} {f.target_url} (Param: {f.vulnerable_parameter})")


@cli_app.command("scan")
def scan(
    target: str = typer.Option("http://localhost:8000", "--target", "-t", help="Target Base URL"),
    output: str = typer.Option("./reports", "--output", "-o", help="Report Output Directory")
):
    """Executes a demonstration BOLA security scan against a target API."""
    console.print(f"[bold green]Starting Flow-Graph VAPT Demo Scan on target:[/bold green] {target}")

    user_b_interaction = HTTPInteraction(
        interaction_id="b_1",
        session_id="User_B",
        request=HTTPRequestModel(
            url=f"{target}/api/v1/orders/101",
            method=HTTPMethod.GET,
            headers={"Authorization": "Bearer victim_token_b"}
        ),
        response=HTTPResponseModel(
            status_code=200,
            headers={"Content-Type": "application/json"},
            body='{"order_id": 101, "item": "Laptop", "total": 1200, "user_id": "usr_victim"}',
            json_data={"order_id": 101, "item": "Laptop", "total": 1200, "user_id": "usr_victim"},
            content_length=75
        )
    )

    user_a_interaction = HTTPInteraction(
        interaction_id="a_1",
        session_id="User_A",
        request=HTTPRequestModel(
            url=f"{target}/api/v1/orders/55",
            method=HTTPMethod.GET,
            headers={"Authorization": "Bearer attacker_token_a"}
        ),
        response=HTTPResponseModel(
            status_code=200,
            headers={"Content-Type": "application/json"},
            body='{"order_id": 55, "item": "Mouse", "total": 25, "user_id": "usr_attacker"}',
            json_data={"order_id": 55, "item": "Mouse", "total": 25, "user_id": "usr_attacker"},
            content_length=70
        )
    )

    pipeline = FlowGraphVAPTPipeline(target_base_url=target, output_dir=output)

    findings = asyncio.run(pipeline.run_full_assessment(
        user_a_interactions=[user_a_interaction],
        user_b_interactions=[user_b_interaction],
        user_a_auth_headers={"Authorization": "Bearer attacker_token_a"}
    ))

    console.print(f"\n[bold yellow]Scan Completed. Confirmed BOLA Vulnerabilities:[/bold yellow] {len(findings)}")
    for f in findings:
        console.print(f"[bold red][+] [CONFIRMED BOLA][/bold red] {f.http_method} {f.target_url} (Param: {f.vulnerable_parameter})")


if __name__ == "__main__":
    cli_app()

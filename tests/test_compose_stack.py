"""Integration checks for the local Docker Compose platform."""

from __future__ import annotations

import json
import os
import subprocess
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import urlopen

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
EXPECTED_SERVICES = {"postgres", "adminer", "ollama", "open-webui", "n8n"}


def compose(*arguments: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["docker", "compose", *arguments],
        cwd=PROJECT_ROOT,
        check=True,
        capture_output=True,
        text=True,
    )


@pytest.fixture(scope="module")
def compose_config() -> dict:
    return json.loads(compose("config", "--format", "json").stdout)


@pytest.fixture(scope="module")
def running_services() -> dict[str, dict]:
    output = compose("ps", "--format", "json").stdout
    services = [json.loads(line) for line in output.splitlines() if line.strip()]
    return {service["Service"]: service for service in services}


def published_port(config: dict, service_name: str) -> int:
    ports = config["services"][service_name]["ports"]
    assert ports, f"{service_name} must publish a local port"
    return int(ports[0]["published"])


def get_status(url: str) -> int:
    try:
        with urlopen(url, timeout=10) as response:  # nosec B310 - local test endpoints
            return response.status
    except HTTPError as error:
        return error.code
    except URLError as error:
        pytest.fail(f"Could not reach {url}: {error.reason}")


def test_compose_declares_the_core_services(compose_config: dict) -> None:
    services = compose_config["services"]
    assert set(services) == EXPECTED_SERVICES
    assert services["adminer"]["depends_on"]["postgres"]["condition"] == "service_healthy"
    assert services["n8n"]["depends_on"]["postgres"]["condition"] == "service_healthy"
    assert services["open-webui"]["depends_on"]["ollama"]["condition"] == "service_healthy"


@pytest.mark.integration
def test_all_compose_services_are_running(running_services: dict[str, dict]) -> None:
    missing = EXPECTED_SERVICES - set(running_services)
    assert not missing, f"Compose did not create: {sorted(missing)}"
    stopped = {
        name: service["State"]
        for name, service in running_services.items()
        if name in EXPECTED_SERVICES and service["State"] != "running"
    }
    assert not stopped, f"Services not running: {stopped}"


@pytest.mark.integration
def test_healthchecked_services_are_healthy(running_services: dict[str, dict]) -> None:
    for service_name in ("postgres", "ollama", "open-webui"):
        assert running_services[service_name]["Health"] == "healthy"


@pytest.mark.integration
def test_postgres_accepts_connections() -> None:
    database = os.getenv("POSTGRES_DB", "creative_ai_lab")
    user = os.getenv("POSTGRES_USER", "creative_ai")
    result = compose("exec", "-T", "postgres", "pg_isready", "-U", user, "-d", database)
    assert "accepting connections" in result.stdout


@pytest.mark.integration
def test_local_http_services_respond(compose_config: dict) -> None:
    endpoints = {"adminer": "/", "ollama": "/api/tags", "open-webui": "/", "n8n": "/healthz"}
    for service_name, path in endpoints.items():
        port = published_port(compose_config, service_name)
        status = get_status(f"http://127.0.0.1:{port}{path}")
        assert status < 500, f"{service_name} returned HTTP {status}"
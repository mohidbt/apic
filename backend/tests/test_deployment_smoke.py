"""
Smoke tests for the remote deployment at api-ingest.com (or any URL).

Skipped by default. Enable by setting the TEST_REMOTE_URL env var:

    TEST_REMOTE_URL=https://api-ingest.com pytest tests/test_deployment_smoke.py -v
"""

import os
import socket

import pytest

REMOTE_URL = os.getenv("TEST_REMOTE_URL", "").rstrip("/")

pytestmark = pytest.mark.skipif(not REMOTE_URL, reason="TEST_REMOTE_URL not set")


@pytest.fixture(scope="module")
def http():
    import httpx
    with httpx.Client(base_url=REMOTE_URL, timeout=15.0) as c:
        yield c


class TestDeploymentSmoke:
    def test_health(self, http):
        r = http.get("/health")
        assert r.status_code == 200
        assert r.json()["status"] == "healthy"

    def test_api_info(self, http):
        r = http.get("/api")
        assert r.status_code == 200
        body = r.json()
        assert body.get("status") == "ok"

    def test_auth_me_returns_401_not_500(self, http):
        r = http.get("/api/auth/me")
        assert r.status_code == 401, f"Expected 401, got {r.status_code}: {r.text}"

    def test_specs_list(self, http):
        r = http.get("/api/specs")
        assert r.status_code == 200
        body = r.json()
        assert "specs" in body
        assert isinstance(body["specs"], list)

    def test_mcp_port_reachable(self):
        """Check whether port 8080 is externally reachable on the remote host."""
        from urllib.parse import urlparse
        parsed = urlparse(REMOTE_URL)
        host = parsed.hostname
        try:
            sock = socket.create_connection((host, 8080), timeout=5)
            sock.close()
            reachable = True
        except (OSError, socket.timeout):
            reachable = False

        if not reachable:
            pytest.skip(
                f"MCP port 8080 not reachable on {host}. "
                "Koyeb may only expose port 8000. "
                "Consider adding a reverse-proxy rule for /mcp."
            )

"""
Tests for the auth + token system (FastAPI backend) and the MCP server
(bearer-token middleware, resources, tools).

Uses an isolated in-memory SQLite database so no external services are needed.

Run:  cd backend && pytest tests/test_auth_and_mcp.py -v
"""

import hashlib
import os
import secrets
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

# Ensure backend package is importable
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

# Point database to in-memory SQLite before any model imports
os.environ.pop("DATABASE_URL", None)
os.environ["DATABASE_PATH"] = ":memory:"
os.environ["ADMIN_GITHUB_LOGINS"] = "admin-user"
os.environ["ADMIN_EMAILS"] = "admin@example.com"

import jwt as pyjwt
import pytest
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from models.database import Base

# Build an isolated in-memory engine and session factory for tests
_test_engine = create_engine(
    "sqlite:///:memory:",
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
_TestSession = sessionmaker(autocommit=False, autoflush=False, bind=_test_engine)

# Patch the module-level engine and SessionLocal so that all production code
# (main.py, mcp_server.py) uses our in-memory DB.
import models.database as _dbmod

_dbmod.engine = _test_engine
_dbmod.SessionLocal = _TestSession
_dbmod.IS_SQLITE = True

from models.user import User, ApiToken  # noqa: E402
from models.api_spec import ApiSpec, Tag  # noqa: E402

# Create tables
Base.metadata.create_all(bind=_test_engine)

# Now import the FastAPI app (after DB is patched)
from main import app, SESSION_SECRET, SESSION_MAX_AGE  # noqa: E402

from fastapi.testclient import TestClient


# ── Helpers ───────────────────────────────────────────────────────────

def _make_user(db, github_id=9999, login="testuser"):
    user = db.query(User).filter(User.github_id == github_id).first()
    if user:
        return user
    user = User(github_id=github_id, github_login=login, name="Test User")
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def _mint_jwt(
    user_id: int,
    secret: str = SESSION_SECRET,
    expired: bool = False,
    gh_email: str | None = None,
):
    delta = timedelta(seconds=-10) if expired else timedelta(seconds=SESSION_MAX_AGE)
    payload = {"sub": str(user_id), "exp": datetime.now(timezone.utc) + delta}
    if gh_email:
        payload["gh_email"] = gh_email
    return pyjwt.encode(payload, secret, algorithm="HS256")


def _create_db_token(db, user_id: int, label: str = "test-token"):
    raw = f"apii_{secrets.token_urlsafe(32)}"
    token_hash = hashlib.sha256(raw.encode()).hexdigest()
    t = ApiToken(user_id=user_id, token_hash=token_hash, label=label)
    db.add(t)
    db.commit()
    db.refresh(t)
    return raw, t


# ── Fixtures ──────────────────────────────────────────────────────────

@pytest.fixture(autouse=True)
def _clean_tables():
    """Wipe all rows between tests while keeping tables."""
    yield
    db = _TestSession()
    try:
        db.query(ApiToken).delete()
        db.query(User).delete()
        db.query(ApiSpec).delete()
        db.commit()
    finally:
        db.close()


def _override_get_db():
    db = _TestSession()
    try:
        yield db
    finally:
        db.close()


from models.database import get_db  # noqa: E402
app.dependency_overrides[get_db] = _override_get_db

client = TestClient(app, raise_server_exceptions=False)


# ======================================================================
# Part 1: Backend Auth API
# ======================================================================

class TestAuthAPI:
    def test_auth_me_no_session(self):
        r = client.get("/api/auth/me")
        assert r.status_code == 401

    def test_auth_me_tampered_jwt(self):
        db = _TestSession()
        user = _make_user(db)
        token = _mint_jwt(user.id)
        db.close()
        tampered = token[:-3] + "xxx"
        r = client.get("/api/auth/me", cookies={"session": tampered})
        assert r.status_code == 401

    def test_auth_me_expired_jwt(self):
        db = _TestSession()
        user = _make_user(db)
        token = _mint_jwt(user.id, expired=True)
        db.close()
        r = client.get("/api/auth/me", cookies={"session": token})
        assert r.status_code == 401

    def test_auth_me_valid_jwt(self):
        db = _TestSession()
        user = _make_user(db)
        token = _mint_jwt(user.id)
        db.close()
        r = client.get("/api/auth/me", cookies={"session": token})
        assert r.status_code == 200
        data = r.json()
        assert data["user"]["github_login"] == "testuser"
        assert data["user"]["id"] == user.id
        assert data["user"]["is_admin"] is False

    def test_auth_me_admin_by_login(self):
        db = _TestSession()
        user = _make_user(db, github_id=7777, login="admin-user")
        token = _mint_jwt(user.id)
        db.close()
        r = client.get("/api/auth/me", cookies={"session": token})
        assert r.status_code == 200
        assert r.json()["user"]["is_admin"] is True

    def test_auth_me_admin_by_email_claim(self):
        db = _TestSession()
        user = _make_user(db, github_id=7778, login="someuser")
        token = _mint_jwt(user.id, gh_email="admin@example.com")
        db.close()
        r = client.get("/api/auth/me", cookies={"session": token})
        assert r.status_code == 200
        assert r.json()["user"]["is_admin"] is True

    def test_auth_github_missing_code(self):
        r = client.post("/api/auth/github", json={})
        assert r.status_code == 400
        assert "Missing code" in r.json()["detail"]

    def test_auth_github_no_config(self):
        old_id = os.environ.get("GITHUB_CLIENT_ID")
        old_secret = os.environ.get("GITHUB_CLIENT_SECRET")
        os.environ["GITHUB_CLIENT_ID"] = ""
        os.environ["GITHUB_CLIENT_SECRET"] = ""
        # Re-import won't help since main.py reads at import time.
        # The module-level vars are already set. We patch them directly.
        import main
        orig_cid, orig_csec = main.GITHUB_CLIENT_ID, main.GITHUB_CLIENT_SECRET
        main.GITHUB_CLIENT_ID = ""
        main.GITHUB_CLIENT_SECRET = ""
        try:
            r = client.post("/api/auth/github", json={"code": "abc"})
            assert r.status_code == 500
            assert "not configured" in r.json()["detail"]
        finally:
            main.GITHUB_CLIENT_ID = orig_cid
            main.GITHUB_CLIENT_SECRET = orig_csec
            if old_id is not None:
                os.environ["GITHUB_CLIENT_ID"] = old_id
            if old_secret is not None:
                os.environ["GITHUB_CLIENT_SECRET"] = old_secret

    def test_logout_clears_cookie(self):
        r = client.post("/api/auth/logout")
        assert r.status_code == 200
        sc = r.headers.get("set-cookie", "")
        assert "session=" in sc
        assert 'Max-Age=0' in sc or 'max-age=0' in sc.lower()


# ======================================================================
# Part 2: Token CRUD
# ======================================================================

class TestTokenCRUD:
    def _session_cookie(self):
        db = _TestSession()
        user = _make_user(db)
        token = _mint_jwt(user.id)
        db.close()
        return {"session": token}, user

    def test_tokens_no_session(self):
        r = client.get("/api/tokens")
        assert r.status_code == 401

    def test_create_token_empty_label(self):
        cookies, _ = self._session_cookie()
        r = client.post("/api/tokens", json={"label": ""}, cookies=cookies)
        assert r.status_code == 400
        assert "Label" in r.json()["detail"]

    def test_create_token_success(self):
        cookies, _ = self._session_cookie()
        r = client.post("/api/tokens", json={"label": "My Token"}, cookies=cookies)
        assert r.status_code == 200
        data = r.json()
        assert data["token"].startswith("apii_")
        assert data["details"]["label"] == "My Token"
        assert data["details"]["is_revoked"] is False

    def test_list_tokens(self):
        cookies, _ = self._session_cookie()
        client.post("/api/tokens", json={"label": "Token A"}, cookies=cookies)
        r = client.get("/api/tokens", cookies=cookies)
        assert r.status_code == 200
        tokens = r.json()["tokens"]
        assert len(tokens) == 1
        assert tokens[0]["label"] == "Token A"
        # Raw token value must never appear in list
        assert all("apii_" not in str(t) for t in tokens)

    def test_revoke_token(self):
        cookies, _ = self._session_cookie()
        create_r = client.post("/api/tokens", json={"label": "To Revoke"}, cookies=cookies)
        token_id = create_r.json()["details"]["id"]

        r = client.delete(f"/api/tokens/{token_id}", cookies=cookies)
        assert r.status_code == 200
        assert r.json()["ok"] is True

        # Verify it's gone from list
        list_r = client.get("/api/tokens", cookies=cookies)
        assert all(t["id"] != token_id for t in list_r.json()["tokens"])

    def test_revoke_already_revoked(self):
        cookies, _ = self._session_cookie()
        create_r = client.post("/api/tokens", json={"label": "Double Revoke"}, cookies=cookies)
        token_id = create_r.json()["details"]["id"]

        client.delete(f"/api/tokens/{token_id}", cookies=cookies)
        r = client.delete(f"/api/tokens/{token_id}", cookies=cookies)
        assert r.status_code == 404

    def test_token_isolation(self):
        # User A creates a token
        db = _TestSession()
        user_a = _make_user(db, github_id=1001, login="alice")
        user_b = _make_user(db, github_id=1002, login="bob")
        jwt_a = _mint_jwt(user_a.id)
        jwt_b = _mint_jwt(user_b.id)
        db.close()

        cookies_a = {"session": jwt_a}
        cookies_b = {"session": jwt_b}

        create_r = client.post("/api/tokens", json={"label": "Alice Token"}, cookies=cookies_a)
        token_id = create_r.json()["details"]["id"]

        # Bob cannot see Alice's tokens
        list_r = client.get("/api/tokens", cookies=cookies_b)
        assert len(list_r.json()["tokens"]) == 0

        # Bob cannot revoke Alice's token
        r = client.delete(f"/api/tokens/{token_id}", cookies=cookies_b)
        assert r.status_code == 404


class TestMarketplaceAdminDelete:
    def _seed_spec(self):
        db = _TestSession()
        spec = ApiSpec(
            name="AdminDeleteAPI",
            version="1.0.0",
            original_format="yaml",
            original_content="openapi: '3.0.0'\ninfo:\n  title: AdminDeleteAPI\n  version: 1.0.0\npaths: {}\n",
            markdown_content="# AdminDeleteAPI",
        )
        db.add(spec)
        db.commit()
        db.refresh(spec)
        sid = spec.id
        db.close()
        return sid

    def test_delete_spec_requires_auth(self):
        spec_id = self._seed_spec()
        r = client.delete(f"/api/specs/{spec_id}")
        assert r.status_code == 401

    def test_delete_spec_forbidden_for_non_admin(self):
        db = _TestSession()
        user = _make_user(db, github_id=2001, login="alice")
        token = _mint_jwt(user.id)
        db.close()
        spec_id = self._seed_spec()
        r = client.delete(f"/api/specs/{spec_id}", cookies={"session": token})
        assert r.status_code == 403

    def test_delete_spec_allowed_for_admin_login(self):
        db = _TestSession()
        user = _make_user(db, github_id=2002, login="admin-user")
        token = _mint_jwt(user.id)
        db.close()
        spec_id = self._seed_spec()
        r = client.delete(f"/api/specs/{spec_id}", cookies={"session": token})
        assert r.status_code == 200
        assert r.json()["id"] == spec_id

    def test_delete_spec_allowed_for_admin_email(self):
        db = _TestSession()
        user = _make_user(db, github_id=2003, login="another-user")
        token = _mint_jwt(user.id, gh_email="admin@example.com")
        db.close()
        spec_id = self._seed_spec()
        r = client.delete(f"/api/specs/{spec_id}", cookies={"session": token})
        assert r.status_code == 200
        assert r.json()["id"] == spec_id


# ======================================================================
# Part 3: MCP Server Auth
# ======================================================================

class TestMCPAuth:
    """Test the MCP bearer-token validation function directly."""

    def test_validate_no_match(self):
        from mcp_server import _validate_bearer_token
        assert _validate_bearer_token("random-garbage", None) is False

    def test_validate_admin_token(self):
        from mcp_server import _validate_bearer_token
        assert _validate_bearer_token("admin-secret", "admin-secret") is True
        assert _validate_bearer_token("wrong", "admin-secret") is False

    def test_validate_db_token(self):
        from mcp_server import _validate_bearer_token
        db = _TestSession()
        user = _make_user(db)
        raw, _ = _create_db_token(db, user.id)
        db.close()

        assert _validate_bearer_token(raw, None) is True

    def test_validate_revoked_db_token(self):
        from mcp_server import _validate_bearer_token
        db = _TestSession()
        user = _make_user(db)
        raw, tok = _create_db_token(db, user.id, label="will-revoke")
        tok.revoked_at = datetime.now(timezone.utc)
        db.commit()
        db.close()

        assert _validate_bearer_token(raw, None) is False

    def test_last_used_at_updates(self):
        from mcp_server import _validate_bearer_token
        db = _TestSession()
        user = _make_user(db)
        raw, tok = _create_db_token(db, user.id, label="track-usage")
        assert tok.last_used_at is None
        db.close()

        _validate_bearer_token(raw, None)

        db2 = _TestSession()
        refreshed = db2.query(ApiToken).filter(ApiToken.id == tok.id).first()
        assert refreshed.last_used_at is not None
        db2.close()


# ======================================================================
# Part 4: MCP Resources and Tools (via FastMCP directly)
# ======================================================================

class TestMCPResourcesAndTools:
    """Call MCP resource/tool functions directly (they are plain Python)."""

    def _seed_spec(self):
        """Insert a minimal spec into the DB for resource tests."""
        db = _TestSession()
        existing = db.query(ApiSpec).filter(ApiSpec.name == "TestAPI").first()
        if existing:
            db.close()
            return existing.id
        spec = ApiSpec(
            name="TestAPI",
            version="1.0.0",
            original_format="yaml",
            original_content=(
                "openapi: '3.0.0'\n"
                "info:\n  title: TestAPI\n  version: 1.0.0\n"
                "paths:\n"
                "  /hello:\n"
                "    get:\n"
                "      operationId: getHello\n"
                "      summary: Say hello\n"
                "      responses:\n"
                "        '200':\n"
                "          description: OK\n"
            ),
            markdown_content="# TestAPI",
        )
        db.add(spec)
        db.commit()
        db.refresh(spec)
        sid = spec.id
        db.close()
        return sid

    def test_list_specs_resource(self):
        import json as _json
        from mcp_server import list_specs
        self._seed_spec()
        result = list_specs()
        parsed = _json.loads(result)
        assert isinstance(parsed, list)
        assert any(s["name"] == "TestAPI" for s in parsed)
        test_api = next(s for s in parsed if s["name"] == "TestAPI")
        assert test_api["id"] == test_api["spec_id"]

    def test_get_manifest_resource(self):
        from mcp_server import get_manifest
        sid = self._seed_spec()
        manifest = get_manifest(sid)
        assert isinstance(manifest, str)
        assert len(manifest) > 0
        assert "TestAPI" in manifest

    def test_convert_spec_tool(self):
        import json as _json
        from mcp_server import convert_spec

        sample_yaml = (
            "openapi: '3.0.0'\n"
            "info:\n  title: ToolTest\n  version: 1.0.0\n"
            "paths:\n"
            "  /ping:\n"
            "    get:\n"
            "      operationId: ping\n"
            "      summary: Ping\n"
            "      responses:\n"
            "        '200':\n"
            "          description: pong\n"
        )
        result = convert_spec(sample_yaml, "yaml")
        parsed = _json.loads(result)
        assert "conversion_id" in parsed
        assert parsed["source_type"] == "local"
        assert isinstance(parsed.get("token_count"), int)
        assert parsed.get("token_threshold") == 4000
        assert isinstance(parsed.get("full_markdown"), str)
        assert "manifest" in parsed
        assert isinstance(parsed.get("chunks_available"), list)
        assert len(parsed["chunks_available"]) >= 1
        first_chunk = parsed["chunks_available"][0]
        assert first_chunk["type"] == first_chunk["chunk_type"]
        assert first_chunk["key"] == first_chunk["chunk_key"]

    def test_search_specs_tool(self):
        import json as _json
        from mcp_server import search_specs

        sid = self._seed_spec()
        db = _TestSession()
        spec = db.query(ApiSpec).filter(ApiSpec.id == sid).first()
        users_tag = Tag(name="users")
        db.add(users_tag)
        db.commit()
        db.refresh(users_tag)
        spec.tags.append(users_tag)
        db.commit()
        db.close()

        by_query = _json.loads(search_specs(query="TestAPI"))
        assert any(item["name"] == "TestAPI" for item in by_query)
        queried = next(item for item in by_query if item["name"] == "TestAPI")
        assert queried["id"] == queried["spec_id"]
        by_tag = _json.loads(search_specs(tag="users"))
        assert any(item["spec_id"] == sid for item in by_tag)

    def test_load_spec_tool(self):
        import json as _json
        from mcp_server import load_spec

        sid = self._seed_spec()
        parsed = _json.loads(load_spec(sid))
        assert parsed["spec_id"] == str(sid)
        assert parsed["source_type"] == "marketplace"
        assert isinstance(parsed.get("full_markdown"), str)
        assert isinstance(parsed.get("chunks_available"), list)
        assert "manifest" in parsed
        first_chunk = parsed["chunks_available"][0]
        assert first_chunk["type"] == first_chunk["chunk_type"]
        assert first_chunk["key"] == first_chunk["chunk_key"]

    def test_get_chunk_tool(self):
        import json as _json
        from mcp_server import get_chunk

        sid = self._seed_spec()
        parsed = _json.loads(get_chunk(str(sid), "marketplace", "endpoint", "getHello"))
        assert parsed["source_type"] == "marketplace"
        assert parsed["chunk_type"] == "endpoint"
        assert "manifest" in parsed
        assert "chunk_content" in parsed
        assert "getHello" in parsed["chunk_content"]

    def test_get_chunk_local(self):
        import json as _json
        from mcp_server import convert_spec, get_chunk

        sample_yaml = (
            "openapi: '3.0.0'\n"
            "info:\n  title: LocalChunk\n  version: 1.0.0\n"
            "paths:\n"
            "  /ping:\n"
            "    get:\n"
            "      operationId: ping\n"
            "      summary: Ping\n"
            "      responses:\n"
            "        '200':\n"
            "          description: pong\n"
        )
        converted = _json.loads(convert_spec(sample_yaml, "yaml"))
        conversion_id = converted["conversion_id"]
        parsed = _json.loads(get_chunk(conversion_id, "local", "endpoint", "ping"))
        assert parsed["source_type"] == "local"
        assert parsed["chunk_type"] == "endpoint"
        assert "manifest" in parsed
        assert "ping" in parsed["chunk_content"]

    def test_convert_spec_to_tools(self):
        import json as _json
        from mcp_server import convert_spec_to_tools

        sample_yaml = (
            "openapi: '3.0.0'\n"
            "info:\n  title: ToolTest\n  version: 1.0.0\n"
            "paths:\n"
            "  /ping:\n"
            "    get:\n"
            "      operationId: ping\n"
            "      summary: Ping\n"
            "      responses:\n"
            "        '200':\n"
            "          description: pong\n"
        )
        result = convert_spec_to_tools(sample_yaml, "yaml")
        parsed = _json.loads(result)
        assert isinstance(parsed, list)
        assert len(parsed) >= 1


# ======================================================================
# Part 5: Database Migration
# ======================================================================

class TestDatabaseMigration:
    def test_tables_exist(self):
        inspector = inspect(_test_engine)
        table_names = inspector.get_table_names()
        for expected in ("users", "api_tokens", "api_specs", "tags"):
            assert expected in table_names, f"Missing table: {expected}"


class TestMCPProxyHeaders:
    def test_proxy_forwards_mcp_headers_and_filters_unknown(self, monkeypatch):
        import main

        captured: dict[str, object] = {}

        class _DummyResponse:
            def __init__(self):
                self.status_code = 200
                self.content = b'{"ok":true}'
                self.headers = {"content-type": "application/json", "x-upstream": "1"}

        class _DummyAsyncClient:
            def __init__(self, *args, **kwargs):
                pass

            async def __aenter__(self):
                return self

            async def __aexit__(self, exc_type, exc, tb):
                return False

            async def request(self, method, url, headers=None, content=None):
                captured["method"] = method
                captured["url"] = url
                captured["headers"] = headers or {}
                captured["content"] = content
                return _DummyResponse()

        monkeypatch.setattr(main.httpx, "AsyncClient", _DummyAsyncClient)

        r = client.get(
            "/mcp",
            headers={
                "Authorization": "Bearer test-token",
                "Accept": "application/json",
                "MCP-Session-Id": "session-123",
                "MCP-Custom": "custom-value",
                "X-Should-Not-Forward": "nope",
            },
        )

        assert r.status_code == 200
        forwarded = {k.lower(): v for k, v in captured["headers"].items()}
        assert forwarded["authorization"] == "Bearer test-token"
        assert forwarded["accept"] == "application/json"
        assert forwarded["mcp-session-id"] == "session-123"
        assert forwarded["mcp-custom"] == "custom-value"
        assert "x-should-not-forward" not in forwarded

import pytest
from jwt import InvalidTokenError

from app import app
from controllers import user_controller


@pytest.fixture
def client():
    app.config["TESTING"] = True
    return app.test_client()


def test_login_sets_httponly_token_cookie_and_logout_revokes_it(client, monkeypatch):
    token = "signed-test-token"
    monkeypatch.setattr(
        user_controller.user_service,
        "check_user",
        lambda username, password: {
            "authenticated": True,
            "token": token,
            "user": {"id": 7, "username": "alice"},
        },
    )
    revoked_tokens = []
    monkeypatch.setattr(
        user_controller,
        "revoke_jwt_token",
        lambda value: revoked_tokens.append(value) or True,
    )

    login_response = client.post(
        "/user/login",
        json={"username": "alice", "password": "correct horse battery staple"},
    )

    assert login_response.status_code == 200
    assert login_response.json["data"]["authenticated"] is True
    assert "token" not in login_response.json["data"]
    cookie = client.get_cookie("access_token")
    assert cookie is not None
    assert cookie.value == token
    assert cookie.http_only is True

    logout_response = client.post("/user/logout")

    assert logout_response.status_code == 200
    assert logout_response.json["data"]["logged_out"] is True
    assert revoked_tokens == [token]
    assert client.get_cookie("access_token") is None


def test_login_rejects_invalid_credentials_without_cookie(client, monkeypatch):
    monkeypatch.setattr(
        user_controller.user_service, "check_user", lambda username, password: None
    )

    response = client.post(
        "/user/login",
        json={"username": "alice", "password": "wrong password"},
    )

    assert response.status_code == 401
    assert response.headers.get("Set-Cookie") is None


def test_me_returns_identity_from_valid_cookie(client, monkeypatch):
    monkeypatch.setattr(
        user_controller,
        "check_jwt_token",
        lambda token: {"id": "7", "username": "alice"},
    )

    client.set_cookie("access_token", "test-token")
    response = client.get("/user/me")

    assert response.status_code == 200
    assert response.json["data"] == {"id": 7, "username": "alice"}


def test_me_rejects_missing_or_invalid_cookie(client, monkeypatch):
    missing_response = client.get("/user/me")
    assert missing_response.status_code == 401

    monkeypatch.setattr(
        user_controller,
        "check_jwt_token",
        lambda token: (_ for _ in ()).throw(InvalidTokenError("invalid")),
    )
    client.set_cookie("access_token", "invalid-token")
    invalid_response = client.get("/user/me")

    assert invalid_response.status_code == 401
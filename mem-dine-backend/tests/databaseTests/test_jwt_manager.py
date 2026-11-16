import jwt

from services import jwt_manager


def test_encode_jwt_token_stores_token_with_ttl(monkeypatch):
    secret = "test-secret-for-jwt-signing-32-bytes"
    monkeypatch.setattr(jwt_manager.settings, "jwt_token", secret)
    stored = []
    monkeypatch.setattr(
        jwt_manager.redis_manager,
        "set_string_with_timer",
        lambda key, value, ttl: stored.append((key, value, ttl)) or True,
    )

    token = jwt_manager.encode_jwt_token({"sub": "user-1"})

    assert jwt.decode(token, secret, algorithms=["HS256"]) == {
        "sub": "user-1"
    }
    assert stored == [(token, token)]


def test_check_jwt_token_only_decodes_tokens_found_in_redis(monkeypatch):
    secret = "test-secret-for-jwt-signing-32-bytes"
    monkeypatch.setattr(jwt_manager.settings, "jwt_token", secret)
    token = jwt.encode({"sub": "user-1"}, secret, algorithm="HS256")
    monkeypatch.setattr(
        jwt_manager.redis_manager, "get_string", lambda key: token if key == token else None
    )

    assert jwt_manager.check_jwt_token(token) == {"sub": "user-1"}
    assert jwt_manager.check_jwt_token("missing") is False
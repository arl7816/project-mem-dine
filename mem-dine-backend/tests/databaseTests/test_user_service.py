import sqlite3

from database.DataObjects.User import User
from services import user_service as user_service_module


def test_check_user_returns_jwt_for_authenticated_user(monkeypatch):
    connection = sqlite3.connect(":memory:")
    user_data = User()
    user_data.create(connection)
    user_data.create_user(connection, "alice", "correct horse battery staple")
    monkeypatch.setattr(
        user_service_module.database_connection, "connect", lambda: connection
    )
    encoded_payloads = []
    monkeypatch.setattr(
        user_service_module,
        "encode_jwt_token",
        lambda payload: encoded_payloads.append(payload) or "test-token",
    )
    service = user_service_module.UserService()
    service.user_data = user_data

    result = service.check_user("Alice", "correct horse battery staple")

    assert result is not None
    assert result["token"] == "test-token"
    assert result["authenticated"] is True
    assert result["user"]["username"] == "alice"
    assert encoded_payloads == [{"id": str(result["user"]["id"]), "username": "alice"}]
    connection.close()
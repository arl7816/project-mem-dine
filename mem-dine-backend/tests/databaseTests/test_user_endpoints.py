import sqlite3

import pytest

from app import app
from database.DB import database_connection
from database.DataObjects.User import User


@pytest.fixture
def client(tmp_path, monkeypatch):
    database_path = tmp_path / "users.db"
    monkeypatch.setattr(database_connection, "database_path", str(database_path), raising=False)
    connection = sqlite3.connect(database_path)
    User().create(connection)
    connection.close()

    app.config["TESTING"] = True
    return app.test_client()


def test_create_and_check_user_endpoints(client):
    password = "correct horse battery staple"
    response = client.post(
        "/api/create_user",
        json={"username": "Alice", "password": password},
    )

    assert response.status_code == 201
    assert response.json["data"]["username"] == "alice"
    assert "password" not in response.json["data"]

    response = client.post(
        "/api/check_user",
        json={"username": "ALICE", "password": password},
    )
    assert response.status_code == 200
    assert response.json["data"]["authenticated"] is True

    response = client.post(
        "/api/check_user",
        json={"username": "alice", "password": "wrong password"},
    )
    assert response.status_code == 401
    assert response.json["data"]["error"] == "Invalid username or password"


def test_user_endpoints_validate_input_and_duplicates(client):
    response = client.post("/api/create_user", json={"username": "", "password": "short"})
    assert response.status_code == 400

    payload = {"username": "alice", "password": "correct horse battery staple"}
    assert client.post("/api/create_user", json=payload).status_code == 201
    assert client.post("/api/create_user", json=payload).status_code == 409

    response = client.post("/api/check_user", json={"username": "alice"})
    assert response.status_code == 400
import sqlite3

from database.DataObjects.User import User


def create_user_store():
    connection = sqlite3.connect(":memory:")
    user_store = User()
    assert user_store.create(connection) is True
    return connection, user_store


def test_create_user_hashes_password_and_returns_public_package():
    connection, user_store = create_user_store()
    password = "correct horse battery staple"

    assert user_store.create_user(connection, "alice", password) is True
    user_id = user_store.exists(connection, username="alice")
    user = user_store.get_user(connection, user_id)
    stored_password = connection.execute(
        "SELECT password FROM users WHERE id = ?", (user_id,)
    ).fetchone()[0]

    assert user.id == user_id
    assert user.name == "alice"
    assert user.created_at is not None
    assert not hasattr(user, "password")
    assert stored_password != password
    assert user_store.verify_password(connection, "alice", password) is True
    assert user_store.verify_password(connection, "alice", "wrong password") is False


def test_user_lookups_bind_input_as_data():
    connection, user_store = create_user_store()
    injection_shaped_name = "' OR 1=1 --"

    assert user_store.create_user(
        connection, injection_shaped_name, "correct horse battery staple"
    ) is True
    user_id = user_store.exists(connection, username=injection_shaped_name)

    assert user_id > 0
    assert user_store.exists(connection, username="' OR 1=1 -- '") == -1
    assert user_store.get_user(connection, "1 OR 1=1") is None


def test_duplicate_usernames_and_weak_passwords_are_rejected():
    connection, user_store = create_user_store()

    assert user_store.create_user(
        connection, "alice", "correct horse battery staple"
    ) is True
    assert user_store.create_user(
        connection, "alice", "another secure password"
    ) is False
    assert user_store.create_user(connection, "bob", "short") is False
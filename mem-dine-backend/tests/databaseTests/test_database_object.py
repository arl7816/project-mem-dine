import pytest

def test_database_singleton():
    from database.DB import DatabaseConnection

    db1 = DatabaseConnection()
    db2 = DatabaseConnection()

    assert db1 == db2
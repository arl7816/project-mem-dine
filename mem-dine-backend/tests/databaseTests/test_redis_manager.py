from unittest.mock import Mock

from database.RedisManger import _RedisManager


def test_redis_manager_delegates_commands():
    manager = _RedisManager()
    manager.connection = Mock()
    manager.connection.setex.return_value = True
    manager.connection.get.return_value = "value"
    manager.connection.delete.return_value = 1
    manager.connection.ping.return_value = True

    assert manager.set_string_with_timer("key", "value", 30) is True
    assert manager.get_string("key") == "value"
    assert manager.delete_key("key") is True
    assert manager.ping() is True

    manager.connection.setex.assert_called_once_with("key", 30, "value")
    manager.connection.get.assert_called_once_with("key")
    manager.connection.delete.assert_called_once_with("key")
    manager.connection.ping.assert_called_once_with()


def test_redis_manager_reports_missing_values_and_keys():
    manager = _RedisManager()
    manager.connection = Mock()
    manager.connection.get.return_value = None
    manager.connection.delete.return_value = 0

    assert manager.get_string("missing") is None
    assert manager.delete_key("missing") is False
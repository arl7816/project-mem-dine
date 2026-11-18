import redis
from services.settings import settings

class _RedisManager:
    def __init__(self):
        self.connection = redis.Redis(
            host="localhost", 
            port=settings.redis_port,
            db=0,
            decode_responses=True
        )

    def set_string_with_timer(self, 
            key: str,
            value: str, 
            time_seconds: int = 60
    ) -> bool:
        return bool(self.connection.setex(
            key, time_seconds, value
        ))

    def get_string(self, key: str) -> str | None:
        return self.connection.get(key)

    def delete_key(self, key: str) -> bool:
        return bool(self.connection.delete(key))

    def ping(self) -> bool:
        return bool(self.connection.ping())

    def close(self) -> None:
        self.connection.close()


redis_manager = _RedisManager()
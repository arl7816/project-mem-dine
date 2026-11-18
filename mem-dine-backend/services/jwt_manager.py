from typing import Any

import jwt
from services.settings import settings
from database.RedisManger import redis_manager


def encode_jwt_token(payload: dict[str, Any]) -> str:
	token = jwt.encode(payload, settings.jwt_token, algorithm="HS256")
	redis_manager.set_string_with_timer(token, token, settings.jwt_seconds)
	return token


def check_jwt_token(token: str) -> dict[str, Any] | bool:
	stored_token = redis_manager.get_string(token)
	if stored_token is None:
		return False
	return jwt.decode(stored_token, settings.jwt_token, algorithms=["HS256"])


def revoke_jwt_token(token: str) -> bool:
	return redis_manager.delete_key(token)


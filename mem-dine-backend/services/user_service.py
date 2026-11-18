from database.DB import database_connection
from database.DataObjects.User import User
from services.jwt_manager import encode_jwt_token


class InvalidUserDataError(ValueError):
    pass


class UsernameAlreadyExistsError(Exception):
    pass


class UserService:
    def __init__(self):
        self.user_data = User()

    def create_user(self, username: str, password: str) -> dict:
        normalized_username = username.strip().lower()
        if (
            not normalized_username
            or len(normalized_username) > 64
            or not 12 <= len(password) <= 1024
        ):
            raise InvalidUserDataError("Invalid username or password requirements")

        connection = database_connection.connect()
        try:
            if self.user_data.exists(connection, username=normalized_username) != -1:
                raise UsernameAlreadyExistsError("Username is already in use")
            if not self.user_data.create_user(connection, normalized_username, password):
                raise UsernameAlreadyExistsError("Username is already in use")

            user_id = self.user_data.exists(connection, username=normalized_username)
            return {"id": user_id, "username": normalized_username}
        finally:
            connection.close()

    def check_user(self, username: str, password: str) -> dict | None:
        authenticated_user = self.verify_user(username, password)
        if authenticated_user is None:
            return None

        user = authenticated_user["user"]
        token = encode_jwt_token({"id": str(user["id"]), "username": user["username"]})
        return {**authenticated_user, "token": token}

    def verify_user(self, username: str, password: str) -> dict | None:
        normalized_username = username.strip().lower()
        connection = database_connection.connect()
        try:
            if not self.user_data.verify_password(
                connection, normalized_username, password
            ):
                return None

            user_id = self.user_data.exists(connection, username=normalized_username)
            user = self.user_data.get_user(connection, user_id)
            if user is None:
                return None

            return {
                "authenticated": True,
                "user": {"id": user.id, "username": user.name},
            }
        finally:
            connection.close()


user_service = UserService()
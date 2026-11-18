from flask import Blueprint, jsonify, request
from jwt import PyJWTError

from classes.api_classes import ResponseObject
from helpers.validate_response import validate_response
from services.jwt_manager import check_jwt_token, revoke_jwt_token
from services.settings import settings
from services.user_service import (
    InvalidUserDataError,
    UsernameAlreadyExistsError,
    user_service,
)


user_blueprint = Blueprint("users", __name__, url_prefix="/user")


def _read_credentials():
    payload = request.get_json(silent=True)
    if not isinstance(payload, dict):
        return ResponseObject.error("A JSON object is required")

    username = payload.get("username")
    password = payload.get("password")
    if not isinstance(username, str) or not isinstance(password, str):
        return ResponseObject.error("Username and password are required", status_code=400)

    return username, password


@user_blueprint.route("/create_user", methods=["POST"])
@validate_response
def create_user():
    credentials = _read_credentials()
    if isinstance(credentials, ResponseObject):
        return credentials

    username, password = credentials
    try:
        user = user_service.create_user(username, password)
    except InvalidUserDataError as error:
        return ResponseObject.error(str(error), 400)
    except UsernameAlreadyExistsError as error:
        return ResponseObject.error(str(error), 409)

    return ResponseObject.success(user, status_code=201)


@user_blueprint.route("/check_user", methods=["POST"])
@validate_response
def check_user():
    credentials = _read_credentials()
    if isinstance(credentials, ResponseObject):
        return credentials

    username, password = credentials
    user = user_service.verify_user(username, password)
    if user is None:
        return ResponseObject.error("Invalid username or password", 401)

    return ResponseObject.success(
        {"authenticated": True, "user": user["user"]}
    )


@user_blueprint.route("/login", methods=["POST"])
@validate_response
def login():
    credentials = _read_credentials()
    if isinstance(credentials, ResponseObject):
        return credentials

    username, password = credentials
    user = user_service.check_user(username, password)
    if user is None:
        return ResponseObject.error("Invalid username or password", 401)

    token = user["token"]
    response = jsonify(
        ResponseObject.success(
            {"authenticated": True, "user": user["user"]}
        )
    )
    response.set_cookie(
        "access_token",
        token,
        max_age=settings.jwt_seconds,
        httponly=True,
        secure=not settings.debug,
        samesite="Lax",
    )
    return response


@user_blueprint.route("/logout", methods=["POST"])
@validate_response
def logout():
    token = request.cookies.get("access_token")
    if token:
        revoke_jwt_token(token)

    response = jsonify(ResponseObject.success({"logged_out": True}))
    response.delete_cookie(
        "access_token",
        httponly=True,
        secure=not settings.debug,
        samesite="Lax",
    )
    return response

@user_blueprint.route("/me", methods=["GET"])
@validate_response
def me():
    token = request.cookies.get("access_token")
    if not token:
        return ResponseObject.error("Not logged in", 401)

    try:
        payload = check_jwt_token(token)
    except PyJWTError:
        return ResponseObject.error("Invalid or expired token", 401)

    if (
        not isinstance(payload, dict)
        or not payload.get("id")
        or not isinstance(payload.get("username"), str)
    ):
        return ResponseObject.error("Invalid or expired token", 401)

    try:
        user_id = int(payload["id"])
    except (TypeError, ValueError):
        return ResponseObject.error("Invalid or expired token", 401)

    return ResponseObject.success({"id": user_id, "username": payload["username"]})
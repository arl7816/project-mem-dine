from flask import Blueprint, request

from classes.api_classes import ResponseObject
from helpers.validate_response import validate_response
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
        return ResponseObject.error("Username and password are required")

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
    user = user_service.check_user(username, password)
    if user is None:
        return ResponseObject.error("Invalid username or password", 401)

    return ResponseObject.success(user)
from flask import Blueprint

from classes.api_classes import ResponseObject
from helpers.validate_response import validate_response


health_blueprint = Blueprint("health", __name__, url_prefix="/health")


@health_blueprint.route("/hello", methods=["GET"])
@validate_response
def hello_world():
    return ResponseObject.success("Hello World!")
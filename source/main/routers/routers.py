from flask import Blueprint, request, jsonify
from source.main.adapters.request_adapter import request_adapter
from source.main.composer.user_finder_composer import use_finder_composer
from source.main.composer.user_registry_composer import use_register_composer

user_router_bp = Blueprint("user_routes", __name__)


@user_router_bp.route("/users/find", methods=['GET'])
def find_user():
    http_response = request_adapter(request, use_finder_composer())
    return jsonify(http_response.body), http_response.status_code


@user_router_bp.route("/users", methods=['POST'])
def registry_user():
    http_response = request_adapter(request, use_register_composer())
    return jsonify(http_response.body), http_response.status_code

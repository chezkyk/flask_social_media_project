from flask import Blueprint, jsonify
from services.user import fetch_all_users, fetch_user_by_id

user_bp = Blueprint('user', __name__, url_prefix='/api/user')

@user_bp.route('', methods=['GET'])
def get_all_users():
    users = fetch_all_users()
    return jsonify(users), 200

@user_bp.route('/<int:id>', methods=['GET'])
def get_user_by_id_route(id):
    user = fetch_user_by_id(id)
    if user:
        return jsonify(user), 200
    else:
        return jsonify({"message": "User not found"}), 404


from flask import Blueprint, jsonify
from services.user import fetch_all_users, fetch_user_by_id

user_bp = Blueprint('user', __name__, url_prefix='/api/user')

@user_bp.route('', methods=['GET'])
def get_all_users():
    users = fetch_all_users()
    serialized_users = [serialize_user(user) for user in users]
    return jsonify(serialized_users), 200

@user_bp.route('/<int:id>', methods=['GET'])
def get_user_by_id(id):
    user = fetch_user_by_id(id)
    serialized_user = serialize_user(user)
    if serialized_user:
        return jsonify(serialized_user), 200
    else:
        return jsonify({"message": "User not found"}), 404

def serialize_user(user):
    user['_id'] = str(user['_id'])
    return user

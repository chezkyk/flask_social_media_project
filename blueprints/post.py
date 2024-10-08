from flask import Blueprint, jsonify, request
from services.post import fetch_all_posts,fetch_post_by_id
post_bp = Blueprint('post', __name__,url_prefix='/api/post')

@post_bp.route('', methods=['GET'])
def get_all_posts_route():
    posts = fetch_all_posts()
    return jsonify(posts), 200

@post_bp.route('/<int:id>', methods=['GET'])
def get_post_by_id(id):
    post = fetch_post_by_id(id)
    if post:
        return jsonify(post), 200
    else:
        return jsonify({"message": "Post not found"}), 404




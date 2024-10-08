from flask import Flask
from config import COLLECTION_NAMES,USERS_URL,POSTS_URL
from utils.import_data_api import insert_users ,insert_posts
from blueprints.user import user_bp
from blueprints.post import post_bp
app = Flask(__name__)
# insert_users(COLLECTION_NAMES[0], USERS_URL)
# insert_posts(COLLECTION_NAMES[1], POSTS_URL)
app.register_blueprint(user_bp)
app.register_blueprint(post_bp)


if __name__ == '__main__':
    app.run(debug=True)

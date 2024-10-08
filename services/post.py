from db import get_db_connection

def fetch_all_posts():
    client, db = get_db_connection()
    posts = list(db['posts'].find())
    client.close()
    return posts
def fetch_post_by_id(post_id):
    client, db = get_db_connection()
    post = db['posts'].find_one({"id": post_id})
    client.close()
    return post

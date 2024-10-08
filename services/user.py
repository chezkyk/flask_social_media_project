
from db import get_db_connection

def fetch_all_users():
    client, db = get_db_connection()
    users = list(db['users'].find())
    client.close()
    return users

def fetch_user_by_id(user_id):
    client, db = get_db_connection()
    user = list(db['users'].find_one({"id": user_id}))
    client.close()
    return user
from pymongo import MongoClient
from config import MONGO_URI, DB_NAME

def get_db_connection():
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    return client,db
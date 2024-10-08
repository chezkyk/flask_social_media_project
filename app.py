from flask import Flask
from config import COLLECTION_NAMES,USERS_URL
from utils.import_data_api import insert_users
app = Flask(__name__)



if __name__ == '__main__':
    app.run()

# insert_users(COLLECTION_NAMES[0],USERS_URL)

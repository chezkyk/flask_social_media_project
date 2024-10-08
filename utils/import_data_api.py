from db import get_db_connection
from flask import requests
from models.user import User
from models.geo import Geo
from models.address import Address
from models.company import Company
from models.post import Post

def insert_users(collection_name, api_url):
    client, db = get_db_connection()
    data = db[collection_name]
    if not data:
        try:
            response = requests.get(api_url)
            response.raise_for_status()
            users_data = response.json()

            user_objects = []
            for user in users_data:
                geo = Geo(lat=user['address']['geo']['lat'], lng=user['address']['geo']['lng'])
                address = Address(street=user['address']['street'], suite=user['address']['suite'],
                                  city=user['address']['city'], zipcode=user['address']['zipcode'], geo=geo)
                company = Company(name=user['company']['name'], catch_phrase=user['company']['catchPhrase'],
                                  bs=user['company']['bs'])
                user_obj = User(user_id=user['id'], name=user['name'], username=user['username'],
                                email=user['email'], address=address, phone=user['phone'],
                                website=user['website'], company=company)
                user_objects.append(user_obj.to_dict())

            db[collection_name].insert_many(user_objects)

            print(f"Inserted {len(user_objects)} users into {collection_name} collection.")
        except requests.exceptions.ConnectionError:
            print('Failed to connect to API')
        except requests.exceptions.HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')  # טעות בבקשה
        except Exception as e:
            print(f'An error occurred: {e}')  # טעות אחרת
    else:
        print(f"Data already exists in {collection_name} collection.")
    client.close()


def insert_posts(collection_name, api_url):
    client, db = get_db_connection()
    data = db[collection_name]
    if not data:
        try:
            response = requests.get(api_url)
            response.raise_for_status()
            posts_data = response.json()
            post_objects = []
            for post_data in posts_data:
                post = Post(user_id=post_data['userId'], post_id=post_data['id'],
                            title=post_data['title'], body=post_data['body'])
                post_objects.append(post.to_dict())

            db[collection_name].insert_many(post_objects)
            print(f"Inserted {len(post_objects)} posts into {collection_name} collection.")

        except requests.exceptions.ConnectionError:
            print('Failed to connect to API')
        except requests.exceptions.HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as e:
            print(f'An error occurred: {e}')
    else:
        print(f"Data already exists in {collection_name} collection.")

    client.close()
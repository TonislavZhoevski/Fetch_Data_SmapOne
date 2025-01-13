from pymongo import MongoClient
from pymongo.server_api import ServerApi
from config import ATLAS_URI


if __name__ == "__main__":
    try:
        client = MongoClient(ATLAS_URI, server_api=ServerApi('1'))
        client.admin.command('ping')
        print("Pinged your deployment. Successfully connected to MongoDB!")
    except Exception as e:
        print(f"Failed to connect to MongoDB: {e}")
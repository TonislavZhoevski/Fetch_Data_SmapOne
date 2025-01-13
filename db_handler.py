from pymongo import MongoClient

def connect_to_db(uri, db_name, collection_name):
    """Connect to MongoDB and return the collection."""
    try:
        client = MongoClient(uri)
        db = client[db_name]
        print(f"Connected to MongoDB at {uri}.")
        return db[collection_name]
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")
        return None

def insert_data(collection, data):
    """Insert or update data in MongoDB."""
    if not isinstance(data, list):
        print("Data must be a list of dictionaries.")
        return
    try:
        collection.insert_many(data, ordered=False)
        print(f"Successfully inserted {len(data)} records into MongoDB.")
    except Exception as e:
        print(f"Error inserting data: {e}")

from pymongo import MongoClient

def connect_to_mongo(uri, db_name, collection_name):
    """Connect to MongoDB and return the collection."""
    client = MongoClient(uri)
    db = client[db_name]
    return db[collection_name]

def insert_or_update_data(collection, data, unique_field="id"):
    """Insert or update records in MongoDB."""
    for record in data:
        # Upsert: Update if exists, insert if not
        collection.update_one(
            {unique_field: record[unique_field]},  # Match unique field
            {"$set": record},                     # Update fields
            upsert=True                           # Insert if no match
        )
    print("Data stored successfully in MongoDB!")

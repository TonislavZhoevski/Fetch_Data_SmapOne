from fetch_smap_definition import fetch_data
from data_handler import process_data
from db_handler import connect_to_mongo, insert_or_update_data
from config import MONGO_URI, DB_NAME, COLLECTION_NAME, SMAP_ID, VERSION

def main():
    # Step 1: Fetch data from SmapOne
    print("Fetching data from SmapOne...")
    raw_data = fetch_data(SMAP_ID, VERSION)
    if not raw_data:
        print("Failed to fetch data from SmapOne.")
        return

    # Step 2: Process the data
    print("Processing fetched data...")
    processed_data = process_data(raw_data)

    # Step 3: Connect to MongoDB
    print("Connecting to MongoDB...")
    collection = connect_to_mongo(MONGO_URI, DB_NAME, COLLECTION_NAME)

    # Step 4: Store the processed data in MongoDB
    print("Storing data in MongoDB...")
    insert_or_update_data(collection, processed_data)

if __name__ == "__main__":
    main()
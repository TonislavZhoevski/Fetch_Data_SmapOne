from fetch_data import fetch_data
from db_handler import connect_to_db, insert_data
from config import ATLAS_URI, ATLAS_DB, ATLAS_COLLECTION, LOCAL_URI, LOCAL_DB, LOCAL_COLLECTION

def main():
    # Step 1: Fetch data from SmapOne
    print("Fetching data from SmapOne...")
    data = fetch_data()

    if not data:
        print("No data fetched. Exiting...")
        return

    # Step 2: Store data in MongoDB Atlas
    print("\n--- Storing Data in MongoDB Atlas ---")
    atlas_collection = connect_to_db(ATLAS_URI, ATLAS_DB, ATLAS_COLLECTION)
    if atlas_collection is not None:
        insert_data(atlas_collection, data)

    # Step 3: Store data in Local MongoDB
    print("\n--- Storing Data in Local MongoDB ---")
    local_collection = connect_to_db(LOCAL_URI, LOCAL_DB, LOCAL_COLLECTION)
    if local_collection is not None:
        insert_data(local_collection, data)
    else:
        print("Error connecting to Local MongoDB.")

if __name__ == "__main__":
    main()
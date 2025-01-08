from smapone_api import fetch_data, update_data
from data_handler import process_data

# Smap configuration
SMAP_ID = "e7e9255f-3109-4498-801e-2ba407950c53"
VERSION = "11.0"

def main():
    print("Fetching data...")
    data = fetch_data(SMAP_ID, VERSION)

    print("Fetched Data:", data)

    if data:
        print("Processing data...")
        updated_data = process_data(data)
        print("Updating data...")
        response = update_data(SMAP_ID, VERSION, updated_data)
        if response:
            print("Data successfully updated!")
        else:
            print("Failed to update data.")
    else:
        print("Failed to fetch data.")

if __name__ == "__main__":
    main()
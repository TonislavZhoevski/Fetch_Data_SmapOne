import requests

# Configuration values
API_KEY = "452ab15f3aec793473ef4395c02752c055031102"
BASE_URL = "https://platform.smapone.com/Backend/intern"
SMAP_ID = "e7e9255f-3109-4498-801e-2ba407950c53"
VERSION = "11.0"

def fetch_smap_data():
    """Fetch data for a specific Smap."""
    url = f"{BASE_URL}/Smaps/{SMAP_ID}/Versions/{VERSION}/Data"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Accept": "application/json"
    }
    params = {
        "markAsExported": "false",
        "format": "Json"
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        print("Fetched Data:")
        print(response.json())
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

if __name__ == "__main__":
    fetch_smap_data()

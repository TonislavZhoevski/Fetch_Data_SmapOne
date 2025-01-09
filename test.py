import requests
from config import BASE_URL, ACCESS_TOKEN

SMAP_ID = "e7e9255f-3109-4498-801e-2ba407950c53"
VERSION = "11.0"

def fetch_smap_data():
    url = f"{BASE_URL}/Smaps/{SMAP_ID}/VErsion/{VERSION}/Data"
    headers = {
        "Authorization": f"Basic {ACCESS_TOKEN}",
        "Accept": "application/json"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        print("Fetched Data:")
        print(response.json())
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occured: {http_err}")
    except Exception as err:
        print(f"An error occured: {err}")
    
if __name__=="__main__":
    fetch_smap_data()



import requests
from config import BASE_URL, HEADERS

def fetch_data(smap_id, version):
    """Fetch data from the SmapOne API."""
    url = f"{BASE_URL}/Smaps/{smap_id}/Versions/{version}/Data"
    try:
        response = requests.get(url, headers=HEADERS, params={"markAsExported": "false", "format": "Json"})
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def update_data(smap_id, version, updated_data):
    """Update data on the SmapOne platform."""
    url = f"{BASE_URL}/Smaps/{smap_id}/Versions/{version}/Data"
    try:
        response = requests.put(url, headers=HEADERS, json=updated_data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error updating data: {e}")
        return None

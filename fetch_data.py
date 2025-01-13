import requests
from config import SMAPONE_URL, HEADERS

def fetch_data():
    """Fetch data from SmapOne API."""
    try:
        response = requests.get(SMAPONE_URL, headers=HEADERS,)
        print(f"Status Code: {response.status_code}")
        print(f"Response Content: {response.text}")
        response.raise_for_status()  # Raise error for bad responses (4xx or 5xx)
        data = response.json()
        print("Data fetched successfully.")
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

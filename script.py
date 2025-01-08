import requests

API_KEY = "452ab15f3aec793473ef4395c02752c055031102"
SMAP_ID = "e7e9255f-3109-4498-801e-2ba407950c53"
BASE_URL = "https://platform.smapone.com/Backend/intern"
VERSION = "11.0"

url = f"{BASE_URL}/Smaps/{SMAP_ID}/Versions/{VERSION}/Definition"
headers = {"Authorization": f"Bearer {API_KEY}", "accept": "application/json"}

response = requests.get(url, headers=headers)
print(response.json())
import requests
from requests.auth import HTTPBasicAuth

url = "https://platform.smapone.com/Backend/intern/Smaps/e7e9255f-3109-4498-801e-2ba407950c53/Versions/11.0/Data?markAsExported=false&format=Json&accessToken=452ab15f3aec793473ef4395c02752c055031102"
username = "User 03"
password = "kMX_6nhTH7_F0_qF0sUK"

response = requests.get(url, auth=HTTPBasicAuth(username, password))

if response.status_code == 200:
    print("Data fetched successfully:", response.json())
else:
    print(f"Failed to fetch data: {response.status_code} - {response.text}")

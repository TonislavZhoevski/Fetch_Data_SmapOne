import requests
import pandas as pd
from requests.auth import HTTPBasicAuth

url = "https://platform.smapone.com/Backend/intern/Smaps/e7e9255f-3109-4498-801e-2ba407950c53/Versions/11.0/Data?markAsExported=false&format=Json&accessToken=452ab15f3aec793473ef4395c02752c055031102"
username = "User 03"
password = "kMX_6nhTH7_F0_qF0sUK"

# Fetch the data
response = requests.get(url, auth=HTTPBasicAuth(username, password))

# Check for successful response
if response.status_code == 200:
    # Parse the JSON response directly into a DataFrame
    try:
        data = response.json()  # Ensure the response is parsed as JSON
        if isinstance(data, list):  # If the response is a list of records
            df = pd.DataFrame(data)
            print("Data fetched successfully:")
            print(df)
        else:
            print("Unexpected data format:", data)
    except ValueError as e:
        print("Failed to decode JSON:", e)
else:
    print(f"Failed to fetch data: {response.status_code} - {response.text}")

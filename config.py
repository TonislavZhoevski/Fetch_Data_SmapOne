# SmapOne API Configuration
ACCESS_TOKEN = "452ab15f3aec793473ef4395c02752c055031102"
BASE_URL = "https://platform.smapone.com/Backend/intern"
SMAP_ID = "e7e9255f-3109-4498-801e-2ba407950c53"
VERSION = "11.0"
SMAPONE_URL = f"{BASE_URL}/Smaps/{SMAP_ID}/Versions/{VERSION}/Data?markAsExported=false&format=Json&accessToken={ACCESS_TOKEN}"

# Headers for API requests
HEADERS = {
    "Authorization": f"Basic {ACCESS_TOKEN}",
    "Accept": "application/json",
    "Content-Type": "application/json",
    "cache-control": "no-cache",
}

# MongoDB Atlas Configuration
ATLAS_URI = "mongodb+srv://tonislavzhoevski:RagnarLothbrok1RicardoQuaresma4@cluster0.ize8r.mongodb.net/"
ATLAS_DB = "smapone"
ATLAS_COLLECTION = "data"

# MongoDB Local Configuration
LOCAL_URI = "mongodb://127.0.0.1:27017"
LOCAL_DB = "smapone"
LOCAL_COLLECTION = "data"

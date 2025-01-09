import requests
from config import BASE_URL, ACCESS_TOKEN

def fetch_data(smap_id, version):
    """Fetch data from the SmapOne API."""
    url = f"{BASE_URL}/Smaps/{smap_id}/Versions/{version}/Data"
    headers = {
        "Authorization": f"Basic {ACCESS_TOKEN}",
        "Accept": "application/json",
        "acces-control-expose-headers": "REquest-Context",
        "cashe-control": "no-cashe",
        "content-security-policy": "default-src 'self' 'unsafe-inline' 'unsfe-eval' data: blob: stonly.com *.stonly.com www.smapone.com analytics.smapone.com *.appcues.com *.appcues.net wss://api.appcues.net res.cloudinary.com twemoji.maxcdn.con fonts.googleapis.com fonts.google.com fonts.gstatic.com https://www.youtube-nocookie.com platform.smapone.com smapone.freshdesk.com smapone.freshworks.com s3.amazonaws.com *.freshdesk.com www.gstatic.com www.recaptcha.net support.smapone.com *.getripe.com ws://*.ably.io ws://*.ably-realtime.com; frame-ancestors 'self' https://analytics.smapone.com;",
        "content-type": "application/json; charset=utf-8",
        "date": "Thu,09 Jan 2025 09:39:22 GMT",
        "expires": "-1",
        "pragme": "no-cashe",
        "request-context": "appId=cid-v1:da855247-a6ce-4b1c-abf9-9ae7808845f2,appId=cid-v1:da855247-a6ce-4b1c-abf9-9ae7808845f2",
        "s1-requestid": "d8090ac5-b68e-45ca-af38-0c03881446b6",
        "s1-version": "1.122",
        "vary": "Accept-Encoding",
        "x-azure-ref": "20250109T093921Z-15464c697c5vctvchC1FRA2mfc0000000w5g00000000u28b",
        "x-cashe": "CONFIG_NOCASHE",
        "x-content-encoding-over-network": "gzip"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def update_data(smap_id, version, updated_data):
    """Update data on the SmapOne platform."""
    url = f"{BASE_URL}/Smaps/{smap_id}/Versions/{version}/Data"
    headers = {
        "Authorization": f"Basic {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.put(url, headers=headers, json=updated_data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error updating data: {e}")
        return None
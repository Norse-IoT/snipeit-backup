import requests
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

SNIPEIT_TOKEN = os.environ.get("SNIPEIT_TOKEN")
BASE = os.environ.get("SNIPEIT_BASE_URL") or "http://10.0.1.4"

url = f"{base}/api/v1/settings/backups/download/file"

headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {TOKEN}"
}

response = requests.get(url, headers=headers)

print(response.text)

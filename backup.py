import requests
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

SNIPEIT_TOKEN = os.environ.get("SNIPEIT_TOKEN")
BASE = os.environ.get("SNIPEIT_BASE_URL") or "http://10.0.1.77"
SCRIPT_LOCATION = os.path.dirname(__file__)
BACKUP_DIR = os.environ.get("SNIPEIT_BACKUP_DIR") or f"{SCRIPT_LOCATION}/backups"

HEADERS = {
    "accept": "application/json",
    "Authorization": f"Bearer {SNIPEIT_TOKEN}"
}

def get_remote_backups() -> set[str]:
    url = f"{BASE}/api/v1/settings/backups"

    response = requests.get(url, headers=HEADERS)

    return {backup['filename'] for backup in response.json()['rows']}

def get_local_backups() -> set[str]:
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)
    return set(os.listdir(BACKUP_DIR))

def download_backup(backup_name: str):
    print(f"DOWNLOADING {backup_name}...")

    url = f"{BASE}/api/v1/settings/backups/download/{backup_name}"

    response = requests.get(url, headers=HEADERS)

    open(f"{BACKUP_DIR}/{backup_name}", 'wb').write(response.content)

def backup_snipeit():
    print("Starting backup...")
    # set difference
    to_download = get_remote_backups() - get_local_backups()

    print(f"found {len(to_download)} new backups")

    for filename in to_download:
        download_backup(filename)

    print("done!")


backup_snipeit()


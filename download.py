import os
import requests

print(
    """
   ____ _ _   ____             _         ____                      _                 _           
  / ___(_) |_|  _ \ _   _  ___| | __    |  _ \  _____      ___ __ | | ___   __ _  __| | ___ _ __ 
 | |  _| | __| | | | | | |/ __| |/ /    | | | |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |/ _ \ '__|
 | |_| | | |_| |_| | |_| | (__|   <     | |_| | (_) \ V  V /| | | | | (_) | (_| | (_| |  __/ |   
  \____|_|\__|____/ \__,_|\___|_|\_\    |____/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|\___|_|   
                                                                                                 
"""
)

BASE_URL = "https://storage.googleapis.com/gitduck-live/app/4e41c9a00bc4e89bfb94b2b1679b2ec14a7470f215f7b0a1ff6cdf2bc5278c53/1576177423635-e6606a0a-ac69-4bc7-a916-2a1a40cd0fc7"
OUTPUT_DIR = "downloads/gitduck_updates"
ITTERATOR = 1

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

while True:

    file_name = f"index{ITTERATOR}.ts"

    url = f"{BASE_URL}/{file_name}"

    print(f"Downloading : { file_name}")

    r = requests.get(url)

    if r.status_code == 404:
        print(f"Filename : {file_name} not found, ending.")
        break

    open(f"{OUTPUT_DIR}/{file_name}", "wb").write(r.content)

    ITTERATOR += 1


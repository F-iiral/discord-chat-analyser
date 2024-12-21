import requests
from src.helper.logger import Logger

def check_access(channel_id: str, token: str) -> bool:
    url = f"https://discord.com/api/v9/channels/{channel_id}"
    headers = {"authorization": token}
    params = {}

    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        return False
    
    data = response.json()

    if data["type"] == 0:   # Chat
        Logger.log(f"Found server channel '#{data['name']}' and will now collect message data.", True)
        return True
    if data["type"] == 1:   # DM
        Logger.log(f"Found DM with '{ data['recipients'][0]['username']}' ({ data['recipients'][0]['id']} and will now collect message data.", True)
        return True
    if data["type"] == 2:   # Voice Chat
        Logger.log(f"Found server VC '#{data['name']}' and will now collect message data from its side chat.", True)
        return True
    if data["type"] == 3:   # Group DM
        recievers = ""

        for recipient in data['recipients']:
            recievers += f"'{recipient['username']}' ({data['id']}), "
        recievers = recievers[:-2]
        recievers = recievers[::-1].replace(",", "dna ", 1)[::-1]

        Logger.log(f"Found Group DM with {recievers} and will now collect message data.", True)
        return True
    else:
        Logger.log(f"Found channel '#{data['name']}' and will now collect message data.", True)
        return True

def fetch_messages(channel_id: str, token: str) -> list[dict]:
    url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
    headers = {"authorization": token}
    params = {"limit": 50}

    messages = []
    count = 0

    while True:
        Logger.log(f"Starting request: No#{count}")

        response = requests.get(url, headers=headers, params=params)
        if response.status_code != 200:
            raise Exception(f"Error fetching messages: {response.status_code}, {response.text}")
        
        batch = response.json()
        if not batch:
            break
        
        count += 1
        messages.extend(batch)
        params["before"] = batch[-1]["id"]
    
    return messages
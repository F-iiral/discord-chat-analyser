from datetime import datetime

def process_messages(messages: list[dict]) -> list[dict]:
    processed_messages = []
    
    for message in messages:
        user_id = message["author"]["id"]
        username = message["author"]["username"]
        timestamp = datetime.fromisoformat(message["timestamp"].replace("Z", "+00:00"))

        processed_messages.append({"id": user_id, "username": username, "time": timestamp})
    
    return processed_messages
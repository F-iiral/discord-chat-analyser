from datetime import datetime, timezone, timedelta

def process_messages(messages: list[dict]) -> list[dict]:
    processed_messages = []
    tz = datetime.now(timezone(timedelta(0))).astimezone().tzinfo

    for message in messages:
        user_id = message["author"]["id"]
        username = message["author"]["username"]
        timestamp = datetime.fromisoformat(message["timestamp"].replace("Z", "+00:00")).astimezone(tz)

        processed_messages.append({"id": user_id, "username": username, "time": timestamp})
    
    return processed_messages
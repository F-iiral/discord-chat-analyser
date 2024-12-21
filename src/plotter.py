import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

def plot_messages(processed_messages: list[dict]) -> None:
    fig, axes = plt.subplots(2, 1, figsize=(10, 10))

    # Overall activity by hour
    times = [msg["time"].hour for msg in processed_messages]
    activity_by_time = Counter(times)
    
    time_labels = list(activity_by_time.keys())
    counts = list(activity_by_time.values())

    axes[0].bar(time_labels, counts, color="blue")
    axes[0].set_xlabel("Hour of Day")
    axes[0].set_ylabel("Number of Messages")
    axes[0].set_title("Overall Activity by Hour")
    axes[0].set_xticks(range(0, 24))
    axes[0].set_xticklabels([f"{h}:00" for h in range(0, 24)])

    # Activity by user and hour
    user_activity = {}
    for msg in processed_messages:
        user_activity.setdefault(msg["username"], Counter())[msg["time"].hour] += 1

    time_labels = range(0, 24)
    users = list(user_activity.keys())
    bar_width = 0.8 / len(users)
    x_positions = np.arange(len(time_labels))

    for idx, user in enumerate(users):
        counts = [user_activity[user].get(t, 0) for t in time_labels]
        axes[1].bar(x_positions + idx * bar_width, counts, bar_width, label=user)

    axes[1].set_xlabel("Hour of Day")
    axes[1].set_ylabel("Number of Messages")
    axes[1].set_title("Activity by User")
    axes[1].set_xticks(x_positions + bar_width * (len(users) - 1) / 2)
    axes[1].set_xticklabels([f"{h}:00" for h in time_labels], rotation=45)
    axes[1].legend(title="Users")

    plt.tight_layout()
    plt.show()
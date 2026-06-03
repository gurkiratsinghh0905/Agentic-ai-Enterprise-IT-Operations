import json
import os


LOG_FILE = "logs/execution.json"


def log_event(event: dict):
    """Append a workflow execution event to the JSON log file."""
    os.makedirs("logs", exist_ok=True)

    with open(LOG_FILE, "a") as f:
        json.dump(event, f, default=str)
        f.write("\n")

import json
import os


LOG_FILE = "logs/execution.json"


def log_event(event):

    os.makedirs(
        "logs",
        exist_ok=True
    )

    with open(
        LOG_FILE,
        "a"
    ) as f:

        json.dump(
            event,
            f
        )

        f.write("\n")
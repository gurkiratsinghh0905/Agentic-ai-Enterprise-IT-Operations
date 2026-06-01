import time


def monitoring_agent(state):

    state["execution_path"].append(
        "monitoring"
    )

    state["monitoring"] = {

        "timestamp": time.time(),

        "workflow_status": "success",

        "agents_executed":
            state["execution_path"]
    }

    return state
import time
from app.monitoring.logger import log_event


def monitoring_agent(state):

    state["execution_path"].append("monitoring")

    # Calculate end-to-end latency
    latency = round(time.time() - state.get("start_time", time.time()), 2)
    had_error = bool(state.get("error"))

    monitoring_data = {
        "timestamp":        time.time(),
        "workflow_status":  "error" if had_error else "success",
        "agents_executed":  list(state["execution_path"]),
        "latency_seconds":  latency,
        "retry_count":      state.get("retry_count", 0),
        "category":         state.get("category", "Unknown"),
        "sources_used":     state.get("sources", []),
        "need_tool":        state.get("need_tool", False),
        "error":            state.get("error", ""),
    }

    state["monitoring"] = monitoring_data

    # Persist to logs/execution.json (logger.py finally activated)
    log_event({
        "query": state["query"],
        **monitoring_data
    })

    return state
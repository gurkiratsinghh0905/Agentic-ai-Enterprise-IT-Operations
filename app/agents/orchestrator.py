from app.workflows.state import AgentState


def orchestrator_agent(state: AgentState):

    query = state["query"].lower()

    state["execution_path"].append("orchestrator")

    keywords = [
        "vpn",
        "password",
        "outlook",
        "mfa",
        "software",
        "network",
        "device",
        "access",
    ]

    if any(word in query for word in keywords):
        state["route"] = "retrieve"
    else:
        state["route"] = "direct"

    return state
from app.tools.system_status_tool import get_system_status
from app.tools.ticket_tool import create_ticket
from app.tools.asset_tool import asset_lookup
from app.tools.software_tool import software_lookup


def tool_agent(state):

    state["execution_path"].append("tool")
    results = {}
    category = state.get("category", "General").lower()

    try:
        # Always check system status when tools are needed
        results["system_status"] = get_system_status.invoke({})

        # Always create a support ticket for traceability
        results["ticket"] = create_ticket.invoke({"issue": state["query"]})

        # Category-specific tool calls
        if "software" in category:
            # Extract first known software name from query
            known_apps = ["zoom", "teams", "chrome", "slack", "vscode"]
            query_lower = state["query"].lower()
            matched = next((app for app in known_apps if app in query_lower), "unknown")
            results["software_check"] = software_lookup.invoke({"name": matched})

        if "device" in category or "asset" in category:
            # Extract user identifier — fallback to "current_user"
            results["asset_info"] = asset_lookup.invoke({"user": "current_user"})

        state["tool_results"] = results
        state["error"] = ""

    except Exception as e:
        state["error"] = f"Tool execution failed: {str(e)}"
        state["retry_count"] = state.get("retry_count", 0) + 1

    return state
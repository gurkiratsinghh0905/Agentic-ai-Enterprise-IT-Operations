from app.tools.system_status_tool import (
    get_system_status
)

from app.tools.ticket_tool import (
    create_ticket
)


def tool_agent(state):

    state["execution_path"].append(
        "tool"
    )

    status = get_system_status()

    ticket = create_ticket(
        state["query"]
    )

    state["tool_results"] = {

        "system_status": status,

        "ticket": ticket
    }

    return state
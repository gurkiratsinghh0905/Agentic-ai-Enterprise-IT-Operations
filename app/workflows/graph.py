from langgraph.graph import StateGraph
from langgraph.graph import END

from app.workflows.state import AgentState

from app.agents.orchestrator import orchestrator_agent
from app.agents.retrieval_agent import retrieval_agent
from app.agents.diagnostic_agent import diagnostic_agent
from app.agents.tool_agent import tool_agent
from app.agents.resolution_agent import resolution_agent
from app.agents.response_agent import response_agent
from app.agents.monitoring_agent import monitoring_agent


builder = StateGraph(AgentState)

builder.add_node(
    "orchestrator",
    orchestrator_agent
)

builder.add_node(
    "retrieval",
    retrieval_agent
)

builder.add_node(
    "diagnostic",
    diagnostic_agent
)

builder.add_node(
    "tool",
    tool_agent
)

builder.add_node(
    "resolution",
    resolution_agent
)

builder.add_node(
    "response",
    response_agent
)

builder.add_node(
    "monitoring",
    monitoring_agent
)

builder.set_entry_point(
    "orchestrator"
)

builder.add_edge(
    "orchestrator",
    "retrieval"
)

builder.add_edge(
    "retrieval",
    "diagnostic"
)


def route_tools(state):

    if state["need_tool"]:
        return "tool"

    return "resolution"


builder.add_conditional_edges(
    "diagnostic",
    route_tools,
    {
        "tool": "tool",
        "resolution": "resolution"
    }
)

builder.add_edge(
    "tool",
    "resolution"
)

builder.add_edge(
    "resolution",
    "response"
)

builder.add_edge(
    "response",
    "monitoring"
)

builder.add_edge(
    "monitoring",
    END
)

graph = builder.compile()
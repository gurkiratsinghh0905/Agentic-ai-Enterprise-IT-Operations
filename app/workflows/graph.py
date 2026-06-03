from langgraph.graph import StateGraph, END

from app.workflows.state import AgentState
from app.agents.orchestrator import orchestrator_agent
from app.agents.retrieval_agent import retrieval_agent
from app.agents.diagnostic_agent import diagnostic_agent
from app.agents.tool_agent import tool_agent
from app.agents.resolution_agent import resolution_agent
from app.agents.response_agent import response_agent
from app.agents.monitoring_agent import monitoring_agent


builder = StateGraph(AgentState)

# Register all nodes
builder.add_node("orchestrator", orchestrator_agent)
builder.add_node("retrieval",    retrieval_agent)
builder.add_node("diagnostic",   diagnostic_agent)
builder.add_node("tool",         tool_agent)
builder.add_node("resolution",   resolution_agent)
builder.add_node("response",     response_agent)
builder.add_node("monitoring",   monitoring_agent)

# Entry point
builder.set_entry_point("orchestrator")

# Fixed edges
builder.add_edge("orchestrator", "retrieval")
builder.add_edge("retrieval",    "diagnostic")


# --- Conditional Edge 1: After Diagnostic ---
# Does this issue need tool execution?
def route_after_diagnostic(state):
    if state.get("need_tool"):
        return "tool"
    return "resolution"

builder.add_conditional_edges(
    "diagnostic",
    route_after_diagnostic,
    {
        "tool":       "tool",
        "resolution": "resolution"
    }
)


# --- Conditional Edge 2: After Tool Agent ---
# Did the tool succeed? If not and retries remain, retry. Otherwise proceed.
def route_after_tool(state):
    if state.get("error") and state.get("retry_count", 0) < 2:
        return "tool"       # retry the tool agent
    return "resolution"     # proceed to resolution regardless

builder.add_conditional_edges(
    "tool",
    route_after_tool,
    {
        "tool":       "tool",
        "resolution": "resolution"
    }
)

# Fixed terminal edges
builder.add_edge("resolution",  "response")
builder.add_edge("response",    "monitoring")
builder.add_edge("monitoring",  END)

graph = builder.compile()
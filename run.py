from app.workflows.graph import graph


initial_state = {

    "query":
    "VPN not connecting",

    "retrieved_docs": [],

    "diagnosis": "",

    "tool_results": {},

    "resolution": "",

    "response": "",

    "execution_path": [],

    "monitoring": {},

    "need_tool": False,

    "route": "",

    "error": ""
}


result = graph.invoke(
    initial_state
)

print(
    result["response"]
)
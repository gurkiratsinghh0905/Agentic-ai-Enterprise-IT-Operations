import sys
sys.stdout.reconfigure(encoding="utf-8")

from app.workflows.graph import graph


initial_state = {
    "query":           "VPN not connecting",
    "rewritten_query": "",
    "retrieved_docs":  [],
    "sources":         [],
    "diagnosis":       "",
    "category":        "",
    "tool_results":    {},
    "resolution":      "",
    "response":        "",
    "execution_path":  [],
    "monitoring":      {},
    "need_tool":       False,
    "route":           "",
    "retry_count":     0,
    "error":           "",
    "start_time":      0.0,
}


result = graph.invoke(initial_state)

print(result["response"])
print("\n--- Monitoring ---")
print(result["monitoring"])
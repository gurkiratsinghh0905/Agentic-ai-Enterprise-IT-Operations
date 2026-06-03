import time
from app.llm import invoke
from app.workflows.state import AgentState


ORCHESTRATOR_SYSTEM = """You are an IT support ticket router for an enterprise helpdesk.
Your job is to classify the user query into exactly one of these categories:
VPN, Password, Email, MFA, Software, Network, Device, Access, General

Respond in this EXACT format with no extra text or explanation:
CATEGORY: <category>
NEEDS_RETRIEVAL: YES or NO
"""


def orchestrator_agent(state: AgentState) -> AgentState:

    state["execution_path"].append("orchestrator")
    state["start_time"] = time.time()

    prompt = f"Classify this IT support query:\n\n{state['query']}"

    response = invoke(
        prompt,
        system_prompt=ORCHESTRATOR_SYSTEM,
        max_tokens=60
    )

    # Parse structured response with safe fallbacks
    category = "General"
    needs_retrieval = True

    for line in response.splitlines():
        line = line.strip()
        if line.upper().startswith("CATEGORY:"):
            category = line.split(":", 1)[1].strip().title()
        elif line.upper().startswith("NEEDS_RETRIEVAL:"):
            needs_retrieval = "YES" in line.upper()

    # Fallback: if LLM errored, still set sensible defaults
    if "LLM_ERROR" in response:
        category = "General"
        needs_retrieval = True

    state["category"] = category
    state["route"] = "retrieve" if needs_retrieval else "direct"
    state["rewritten_query"] = state["query"]   # no rewrite — use original

    return state
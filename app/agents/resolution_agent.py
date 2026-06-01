from app.llm import invoke


def resolution_agent(state):

    state["execution_path"].append(
        "resolution"
    )

    prompt = f"""
User Query:
{state['query']}

Diagnosis:
{state['diagnosis']}

Tool Results:
{state['tool_results']}

Retrieved Context:
{state['retrieved_docs']}

Generate a detailed IT resolution.
"""

    state["resolution"] = invoke(
        prompt
    )

    return state
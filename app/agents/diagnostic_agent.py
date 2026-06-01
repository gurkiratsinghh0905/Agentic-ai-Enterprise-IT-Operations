from app.llm import invoke


def diagnostic_agent(state):

    state["execution_path"].append(
        "diagnostic"
    )

    prompt = f"""
You are an enterprise IT support expert.

User Query:
{state['query']}

Retrieved Context:
{state['retrieved_docs']}

Provide:

1. Category
2. Root Cause
3. Need Tool (YES/NO)
4. Confidence Score
"""

    diagnosis = invoke(prompt)

    state["diagnosis"] = diagnosis

    if "YES" in diagnosis.upper():

        state["need_tool"] = True

    else:

        state["need_tool"] = False

    return state
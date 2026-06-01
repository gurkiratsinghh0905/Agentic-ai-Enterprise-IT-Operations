def response_agent(state):

    state["execution_path"].append(
        "response"
    )

    state["response"] = f"""
# Diagnosis

{state['diagnosis']}

# Resolution

{state['resolution']}
"""

    return state
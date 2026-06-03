from app.llm import invoke


RESOLUTION_SYSTEM = """You are a senior IT support engineer writing a resolution guide for an end user.
Be specific, clear, and actionable. Use numbered steps.
Reference the provided knowledge base context where relevant.
End with escalation criteria if the issue may require further support."""


def resolution_agent(state):

    state["execution_path"].append("resolution")

    # Clean text context — no raw Document objects
    context_chunks = state.get("retrieved_docs", [])
    context = "\n\n---\n".join(context_chunks) if context_chunks else "No retrieved context."

    sources = ", ".join(state.get("sources", [])) or "internal knowledge base"
    tool_info = state.get("tool_results", {})
    error_note = ""
    if state.get("error"):
        error_note = f"\n\nNote: Tool execution encountered an error: {state['error']}. Provide resolution based on available context only."

    prompt = f"""Write a clear, numbered, step-by-step IT resolution for this issue.

User Query: {state['query']}

Diagnosis Summary:
{state['diagnosis']}

System Tool Results:
{tool_info}{error_note}

Knowledge Base Context (Sources: {sources}):
{context}

Provide numbered resolution steps. End with escalation criteria if needed."""

    state["resolution"] = invoke(
        prompt,
        system_prompt=RESOLUTION_SYSTEM,
        max_tokens=800
    )

    return state
from app.llm import invoke


DIAGNOSTIC_SYSTEM = """You are a senior IT support engineer performing root cause analysis.
Always respond using this EXACT format with no extra commentary before or after:

CATEGORY: <category name>
ROOT_CAUSE: <one sentence root cause>
NEED_TOOL: YES or NO
CONFIDENCE: <number 1-100>
ANALYSIS: <2-3 sentence detailed analysis>
"""


def diagnostic_agent(state):

    state["execution_path"].append("diagnostic")

    # Inject clean text context (not raw Document objects)
    context = "\n\n---\n".join(state["retrieved_docs"]) if state["retrieved_docs"] else "No context retrieved."

    prompt = f"""Analyze this IT support issue and provide a structured diagnosis.

User Query: {state['query']}
Detected Category: {state.get('category', 'Unknown')}

Knowledge Base Context:
{context}

Provide your structured diagnosis:"""

    diagnosis = invoke(prompt, system_prompt=DIAGNOSTIC_SYSTEM, max_tokens=300)
    state["diagnosis"] = diagnosis

    # Robust tool detection — handles multiple LLM output variations
    diag_upper = diagnosis.upper()
    state["need_tool"] = (
        "NEED_TOOL: YES" in diag_upper
        or "NEED_TOOL:YES" in diag_upper
        or ("NEED_TOOL" in diag_upper and "YES" in diag_upper)
    )

    return state
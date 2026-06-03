import os
from app.rag.retriever import get_retriever


def retrieval_agent(state):

    state["execution_path"].append("retrieval")

    retriever = get_retriever()

    # Use original query (no rewriting as per project scope)
    docs = retriever.invoke(state["query"])

    # Extract clean text strings and source filenames
    clean_docs = []
    sources = []

    for doc in docs:
        clean_docs.append(doc.page_content)
        src = doc.metadata.get("source", "unknown")
        sources.append(os.path.basename(src))

    # Deduplicate sources while preserving order
    seen = set()
    unique_sources = []
    for s in sources:
        if s not in seen:
            seen.add(s)
            unique_sources.append(s)

    state["retrieved_docs"] = clean_docs      # list of plain strings
    state["sources"] = unique_sources         # deduplicated source filenames

    return state

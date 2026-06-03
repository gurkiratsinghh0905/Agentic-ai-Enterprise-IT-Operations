from app.rag.retriever import (
    get_retriever
)


def retrieval_agent(state):

    state["execution_path"].append(
        "retrieval"
    )

    retriever = get_retriever()

    docs = retriever.invoke(
        state["query"]
    )

    state["retrieved_docs"] = docs

    return state

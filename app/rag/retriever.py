from langchain_chroma import Chroma
from app.rag.embeddings import get_embedding_model


def get_retriever():

    db = Chroma(
        persist_directory="chroma_db",
        embedding_function=get_embedding_model()
    )

    # MMR (Maximal Marginal Relevance) — balances relevance + diversity
    # fetch_k=10: fetches 10 candidates, then picks k=4 most diverse
    return db.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k":       4,
            "fetch_k": 10
        }
    )
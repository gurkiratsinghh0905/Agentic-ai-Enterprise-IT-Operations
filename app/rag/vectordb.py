from langchain_chroma import Chroma

from app.rag.embeddings import (
    get_embedding_model
)


def create_db(chunks):

    db = Chroma.from_documents(
        documents=chunks,
        embedding=get_embedding_model(),
        persist_directory="chroma_db"
    )

    return db
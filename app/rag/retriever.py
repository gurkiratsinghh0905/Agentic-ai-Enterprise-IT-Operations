from langchain_chroma import Chroma

from embeddings import get_embedding_model

def get_retriever():

    db = Chroma(
        persist_directory="chroma_db",
        embedding_function=get_embedding_model()
    )

    return db.as_retriever(
        search_kwargs={"k":3}
    )
from app.rag.loader import load_docs
from app.rag.chunker import split_docs
from app.rag.vectordb import create_db


def ingest():

    docs = load_docs()

    chunks = split_docs(
        docs
    )

    create_db(
        chunks
    )

    print(
        f"Successfully created {len(chunks)} chunks"
    )


if __name__ == "__main__":
    ingest()
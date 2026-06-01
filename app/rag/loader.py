from langchain_community.document_loaders import DirectoryLoader

def load_docs():

    loader = DirectoryLoader(
        "knowledge_base"
    )

    docs = loader.load()

    return docs
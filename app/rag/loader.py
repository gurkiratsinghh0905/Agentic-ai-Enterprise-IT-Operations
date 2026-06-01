from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import TextLoader


def load_docs():

    loader = DirectoryLoader(
        "knowledge_base",
        glob="**/*.md",
        loader_cls=TextLoader
    )

    docs = loader.load()

    return docs
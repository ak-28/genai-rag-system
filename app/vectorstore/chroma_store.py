from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings


EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
PERSIST_DIRECTORY = "vector_db/chroma"


embedding_model = HuggingFaceEmbeddings(
    model_name=EMBEDDING_MODEL
)



def create_vector_store(chunks):
    """
    Create and persist Chroma vector database.
    """

    vector_db = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=PERSIST_DIRECTORY
    )

    return vector_db



def load_vector_store():
    """
    Load existing Chroma DB.
    """

    vector_db = Chroma(
        persist_directory=PERSIST_DIRECTORY,
        embedding_function=embedding_model
    )

    return vector_db
from langchain_community.document_loaders import PyPDFLoader


def load_pdf(pdf_path: str):
    """
    Load PDF and return LangChain documents.
    """

    loader = PyPDFLoader(pdf_path)
    docs = loader.load()

    return docs
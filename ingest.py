from app.ingestion.loader import load_pdfs
from app.ingestion.splitter import split_documents
from app.vectorstore.chroma_store import create_vector_store


DATA_PATH = "data/raw/"


def main():

    print("\nLoading PDFs...")
    documents = load_pdfs(DATA_PATH)

    print(f"Loaded {len(documents)} pages")

    print("\nSplitting documents...")
    chunks = split_documents(documents)

    print(f"Created {len(chunks)} chunks")

    print("\nCreating vector database...")
    create_vector_store(chunks)

    print("\nVector database created successfully")


if __name__ == "__main__":
    main()
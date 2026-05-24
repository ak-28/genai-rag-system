from app.ingestion.loader import load_pdf
from app.ingestion.splitter import split_documents
from app.vectorstore.chroma_store import create_vector_store


PDF_PATH = "data/raw/attention_is_all_you_need.pdf"


print("Loading PDF...")
docs = load_pdf(PDF_PATH)

print(f"Loaded {len(docs)} pages")


print("Splitting documents...")
chunks = split_documents(docs)

print(f"Created {len(chunks)} chunks")


print("Creating vector database...")
create_vector_store(chunks)

print("Vector DB created successfully")
from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader

PROJECT_ROOT = Path(__file__).resolve().parents[2]

def load_pdfs(folder_path: str):
    """
    Load mulitple PDF's and return LangChain documents.
    """
    
    folder_path = PROJECT_ROOT/folder_path
    
    pdf_files = Path(folder_path).glob("*.pdf")
    documents = []
    
    
    for pdf_file in pdf_files:
        print(f"Loading: {pdf_file.name}")
        
        
        loader = PyPDFLoader(str(pdf_file))
        docs = loader.load()
        
        for doc in docs:
            doc.metadata["source"] = pdf_file.name
            
        documents.extend(docs)
    return documents
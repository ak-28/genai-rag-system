# GenAI RAG System — V2 Multi-Document RAG Chatbot

A local Retrieval-Augmented Generation (RAG) chatbot capable of searching across multiple PDF documents using:

- Ollama
- LangChain
- ChromaDB
- Streamlit
- Sentence Transformers

This version upgrades the V1 single-document chatbot into a persistent multi-document semantic knowledge system.

---

# Features

## V2 Enhancements

- Multi-PDF ingestion
- Persistent vector database
- Metadata-aware retrieval
- Source citations
- Cross-document semantic search
- Retrieved chunk inspection
- Modular RAG architecture
- Fully local inference using Ollama

---

# Tech Stack

| Component | Tool |
|---|---|
| LLM | Ollama + Phi3 |
| Framework | LangChain |
| Vector DB | ChromaDB |
| Embeddings | sentence-transformers |
| UI | Streamlit |
| Environment | uv |
| Runtime | WSL2 Ubuntu |

---

# What is RAG?

RAG stands for:

```text
Retrieval-Augmented Generation
```

Instead of relying only on an LLM’s internal knowledge, RAG:

1. retrieves relevant information
2. injects retrieved context into prompts
3. generates grounded responses

This significantly reduces hallucinations and enables document-aware question answering.

---

# V2 Architecture

```text
                    ┌────────────────────┐
                    │   Multiple PDFs    │
                    └─────────┬──────────┘
                              │
                              ▼
                    ┌────────────────────┐
                    │     Ingestion      │
                    └─────────┬──────────┘
                              │
                              ▼
                    ┌────────────────────┐
                    │      Chunking      │
                    └─────────┬──────────┘
                              │
                              ▼
                    ┌────────────────────┐
                    │     Embeddings     │
                    └─────────┬──────────┘
                              │
                              ▼
                    ┌────────────────────┐
                    │      ChromaDB      │
                    │  Persistent Store  │
                    └─────────┬──────────┘
                              │
                              ▼
                    ┌────────────────────┐
                    │     Retrieval      │
                    └─────────┬──────────┘
                              │
                              ▼
                    ┌────────────────────┐
                    │      Ollama        │
                    └─────────┬──────────┘
                              │
                              ▼
                    ┌────────────────────┐
                    │ Answer + Citations │
                    └────────────────────┘
```

---

# Project Structure

```text
genai-rag-system/
│
├── app/
│   ├── __init__.py
│   │
│   ├── ingestion/
│   │   ├── __init__.py
│   │   ├── loader.py
│   │   └── splitter.py
│   │
│   ├── vectorstore/
│   │   ├── __init__.py
│   │   ├── chroma_store.py
│   │   └── retriever.py
│   │
│   ├── llm/
│   │   ├── __init__.py
│   │   └── ollama_client.py
│   │
│   ├── prompts/
│   │   ├── __init__.py
│   │   └── rag_prompt.py
│   │
│   └── chains/
│       ├── __init__.py
│       └── rag_chain.py
│
├── data/
│   └── raw/
│       ├── attention.pdf
│       ├── rag.pdf
│       └── bert.pdf
│
├── ui/
│   └── streamlit_app.py
│
├── vector_db/
│   └── chroma/
│
├── ingest.py
├── pyproject.toml
├── uv.lock
├── README.md
└── .gitignore
```

---

# Core RAG Pipeline

```text
Documents
 ↓
Chunking
 ↓
Embeddings
 ↓
Vector Storage
 ↓
Similarity Search
 ↓
Retrieved Context
 ↓
LLM Generation
 ↓
Answer
```

---

# Step-by-Step System Flow

---

# 1. Multi-Document Ingestion

File:

```text
app/ingestion/loader.py
```

All PDFs inside:

```text
data/raw/
```

are automatically loaded.

Example:

```text
data/raw/
├── transformer.pdf
├── bert.pdf
├── rag.pdf
```

Each document becomes LangChain `Document` objects.

---

# 2. Chunking

File:

```text
app/ingestion/splitter.py
```

Documents are split using:

```python
RecursiveCharacterTextSplitter
```

Configuration:

```python
chunk_size=1000
chunk_overlap=200
```

Why chunking matters:
- improves retrieval precision
- avoids context overflow
- enables semantic search

---

# 3. Metadata Preservation

Each chunk stores metadata:

```python
{
   "source": "transformer.pdf",
   "page": 4
}
```

This enables:
- citations
- source tracking
- future filtering

---

# 4. Embeddings

File:

```text
app/vectorstore/chroma_store.py
```

Embedding model:

```text
sentence-transformers/all-MiniLM-L6-v2
```

Each chunk becomes a dense vector.

Example:

```text
"The Transformer uses self-attention"
 ↓
[0.12, -0.88, 0.44, ...]
```

---

# 5. Persistent ChromaDB

Embeddings are stored in:

```text
vector_db/chroma/
```

ChromaDB handles:
- vector storage
- ANN indexing
- similarity search
- persistence

The database persists across application restarts.

---

# 6. Retrieval

When a user asks a question:

```text
"What is self-attention?"
```

the system:
1. embeds the query
2. searches vector DB
3. retrieves top-k similar chunks

Retrieval uses:
- dense embeddings
- cosine similarity
- HNSW ANN indexing

---

# 7. Generation

Retrieved chunks are inserted into prompts:

```text
Context
+
Question
↓
LLM
↓
Answer
```

The LLM generates grounded responses using retrieved context.

---

# 8. Source Citations

V2 introduces citations:

```text
Sources:
- transformer.pdf (Page 4)
- rag.pdf (Page 2)
```

This improves:
- trustworthiness
- explainability
- debugging

---

# Environment Setup Using uv

---

# 1. Install uv

Official docs:

https://docs.astral.sh/uv/

Install:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

---

# 2. Create Virtual Environment

```bash
uv venv
```

Activate:

```bash
source .venv/bin/activate
```

---

# 3. Install Dependencies

```bash
uv sync
```

---

# 4. Pull Ollama Model

Install Ollama:

https://ollama.com

Then pull model:

```bash
ollama pull phi3
```

---

# Running the Project

---

# Step 1 — Add PDFs

Place PDFs inside:

```text
data/raw/
```

---

# Step 2 — Build Vector Database

```bash
python ingest.py
```

This performs:
- document ingestion
- chunking
- embedding generation
- vector DB persistence

---

# Step 3 — Start Streamlit App

```bash
PYTHONPATH=. streamlit run ui/streamlit_app.py
```

---

# Example Questions

```text
What is self-attention?
Explain the Transformer architecture.
How does BERT differ from Transformers?
Summarize retrieval-augmented generation.
```

---

# Retrieval Flow

```text
User Question
 ↓
Query Embedding
 ↓
Similarity Search
 ↓
Top-k Chunks
 ↓
Prompt Construction
 ↓
Ollama
 ↓
Answer + Sources
```

---

# Persistent Vector Database

The Chroma database persists locally:

```text
vector_db/chroma/
```

Benefits:
- faster startup
- reusable embeddings
- scalable ingestion pipeline

---

# Important Concepts Learned in V2

| Concept | Description |
|---|---|
| Multi-document retrieval | Cross-document semantic search |
| Metadata-aware RAG | Source-aware retrieval |
| Persistent vector DBs | Reusable semantic storage |
| ANN indexing | Efficient vector search |
| Modular architecture | Clean separation of concerns |
| Retrieval debugging | Chunk inspection |

---

# V1 vs V2

| Feature | V1 | V2 |
|---|---|---|
| PDFs | Single | Multiple |
| Metadata | Minimal | Rich metadata |
| Citations | No | Yes |
| Retrieval | Basic | Cross-document |
| Persistence | Basic | Structured |
| Knowledge Base | One file | Multi-document system |

---

# Current Limitations

This version does NOT yet include:
- chat memory
- reranking
- hybrid retrieval
- FastAPI backend
- Docker deployment
- authentication
- evaluation framework
- agentic workflows

These are planned for future versions.

---

# Planned Future Improvements

- Hybrid search
- Rerankers
- Conversational memory
- Multi-user support
- FastAPI backend
- Docker deployment
- PostgreSQL + pgvector
- Production deployment
- Evaluation pipelines

---

# Key Learning Outcome

This project demonstrates a production-style local multi-document RAG architecture:

```text
Documents
 ↓
Embeddings
 ↓
Semantic Retrieval
 ↓
Grounded Generation
```

and forms the foundation for advanced GenAI systems.
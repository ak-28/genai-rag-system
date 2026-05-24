# GenAI RAG System — V1 PDF Chatbot

A simple local Retrieval-Augmented Generation (RAG) chatbot built using:

- Ollama
- LangChain
- ChromaDB
- Streamlit
- Sentence Transformers

This project demonstrates the complete V1 RAG pipeline:

```text
PDF
 ↓
Chunking
 ↓
Embeddings
 ↓
Vector Database
 ↓
Retrieval
 ↓
LLM Generation
 ↓
Answer
```

---

# Features

- PDF ingestion
- Recursive text chunking
- Dense embeddings
- Chroma vector database
- Semantic similarity search
- Local LLM inference using Ollama
- Streamlit chat interface
- Fully local RAG pipeline

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
| OS | WSL2 Ubuntu |

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
│   │   └── chroma_store.py
│   │
│   ├── llm/
│   │   ├── __init__.py
│   │   └── ollama_client.py
│   │
│   └── chains/
│       ├── __init__.py
│       └── rag_chain.py
│
├── data/
│   └── raw/
│       └── attention_is_all_you_need.pdf
│
├── ui/
│   └── streamlit_app.py
│
├── vector_db/
│
├── ingest.py
├── pyproject.toml
├── uv.lock
├── README.md
└── .gitignore
```

---

# What is RAG?

RAG stands for:

```text
Retrieval-Augmented Generation
```

Instead of relying only on an LLM’s internal knowledge, RAG:

1. retrieves relevant information
2. injects it into the prompt
3. generates grounded answers

This reduces hallucinations and enables question-answering over custom documents.

---

# V1 Architecture

```text
                    ┌──────────────────┐
                    │      PDF         │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │    Ingestion     │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │    Chunking      │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │   Embeddings     │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │    ChromaDB      │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │    Retrieval     │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │     Ollama       │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │     Answer       │
                    └──────────────────┘
```

---

# Step-by-Step Process

---

# 1. PDF Ingestion

File:

```text
app/ingestion/loader.py
```

The PDF is loaded using:

```python
PyPDFLoader
```

This converts the PDF into LangChain `Document` objects.

Each document contains:
- page content
- metadata

Example:

```python
Document(
    page_content="Transformers use attention...",
    metadata={"page": 0}
)
```

---

# 2. Chunking

File:

```text
app/ingestion/splitter.py
```

The document is split into smaller chunks using:

```python
RecursiveCharacterTextSplitter
```

Configuration:

```python
chunk_size=1000
chunk_overlap=200
```

Why chunking is needed:
- improves retrieval quality
- reduces context overload
- enables semantic search

---

# 3. Embeddings

File:

```text
app/vectorstore/chroma_store.py
```

Each chunk is converted into a dense vector using:

```python
sentence-transformers/all-MiniLM-L6-v2
```

Example:

```text
"The Transformer uses self-attention"
 ↓
[0.12, -0.77, 0.44, ...]
```

These vectors capture semantic meaning.

---

# 4. Vector Database

The embeddings are stored in:

```text
ChromaDB
```

Chroma automatically:
- stores embeddings
- builds vector indexes
- enables similarity search

The vector DB is persisted locally:

```text
vector_db/chroma/
```

---

# 5. Retrieval

When a user asks a question:

```text
"What is self-attention?"
```

the query is:
1. converted into an embedding
2. compared against stored vectors
3. top-k similar chunks are retrieved

Similarity search uses:
- dense vectors
- cosine similarity
- ANN indexing (HNSW)

---

# 6. Generation

File:

```text
app/chains/rag_chain.py
```

Retrieved chunks are combined into a prompt:

```text
Context
+
Question
↓
LLM
↓
Answer
```

The LLM generates grounded responses using the retrieved context.

---

# 7. Ollama

Local LLM inference is handled using:

```text
Ollama
```

Model used:

```text
phi3
```

Why Phi3?
- lightweight
- good for low VRAM GPUs
- fast local inference

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

Install Ollama first:

https://ollama.com

Then pull model:

```bash
ollama pull phi3
```

---

# Running the Project

---

# Step 1 — Ingest PDF

```bash
python ingest.py
```

This performs:
- loading
- chunking
- embedding generation
- vector DB creation

---

# Step 2 — Start Streamlit App

```bash
PYTHONPATH=. streamlit run ui/streamlit_app.py
```

---

# Step 3 — Ask Questions

Examples:

```text
What is self-attention?
Summarize the transformer architecture.
What are the key contributions of the paper?
```

---

# Retrieval Flow

```text
Question
 ↓
Embedding
 ↓
Similarity Search
 ↓
Top-k Chunks
 ↓
Prompt Construction
 ↓
LLM
 ↓
Answer
```

---

# Important Concepts Learned in V1

This project covers the core fundamentals of RAG systems:

| Concept | Description |
|---|---|
| Ingestion | Load documents |
| Chunking | Split large text |
| Embeddings | Semantic vector representation |
| Vector DB | Store/search vectors |
| Retrieval | Fetch relevant chunks |
| Generation | Produce grounded answers |
| Local LLMs | Offline inference |

---

# Current Limitations (V1)

This version does NOT include:
- multi-document support
- chat memory
- reranking
- hybrid retrieval
- metadata filtering
- FastAPI backend
- authentication
- evaluation pipelines

These will be added in future versions.

---

# Future Improvements

Planned upgrades:

- Multi-PDF support
- Conversational memory
- Hybrid search
- Reranking
- FastAPI backend
- Docker deployment
- Agentic RAG workflows
- Evaluation metrics

---

# Key Learning Outcome

This project demonstrates the complete lifecycle of a basic local RAG application:

```text
Document → Retrieval → Generation
```

and serves as the foundation for advanced GenAI systems.
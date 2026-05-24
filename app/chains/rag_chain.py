from app.vectorstore.chroma_store import load_vector_store
from app.llm.ollama_client import generate_response


vector_db = load_vector_store()



def ask_question(query: str, k: int = 3):
    """
    Complete RAG pipeline.
    """

    # Retrieval
    results = vector_db.similarity_search(query, k=k)

    # Build context
    context = "\n\n".join(
        [result.page_content for result in results]
    )

    # Prompt
    prompt = f"""
You are a helpful AI assistant.

Answer the question using ONLY the provided context.

If the answer is not available in the context,
say:
"I could not find the answer in the document."

Context:
{context}

Question:
{query}
"""

    # Generation
    answer = generate_response(prompt)

    return {
        "answer": answer,
        "sources": results
    }
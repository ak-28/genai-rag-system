import streamlit as st

from app.chains.rag_chain import ask_question


st.set_page_config(
    page_title="GenAI RAG System",
    layout="wide"
)


st.title("📚 Multi-Document RAG Chatbot")


st.markdown(
    """
    Ask questions across multiple PDFs using:
    - LangChain
    - ChromaDB
    - Ollama
    - Semantic Retrieval
    """
)


query = st.text_input(
    "Ask a question"
)


if query:

    with st.spinner("Retrieving answer..."):

        response = ask_question(query)

        # Answer
        st.subheader("Answer")
        st.write(response["answer"])

        # Sources
        st.subheader("Sources")

        unique_sources = set()

        for source in response["sources"]:

            source_name = source.metadata.get("source", "Unknown")
            page_number = source.metadata.get("page", "N/A")

            source_key = (source_name, page_number)

            if source_key not in unique_sources:

                unique_sources.add(source_key)

                st.write(
                    f"- {source_name} (Page {page_number})"
                )

        # Retrieved chunks
        st.subheader("Retrieved Chunks")

        for i, source in enumerate(response["sources"]):

            with st.expander(f"Chunk {i+1}"):

                st.write(source.page_content)

                st.caption(
                    f"Source: {source.metadata.get('source')} | "
                    f"Page: {source.metadata.get('page')}"
                )
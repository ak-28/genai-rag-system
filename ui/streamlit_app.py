import streamlit as st

from app.chains.rag_chain import ask_question


st.set_page_config(
    page_title="PDF RAG Chatbot",
    layout="wide"
)


st.title("📄 PDF RAG Chatbot")


query = st.text_input(
    "Ask a question about the PDF"
)


if query:

    with st.spinner("Thinking..."):

        response = ask_question(query)

        st.subheader("Answer")
        st.write(response["answer"])

        st.subheader("Retrieved Chunks")

        for i, source in enumerate(response["sources"]):
            with st.expander(f"Chunk {i+1}"):
                st.write(source.page_content)
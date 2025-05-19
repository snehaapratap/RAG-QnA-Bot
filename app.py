# app.py
import streamlit as st
from chatbot import ask_question

st.set_page_config(page_title="RAG Chatbot")
st.title("📚 RAG-based Chatbot")

st.markdown("""
**Note:** Ensure you have set your OpenAI API key in a `.env` file in the project root as `OPENAI_API_KEY=your-key-here`.
""")

query = st.text_input("Ask a question based on the document:")

if query:
    with st.spinner("Searching..."):
        try:
            answer = ask_question(query)
            st.success(answer)
        except Exception as e:
            st.error(f"Error: {e}")

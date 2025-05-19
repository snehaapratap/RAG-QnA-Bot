# app.py
import streamlit as st
from chatbot import ask_question

st.set_page_config(page_title="RAG Chatbot")
st.title("📚 RAG-based Chatbot")

query = st.text_input("Ask a question based on the document:")

if query:
    with st.spinner("Searching..."):
        answer = ask_question(query)
        st.success(answer)

# app.py
import streamlit as st
from chatbot import ask_question

st.set_page_config(page_title="RAG Chatbot")
st.title("📚 RAG-based Chatbot")

st.markdown("""
**Note:** Ensure you have set your Gemini API key in a `.env` file in the project root as `GEMINI_API_KEY=your-gemini-api-key-here`.
""")

# Initialize chat history in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display chat history
for i, (q, a) in enumerate(st.session_state.chat_history):
    st.markdown(f"**You:** {q}")
    st.markdown(f"<div style='background-color:#23422a;padding:12px;border-radius:8px;color:#fff;'>{a}</div>", unsafe_allow_html=True)

query = st.text_input("Ask a question based on the document:", key="input")

if st.button("Send"):
    if query:
        with st.spinner("Searching..."):
            try:
                answer = ask_question(query)
                st.session_state.chat_history.append((query, answer))
                st.rerun()
            except Exception as e:
                st.error(f"Error: {e}")

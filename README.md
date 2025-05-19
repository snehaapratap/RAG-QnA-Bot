# RAG-based Q&A Chatbot 🤖

A Retrieval-Augmented Generation (RAG) chatbot that uses Google Gemini and LangChain to answer user queries based on the contents of uploaded PDF documents.

> 🧠 Powered by Generative AI • ⚙️ Built with LangChain • 💬 Conversational AI with Retrieval

---

## 🚀 Features

- ✅ Retrieval-Augmented Generation (RAG) Pipeline
- 📄 Custom Knowledge Base from PDFs
- 💬 Conversational Chat UI with context-based answers
- 🔐 Gemini integration for LLM responses
- 📝 Sample Q&A Logs for Evaluation

---

## 📁 Project Structure

```

rag-qna-bot/
├── app.py                  # Streamlit app frontend
├── chatbot.py              # Core RAG logic with Gemini + LangChain
├── data/
│   └── meditations.pdf     # Sample knowledge base
├── responses.txt           # Sample Q\&A
├── requirements.txt        # Project dependencies
├── .env           # Environment variable template
└── README.md               # You're here!

````

---

## 🛠️ Setup Instructions

### 1. **Clone the Repository**
```bash
git clone https://github.com/snehaapratap/RAG-QnA-Bot.git
cd RAG-QnA-Bot
````

### 2. **Install Dependencies**

```bash
pip install -r requirements.txt
```

### 3. **Set Up Environment Variables**

Create a `.env` file in the root directory:

```
GEMINI_API_KEY=your-gemini-api-key-here
```

> 📌 Make sure your `.env` file is **not committed** to version control.

### 4. **Add Your Knowledge Base**

* Add your PDF(s) to the `data/` directory.
* Default file used: `data/meditations.pdf`

---

## ▶️ Running the App

To run the chatbot locally, use:

```bash
streamlit run app.py
```

Then open the provided URL (usually [http://localhost:8501](http://localhost:8501)) in your browser.

---

## 💬 Usage

* Type your question based on the document contents.
* The bot retrieves relevant context from the PDF using LangChain.
* Google Gemini generates a contextual, human-like answer.
* Chat history is preserved within the session.

---

## 📝 Sample Q\&A

Example questions and answers are stored in [`responses.txt`](responses.txt):

```
Q: What is the main message of the document?
A: The core message revolves around self-reflection and inner peace...
```

---

## 🔧 Customization

* **Change the PDF:** Replace `data/meditations.pdf` with your own document.
* **Multiple PDFs:** Extend `chatbot.py` to load and index multiple files.
* **UI Styling:** Modify `app.py` to adjust layout and visuals.

---

## 🛡️ Security

* Never expose your actual `.env` or Gemini API key.
* Use `.env.example` to share the required format with collaborators.

---

## 📦 Dependencies

```txt
streamlit
langchain
google-generativeai
unstructured
pdfminer.six
python-dotenv
```

Install them via:

```bash
pip install -r requirements.txt
```

---

## 🙌 Acknowledgements

* [LangChain](https://github.com/langchain-ai/langchain)
* [Google Gemini](https://ai.google.dev/)
* [Streamlit](https://streamlit.io/)

  
---

## ✨ Connect
For internship submission or queries : sneha.prem918@gmail.com


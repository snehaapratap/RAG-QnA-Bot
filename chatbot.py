# chatbot.py - Load and embed documents
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma

loader = PyPDFLoader("data/meditations.pdf")
docs = loader.load()

embeddings = OpenAIEmbeddings()
vectordb = Chroma.from_documents(docs, embedding=embeddings, persist_directory="db")
vectordb.persist()


# chatbot.py - RAG Chain
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=vectordb.as_retriever(),
    return_source_documents=True
)

def ask_question(query):
    response = qa_chain(query)
    return response["result"]

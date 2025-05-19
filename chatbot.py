# chatbot.py - Load and embed documents
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma

loader = PyPDFLoader("data/meditations.pdf")
docs = loader.load()

embeddings = OpenAIEmbeddings()
vectordb = Chroma.from_documents(docs, embedding=embeddings, persist_directory="db")
vectordb.persist()

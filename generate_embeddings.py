from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_huggingface import HuggingFaceEmbeddings
loaders = [
    PyPDFLoader('./AICS Device agreement  2025-26.pdf'),
    PyPDFLoader('./AICS_Academic_Integirity_Policy_March_2025.pdf'),
    PyPDFLoader('./Code_of_Conduct.pdf'),
    PyPDFLoader('./AICS_Assessment_Policy_2024__2_.pdf')
]

docs = []
for loader in loaders:
    docs.extend(loader.load())


text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
docs = text_splitter.split_documents(docs)
embedding_function = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2", model_kwargs={"device": "cpu"})

vectorstore = Chroma.from_documents(docs, embedding_function, persist_directory="./chroma_db_nccn")
print(vectorstore._collection.count())
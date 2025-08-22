# 📚 RAG PDF Assistant
A simple **Retrieval-Augmented Generation (RAG)** chatbot that answers questions using your own PDF documents. It combines **LangChain**, **HuggingFace embeddings**, **Chroma vector database**, and **Google Gemini** to provide accurate, context-aware answers.

## 🚀 Features
- Load and process multiple PDF documents (e.g. policies, agreements, reports).
- Split documents into smaller chunks for efficient retrieval.
- Generate embeddings using `sentence-transformers/all-MiniLM-L6-v2`.
- Store and query embeddings with **ChromaDB**.
- Answer questions in plain language with **Google Gemini**.
- If an answer is not found in the documents, the bot says it doesn’t know (no hallucinations).

## 🛠️ Tech Stack
- [LangChain](https://www.langchain.com/)  
- [HuggingFace Transformers](https://huggingface.co/)  
- [ChromaDB](https://www.trychroma.com/)  
- [Google Gemini API](https://ai.google.dev/)  

## 📂 Project Structure
1. rag_app.py # Main chatbot loop (asks questions and generates answers)
2. embed_pdfs.py # Script for loading & embedding PDFs
3. chroma_db_nccn/ # Persistent ChromaDB vector storage
4. docs/ # PDF documents (your own files go here)
5. README.md # Project documentation

## ⚙️ Installation
1. **Clone this repository**
   ```bash
   git clone https://github.com/yourusername/rag-pdf-assistant.git
   cd rag-pdf-assistant


⚠️ **Disclaimer**

This project is for educational purposes only.
Do not share or commit your real API keys to a public repository.

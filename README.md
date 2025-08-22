📚 **RAG-PDF Assistant**

RAG-PDF Assistant is a Retrieval-Augmented Generation (RAG) chatbot that answers questions using custom PDF documents. It combines LangChain, HuggingFace embeddings, Chroma vector database, and Google Gemini to provide accurate, context-aware answers.

In this example, the assistant is powered by a few school policy documents:

AICS Device agreement 2025-26.pdf

AICS_Academic_Integirity_Policy_March_2025.pdf

AICS_Assessment_Policy_2024__2_.pdf

Code_of_Conduct.pdf

You can swap out these files for any PDFs you like, making it easy to adapt the assistant to your own data.

🚀 **Features**

Loads multiple PDFs and splits them into manageable chunks.

Generates embeddings using HuggingFace sentence-transformers.

Stores and queries embeddings with ChromaDB.

Builds a context-aware prompt for Google Gemini.

Answers questions in plain language for non-technical users.

Avoids hallucinations by only responding based on document context.

🛠️ How It Works

PDF Loading and Embedding (embedding.py)

PDFs are loaded using PyPDFLoader.

Documents are split into smaller chunks for better retrieval using RecursiveCharacterTextSplitter.

Each chunk is converted into vector embeddings using HuggingFaceEmbeddings.

The embeddings are stored in a persistent ChromaDB vector database.

RAG Chatbot (rag.py)

User inputs a query.

The system searches the ChromaDB for the most relevant chunks of text.

A prompt is generated combining the query and context.

Google Gemini (gemini-2.0-flash) produces a natural-language answer.

The bot outputs the answer and waits for the next query.

⚙️ **Installation**

Clone the repository:

git clone https://github.com/yourusername/rag-pdf-assistant.git
cd rag-pdf-assistant


Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows


Install dependencies:

pip install -r requirements.txt


Set your Google API key as an environment variable:

export GOOGLE_API_KEY="your_api_key_here"   # macOS/Linux
set GOOGLE_API_KEY="your_api_key_here"      # Windows


⚠️ Do not commit your API key to GitHub.

▶️ **Usage**
Step 1: Generate embeddings
python embedding.py


This will load your PDFs, create embeddings, and store them in chroma_db_nccn/.

Step 2: Run the chatbot
python rag.py


Type your questions, and the assistant will respond using information from your PDFs.

📌 **Example**
Query: What is the school's academic integrity policy?
Answer: The academic integrity policy emphasizes honesty, responsibility, and fairness in all academic work...

📜 **Dependencies**
langchain
langchain-community
langchain-huggingface
langchain-chroma
chromadb
sentence-transformers
google-generativeai
PyPDF2

⚠️ **Disclaimer**

This project is for educational purposes only.
Do not share or commit your real API keys to a public repository.

📂 **Notes**

You can replace the provided PDFs with any documents you want.

The bot only answers based on the content of your PDFs; it will not invent answers.

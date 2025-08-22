import os
import signal
import sys
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
import google.generativeai as genai

API_KEY = Your API_KEY_HERE


def signal_handler(sig, frame):
    print("Exiting gracefully...")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)



def generate_rag_prompt(query, context):
    escaped = context.replace('"', "").replace("'", "").replace("\n", " ")
    prompt = ("You are a helpful and informative bot that answers questions using text from the reference context included below. Be sure to respond in a complete sentence, being comprehensive, inculuding all relevant information. However, you are talking to a non-techinical audience so be sure to use simple language. If the context does not contain the answer to the question, say that you do not know. Do not make up an answer."
              " QUESTION: '{query}'"
              " CONTEXT: '{context}'"
              " ANSWER: ").format(query=query, context=context)
    return prompt





def get_relevant_context(query):
    context = ""
    embedding_function = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2", model_kwargs={"device": "cpu"})
    vector_db = Chroma(persist_directory="./chroma_db_nccn", embedding_function=embedding_function)
    search_results = vector_db.similarity_search(query, k=6)
    for result in search_results:
        context += result.page_content + "\n"
    return context


def generate_answer(prompt): 
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(prompt)
    return response.text





while True:
    print("What would you like to ask?")
    query = input("Query: ")
    print(query)
    context = get_relevant_context(query)
    prompt = generate_rag_prompt(query=query, context = context)
    answer = generate_answer(prompt=prompt)
    print(answer)
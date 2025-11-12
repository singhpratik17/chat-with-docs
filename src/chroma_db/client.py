import chromadb
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma


def create_client():
    """Create a Chroma Client"""
    return chromadb.PersistentClient(path="./chroma_langchain_db")


def embeddings_generator(google_api_key):
    """Returns langchain Gemini embedding function"""
    return GoogleGenerativeAIEmbeddings(
        model="models/gemini-embedding-001", google_api_key=google_api_key
    )


def create_vector_store(client, collection_name, embedding_function):
    return Chroma(
        client=client,
        collection_name=collection_name,
        embedding_function=embedding_function,
    )

import hashlib
import chromadb
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.documents import Document


def embeddings_generator():
    """Returns langchain Gemini embedding function"""
    return GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")


def generate_hash(hash_str: str):
    return hashlib.sha256(hash_str.encode("utf-8")).hexdigest()


def generate_ids(file_contents: str, chunks: list[Document]) -> list[str]:
    """Returns ids for langchain documents"""
    ids = []
    for index, chunk in enumerate(chunks):
        hash_str = f"{file_contents}_{index}_{chunk.page_content}"
        hexdigest = generate_hash(hash_str)
        ids.append(hexdigest)
    return ids


def create_client():
    """Create a Chroma Client"""
    return chromadb.PersistentClient(path="./chroma_langchain_db")


def create_vector_store(client, collection_name):
    embedding_function = embeddings_generator()
    return Chroma(
        client=client,
        collection_name=collection_name,
        embedding_function=embedding_function,
    )


def get_vector_store(collection_name):
    client = create_client()
    return create_vector_store(client, collection_name=collection_name)


def add_documents(vector_store, documents, ids):
    return vector_store.add_documents(documents=documents, ids=ids)


def similarity_search(collection_name, query, k=2, filter=None):
    vector_store = get_vector_store(collection_name=collection_name)
    return vector_store.similarity_search(query, k, filter)


def similarity_search_by_vector(vector_store, vector=[], k=2, filter=None):
    return vector_store.similarity_search_by_vector(vector, k, filter)

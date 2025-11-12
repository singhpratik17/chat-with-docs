import hashlib
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.documents import Document


def embeddings_generator():
    """Returns langchain Gemini embedding function"""
    return GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")


def generate_hash(hash_str: str):
    return hashlib.sha256(hash_str.encode("utf-8")).hexdigest()


def generate_ids(
    cleaned_documents_file_contents: dict[str], chunks: list[Document]
) -> list[str]:
    """Returns ids for langchain documents"""
    ids = []
    for index, chunk in enumerate(chunks):
        file_contents = cleaned_documents_file_contents[chunk.metadata["source"]]
        hash_str = f"{file_contents}_{index}_{chunk.page_content}"
        hexdigest = generate_hash(hash_str)
        ids.append(hexdigest)
    return ids


def create_vector_store(client, collection_name):
    embedding_function = embeddings_generator()
    return Chroma(
        client=client,
        collection_name=collection_name,
        embedding_function=embedding_function,
    )


def add_documents(vector_store, documents, ids):
    return vector_store.add_documents(documents=documents, ids=ids)


def similarity_search(collection_name, query, k=3, filter=None):
    vector_store = create_vector_store(collection_name=collection_name)
    return vector_store.similarity_search(query, k, filter)


def similarity_search_by_vector(vector_store, vector=[], k=2, filter=None):
    return vector_store.similarity_search_by_vector(vector, k, filter)

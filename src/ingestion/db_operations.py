import hashlib
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

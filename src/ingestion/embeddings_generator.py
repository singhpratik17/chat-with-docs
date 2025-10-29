from langchain_core.documents import Document
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv


def generate_embeddings(documents: list[Document]):
    """Returns vector embeddings of langchain documents"""

    load_dotenv()  # Move to main.py

    page_contents = [doc.page_content for doc in documents]
    print(len(page_contents))
    embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
    vectors = embeddings.embed_documents(page_contents)
    print("Generated vectors", len(vectors), len(vectors[0]))

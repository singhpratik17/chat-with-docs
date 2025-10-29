from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_core.documents import Document
from pathlib import Path
from ingestion.text_cleaner import clean_text
from ingestion.text_splitter import split_text
from ingestion.embeddings_generator import generate_embeddings


def load_file(file_path: str) -> list[Document]:
    """Loads a pdf or txt file and returns list of langchain document."""

    if not Path(file_path).is_file():
        return "Input not a file."

    documents = []

    if file_path.endswith(".pdf"):
        try:
            loader = PyPDFLoader(
                file_path=file_path,
                mode="single",
                pages_delimiter="\n--THIS IS A CUSTOM END OF PAGE--\n",
            )
            documents = loader.load()
        except Exception as e:
            return f"Error loading pdf file {e}"

    elif file_path.endswith(".txt"):
        try:
            loader = TextLoader(file_path=file_path)
            documents = loader.load()
        except Exception as e:
            return f"Error loading txt file {e}"
    else:
        return "Unsupported file format."

    return documents


def ingest(file_path: str):
    # Load the file
    documents = load_file(file_path=file_path)

    # Clean
    cleaned_documents = clean_text(documents)

    # Split
    splitted_documents = split_text(cleaned_documents)

    # embeddings
    embeddings = generate_embeddings(splitted_documents)

    return embeddings

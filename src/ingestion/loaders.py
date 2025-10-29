from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_core.documents import Document
from pathlib import Path


def loaders(file_path: str) -> Document:
    """Loads a pdf or txt file and returns contents of the file or errors as str."""
    if not Path(file_path).is_file():
        return "Input not a file."

    document = {}

    if file_path.endswith(".pdf"):
        try:
            loader = PyPDFLoader(
                file_path=file_path,
                mode="single",
                pages_delimiter="\n--THIS IS A CUSTOM END OF PAGE--\n",
            )
            document = loader.load()
        except Exception as e:
            return f"Error loading pdf file {e}"

    elif file_path.endswith(".txt"):
        try:
            loader = TextLoader(file_path=file_path)
            document = loader.load()
        except Exception as e:
            return f"Error loading txt file {e}"
    else:
        return "Unsupported file format."

    return clean_text(document)


def clean_text(document):
    for doc in document:
        text = doc.page_content
        text = text.replace("\n", " ").strip()
        doc.page_content = " ".join(text.split())
        return doc

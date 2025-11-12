from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_core.documents import Document


def load_files(file_paths: list[str]) -> list[Document]:
    """Loads a pdf or txt file and returns list of langchain documents."""

    documents = []

    for file_path in file_paths:

        if not Path(file_path).is_file():
            return f"{file_path} - Input not a file."
        doc = []
        if file_path.endswith(".pdf"):
            try:
                loader = PyPDFLoader(
                    file_path=file_path,
                    mode="single",
                    pages_delimiter="\n--THIS IS A CUSTOM END OF PAGE--\n",
                )
                doc = loader.load()
            except Exception as e:
                return f"Error loading pdf file {e}"

        elif file_path.endswith(".txt"):
            try:
                loader = TextLoader(file_path=file_path)
                doc = loader.load()
            except Exception as e:
                return f"Error loading txt file {e}"
        else:
            return f"{file_path} - Unsupported file format."

        documents.extend(doc)
    return documents

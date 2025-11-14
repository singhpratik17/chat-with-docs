from .document_loader import load_files
from .text_cleaner import clean_text, get_file_contents
from .text_splitter import split_documents
from ..chroma_db.db_operations import (
    add_documents,
)
from .id_generator import generate_ids


def ingest(file_paths: list[str], vector_store):
    # Load the file
    documents = load_files(file_paths=file_paths)

    # Clean
    cleaned_documents = clean_text(documents)

    cleaned_documents_file_contents = get_file_contents(cleaned_documents)

    # Split
    chunks = split_documents(cleaned_documents)

    # generate Ids
    ids = generate_ids(cleaned_documents_file_contents, chunks)

    # add documents
    return add_documents(vector_store=vector_store, documents=chunks, ids=ids)

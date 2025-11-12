from .document_loader import load_files
from .text_cleaner import clean_text, get_file_contents
from .text_splitter import split_documents
from ..retrieval.db_operations import (
    generate_ids,
    create_client,
    create_vector_store,
    add_documents,
)


def ingest(file_paths: list[str]):
    # Load the file
    documents = load_files(file_paths=file_paths)

    # Clean
    cleaned_documents = clean_text(documents)

    cleaned_documents_file_contents = get_file_contents(cleaned_documents)

    # Split
    chunks = split_documents(cleaned_documents)

    # generate Ids
    ids = generate_ids(cleaned_documents_file_contents, chunks)

    # create chroma client
    client = create_client()

    # create collection
    store = create_vector_store(client, collection_name="test_2")

    # add documents

    return add_documents(vector_store=store, documents=chunks, ids=ids)

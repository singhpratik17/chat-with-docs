from .document_loader import load_files
from .text_cleaner import clean_text
from .text_splitter import split_documents
from ..chroma_db.db_operations import (
    add_documents,
)
from .id_generator import generate_ids


async def ingest(files: list[str], vector_store):
    # Load the file
    documents = await load_files(files)

    # Clean
    cleaned_documents, file_contents = clean_text(documents).values()

    # Split
    chunks = split_documents(cleaned_documents)

    # generate Ids
    ids = generate_ids(file_contents, chunks)

    # add documents
    await add_documents(vector_store=vector_store, documents=chunks, ids=ids)

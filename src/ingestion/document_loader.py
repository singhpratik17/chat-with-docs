from pathlib import Path
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_core.documents import Document
from ingestion.text_cleaner import clean_text
from ingestion.text_splitter import split_documents
from retrieval.db_operations import (
    generate_ids,
    create_client,
    create_vector_store,
    add_documents,
)


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
    load_dotenv()  # Move to main.py

    # Load the file
    documents = load_file(file_path=file_path)
    # Clean
    cleaned_documents = clean_text(documents)

    file_contents = cleaned_documents[0].page_content

    # Split
    chunks = split_documents(cleaned_documents)

    # generate Ids
    ids = generate_ids(file_contents, chunks)

    # create chroma client
    client = create_client()
    print("Chrom client \n", client)

    # create collection
    store = create_vector_store(client, collection_name="expat_handbook_2")

    # add documents

    docs = add_documents(vector_store=store, documents=chunks, ids=ids)

    return docs

    # results = similarity_search(
    #     store,
    #     "those in which sharing & caring are reciprocated",
    #     k=2,
    # )

    # for res in results:
    #     print(res.page_content)

    # results = store.similarity_search_by_vector(
    #     embedding=embeddings_generator().embed_query("What are the bank options?"),
    #     k=1,
    # )
    # for doc in results:
    #     print(f"* {doc.page_content} [{doc.metadata}]")

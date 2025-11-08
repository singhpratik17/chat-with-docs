from pathlib import Path
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_core.documents import Document
from ingestion.text_cleaner import clean_text, get_file_contents
from ingestion.text_splitter import split_documents
from retrieval.db_operations import (
    generate_ids,
    # create_client,
    # create_vector_store,
    # add_documents,
)


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


def ingest(file_paths: list[str]):
    load_dotenv()  # Move to main.py

    # Load the file
    documents = load_files(file_paths=file_paths)
    print(f"\n\n Docs: {documents}")
    print(f"\n\n Length Docs: {len(documents)}")

    # Clean
    cleaned_documents = clean_text(documents)
    print(f"\n\n Cleaned Docs: {cleaned_documents}")
    print(f"\n\n Length Cleaned Docs: {len(cleaned_documents)}")

    cleaned_documents_file_contents = get_file_contents(cleaned_documents)
    print(f"\n\n Cleaned file contents : {cleaned_documents_file_contents}")
    print(f"\n\n Length cleaned file contents: {len(cleaned_documents)}")

    # Split
    chunks = split_documents(cleaned_documents)
    print(f"\n\n Splitted Docs (Chunks): {chunks}")
    print(f"\n\n Length Splitted Docs (Chunks): {len(chunks)}")

    # generate Ids
    ids = generate_ids(cleaned_documents_file_contents, chunks)
    print(f"\n\n ids: {ids}")
    print(f"\n\n Length ids: {len(ids)}")

    # create chroma client
    # client = create_client()
    # print("Chrom client \n", client)

    # create collection
    # store = create_vector_store(client, collection_name="test_2")

    # add documents

    # docs = add_documents(vector_store=store, documents=chunks, ids=ids)

    # return docs

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

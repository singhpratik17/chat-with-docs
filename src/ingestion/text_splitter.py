from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_text(documents: list[Document]) -> list[Document]:
    """Split langchain documents"""

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100,
        add_start_index=True,
    )
    splitted_documents = text_splitter.split_documents(documents)

    print(f"Split doc into {len(splitted_documents)} sub-documents.")

    return splitted_documents

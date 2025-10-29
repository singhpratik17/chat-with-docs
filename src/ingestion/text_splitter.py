from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_text(documents):
    """Split langchain documents"""

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=20,
        add_start_index=True,
    )
    splitted_documents = text_splitter.split_documents(documents)

    return splitted_documents

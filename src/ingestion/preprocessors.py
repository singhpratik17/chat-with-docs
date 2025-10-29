from langchain_text_splitters import RecursiveCharacterTextSplitter


def clean_text(documents):
    """Clean langchain documents"""

    cleaned_documents = []

    for doc in documents:
        text = doc.page_content
        text = text.replace("\n", " ").strip()
        doc.page_content = " ".join(text.split())
        cleaned_documents.append(doc)

    return cleaned_documents


def split_text(documents):
    """Split langchain documents"""

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=20,
        add_start_index=True,
    )
    splitted_documents = text_splitter.split_documents(documents)

    return splitted_documents

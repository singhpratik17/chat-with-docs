from langchain_core.documents import Document


def clean_text(documents: list[Document]) -> list[Document]:
    """Clean langchain documents"""

    cleaned_documents = []

    for doc in documents:
        text = doc.page_content
        text = text.replace("\n", " ").strip()
        doc.page_content = " ".join(text.split())
        cleaned_documents.append(doc)

    return cleaned_documents


def get_file_contents(documents: list[Document]) -> dict:
    """Clean langchain documents"""

    file_contents = {}

    for doc in documents:
        source = doc.metadata["source"]
        file_contents[source] = doc.page_content

    return file_contents

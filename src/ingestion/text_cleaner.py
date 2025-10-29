def clean_text(documents):
    """Clean langchain documents"""

    cleaned_documents = []

    for doc in documents:
        text = doc.page_content
        text = text.replace("\n", " ").strip()
        doc.page_content = " ".join(text.split())
        cleaned_documents.append(doc)

    return cleaned_documents

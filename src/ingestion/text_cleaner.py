from langchain_core.documents import Document
from pydantic import BaseModel


class CleanedDocs(BaseModel):
    cleaned_documents: list[Document]
    file_contents: dict[str, str]


def clean_text(documents: list[Document]) -> CleanedDocs:
    """Clean langchain documents"""

    cleaned_documents = []
    file_contents = {}

    for doc in documents:
        text = doc.page_content
        text = text.replace("\n", " ").strip()
        doc.page_content = " ".join(text.split())
        cleaned_documents.append(doc)

        source = doc.metadata["source"]
        file_contents[source] = doc.page_content

    return {"cleaned_documents": cleaned_documents, "file_contents": file_contents}

from langchain.tools import tool
from src.chroma_db.db_operations import similarity_search


def _format_chunk(doc) -> str:
    source = doc.metadata.get("source", "unknown")
    page = doc.metadata.get("page_label")
    location = f"{source}, page {page}" if page else source
    return f"[{location}]\n{doc.page_content}"


def make_search_db_tool(vector_store):
    @tool
    def search_db(query: str) -> str:
        """Search the uploaded documents for passages relevant to the query.

        Args:
            query: Search terms to look for

        Returns passages, each labelled with its source file and page (for PDFs).
        """
        docs = similarity_search(vector_store, query=query)
        return "\n\n".join(_format_chunk(doc) for doc in docs)

    return search_db

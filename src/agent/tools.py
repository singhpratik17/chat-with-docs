from langchain.tools import tool
from retrieval.db_operations import similarity_search


@tool
def search_db(query):
    """Search the database for records matching the user query.

    Args:
        collection_name: Chroma store instance
        query: Search terms to look for
        limit: Maximum number of results to return
    """
    docs = similarity_search(collection_name="test_2", query=query)
    print("**********search_db tool invoked**********")
    return "".join([doc.page_content for doc in docs])

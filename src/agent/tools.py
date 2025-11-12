from langchain.tools import tool
from src.chroma_db.db_operations import similarity_search


def make_search_db_tool(vector_store):
    @tool
    def search_db(query):
        """Search the database for records matching the user query.

        Args:
            collection_name: Chroma store instance
            query: Search terms to look for
            limit: Maximum number of results to return
        """
        print("Searching in DB")
        return similarity_search(vector_store, query=query)

    return search_db

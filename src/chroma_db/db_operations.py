async def add_documents(vector_store, documents, ids):
    return await vector_store.aadd_documents(documents=documents, ids=ids)


def similarity_search(vector_store, query, k=3, filter=None):
    return vector_store.similarity_search(query, k, filter)


def similarity_search_by_vector(vector_store, vector=[], k=2, filter=None):
    return vector_store.similarity_search_by_vector(vector, k, filter)

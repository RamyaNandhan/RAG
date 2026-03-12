"""
Handles similarity search
"""


def retrieve_documents(vector_db, query, k=3):
    """
    Retrieve top k relevant documents
    """

    docs = vector_db.similarity_search(query, k=k)

    return docs
"""
Vector database operations using Chroma
"""

from langchain_community.vectorstores import Chroma


def create_vector_store(chunks, embeddings, persist_directory="vector_db"):
    """
    Create and store embeddings in Chroma DB
    """

    vector_db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=persist_directory
    )

    vector_db.persist()

    print("Vector store created successfully")

    return vector_db


def load_vector_store(embeddings, persist_directory="vector_db"):
    """
    Load existing vector database
    """

    vector_db = Chroma(
        persist_directory=persist_directory,
        embedding_function=embeddings
    )

    return vector_db
"""
Handles embedding model creation
"""

from langchain_community.embeddings import SentenceTransformerEmbeddings


def load_embedding_model(model_name="all-MiniLM-L6-v2"):
    """
    Load embedding model
    """

    embeddings = SentenceTransformerEmbeddings(
        model_name=model_name
    )

    return embeddings
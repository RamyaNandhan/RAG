"""
Loads documents from the data directory
"""

from langchain_community.document_loaders import PyMuPDFLoader


def load_documents(file_path: str):
    """
    Load PDF documents using PyMuPDFLoader
    """
    loader = PyMuPDFLoader(file_path)
    documents = loader.load()

    print(f"Loaded {len(documents)} pages from document")

    return documents
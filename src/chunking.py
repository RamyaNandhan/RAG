"""
Splits documents into chunks for embedding
"""

from langchain.text_splitter import RecursiveCharacterTextSplitter


def split_documents(documents, chunk_size=800, chunk_overlap=100):
    """
    Split documents into smaller chunks
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )

    chunks = splitter.split_documents(documents)

    print(f"Created {len(chunks)} chunks")

    return chunks
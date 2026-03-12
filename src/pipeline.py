"""
End-to-end RAG pipeline
"""

from src.data_ingestion import load_documents
from src.chunking import split_documents
from src.embeddings import load_embedding_model
from src.vector_store import create_vector_store
from src.retrieval import retrieve_documents
from src.llm_inference import load_llm, generate_answer


def run_pipeline():

    # 1 Load documents
    docs = load_documents("data/raw/documents.pdf")

    # 2 Chunk documents
    chunks = split_documents(docs)

    # 3 Load embedding model
    embeddings = load_embedding_model()

    # 4 Create vector database
    vector_db = create_vector_store(chunks, embeddings)

    # 5 Load LLM
    llm = load_llm("models/llama_model.gguf")

    while True:

        query = input("\nAsk a question (type 'exit' to quit): ")

        if query.lower() == "exit":
            break

        retrieved_docs = retrieve_documents(vector_db, query)

        answer = generate_answer(llm, query, retrieved_docs)

        print("\nAnswer:\n")
        print(answer)
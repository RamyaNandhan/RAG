"""
Local LLM inference using llama.cpp
"""

from langchain_community.llms import LlamaCpp


def load_llm(model_path):

    llm = LlamaCpp(
        model_path=model_path,
        temperature=0.2,
        max_tokens=512,
        top_p=1,
        verbose=True
    )

    return llm


def generate_answer(llm, query, context_docs):

    context = "\n\n".join([doc.page_content for doc in context_docs])

    prompt = f"""
Use the following context to answer the question.

Context:
{context}

Question:
{query}

Answer:
"""

    response = llm.invoke(prompt)

    return response
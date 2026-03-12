# Retrieval-Augmented Generation (RAG) NLP System



A production-style \*\*Retrieval-Augmented Generation (RAG)\*\* pipeline that enables users to ask natural language questions over documents using a local Large Language Model (LLM).



This project demonstrates how to combine \*\*document retrieval, vector embeddings, and generative AI\*\* to build an intelligent question-answering system grounded in source documents.



\---



# Project Overview



Large Language Models (LLMs) often hallucinate or lack access to proprietary data.

Retrieval-Augmented Generation (RAG) solves this by retrieving relevant information from a document corpus before generating an answer.



This system:



1\. Ingests PDF documents

2\. Splits them into semantic chunks

3\. Generates vector embeddings

4\. Stores embeddings in a vector database

5\. Retrieves relevant context for a user query

6\. Uses a local LLM to generate a final answer



\---



\# System Architecture



<img src="architecture/rag\_architecture.png" width="900">



Pipeline Flow:



Data → Chunking → Embedding → Vector Database → Retrieval → LLM → Response



\---



\# Key Features



\* Document Question Answering

\* Retrieval-Augmented Generation pipeline

\* Local LLM inference

\* Vector similarity search

\* Modular ML engineering code structure

\* FastAPI API interface

\* Experiment tracking

\* Config-driven pipeline



\---



\# Tech Stack



| Component       | Technology           |

| --------------- | -------------------- |

| Programming     | Python               |

| Framework       | LangChain            |

| Embeddings      | SentenceTransformers |

| Vector Database | ChromaDB             |

| LLM Runtime     | Llama.cpp            |

| Document Loader | PyMuPDF              |

| API             | FastAPI              |

| Model Format    | GGUF                 |



\---



\# Repository Structure



```

rag-nlp-production/

│

├── data/

│   ├── raw/

│   │   └── documents.pdf

│   └── processed/

│

├── models/

│   └── llama\_model.gguf

│

├── configs/

│   └── config.yaml

│

├── src/

│   ├── ingestion/

│   │   └── data\_ingestion.py

│   │

│   ├── processing/

│   │   └── chunking.py

│   │

│   ├── embeddings/

│   │   └── embeddings.py

│   │

│   ├── vectorstore/

│   │   └── vector\_store.py

│   │

│   ├── retrieval/

│   │   └── retrieval.py

│   │

│   ├── llm/

│   │   └── llm\_inference.py

│   │

│   ├── prompts/

│   │   └── prompt\_templates.py

│   │

│   ├── pipeline/

│   │   └── rag\_pipeline.py

│   │

│   ├── evaluation/

│   │   └── rag\_evaluator.py

│   │

│   └── utils/

│       └── logger.py

│

├── api/

│   └── app.py

│

├── experiments/

│   └── experiment\_results.md

│

├── notebooks/

│   └── RAG\_Exploration.ipynb

│

├── outputs/

│   └── responses/

│

├── requirements.txt

├── Dockerfile

├── run\_pipeline.py

└── README.md

```



\---



\# Installation



Clone the repository



```

git clone https://github.com/yourusername/rag-nlp-system.git

cd rag-nlp-system

```



Install dependencies



```

pip install -r requirements.txt

```



\---



\# Running the Pipeline



Run the end-to-end RAG pipeline:



```

python run\_pipeline.py

```



Example interaction:



```

Ask question: What is Retrieval Augmented Generation?



Answer:

Retrieval-Augmented Generation is a technique that combines

information retrieval with large language models to produce

responses grounded in external knowledge sources.

```



\---



\# Running the API



Start the FastAPI service



```

uvicorn api.app:app --reload

```



Test API



```

http://localhost:8000/ask?query=What is RAG?

```



\---



\# Configuration



Pipeline configuration is stored in:



```

configs/config.yaml

```



Example parameters:



```

chunk\_size: 800

chunk\_overlap: 100

embedding\_model: all-MiniLM-L6-v2

top\_k: 3

temperature: 0.2

```



\---



\# Experiments



Experiments were conducted to evaluate retrieval performance.



| Experiment | Chunk Size | Retrieval Quality |

| ---------- | ---------- | ----------------- |

| Exp-1      | 500        | Medium            |

| Exp-2      | 800        | Best              |

| Exp-3      | 1200       | Good              |



Observations:



\* Smaller chunks increase recall but reduce context

\* Medium chunk sizes provide optimal balance

\* Embedding quality significantly affects retrieval performance



\---



\# Example Workflow



1️⃣ Load PDF documents

2️⃣ Split documents into chunks

3️⃣ Generate embeddings

4️⃣ Store vectors in ChromaDB

5️⃣ Retrieve relevant chunks for a query

6️⃣ Generate answer using LLM



\---



\# Evaluation



Basic evaluation is implemented in:



```

src/evaluation/rag\_evaluator.py

```



Metrics explored:



\* Retrieval accuracy

\* Context relevance

\* Response latency



\---



\# Future Improvements



\* Add RAG evaluation frameworks (RAGAS / TruLens)

\* Hybrid search (BM25 + vector search)

\* Web UI chatbot

\* Streaming LLM responses

\* Distributed vector database

\* Model fine-tuning



\---



\# Use Cases



\* Enterprise document search

\* Internal knowledge assistants

\* Research document analysis

\* Customer support automation



\---



\# Author



Developed as an end-to-end \*\*NLP Retrieval-Augmented Generation system\*\* demonstrating modern LLM engineering practices.



\---




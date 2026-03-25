# Semantic Search Engine

A hands-on exploration of AI fundamentals by building a semantic
retrieval system, covering embeddings, vector databases, and
Retrieval-Augmented Generation (RAG) architecture.

------------------------------------------------------------------------

## 🚀 Overview

This project demonstrates how modern AI systems retrieve information
using semantic understanding instead of keyword matching.

Text is converted into vector embeddings and stored in a vector
database. Queries are also embedded and matched based on similarity to
retrieve the most relevant results.

------------------------------------------------------------------------

## 🧠 System Architecture

    User Query
       ↓
    Text Embedding
       ↓
    Vector Search (Qdrant)
       ↓
    Top-K Similar Results

------------------------------------------------------------------------

## ⚙️ Tech Stack

-   FastAPI --- API layer
-   Qdrant --- Vector database
-   Sentence Transformers --- Embedding generation (`all-MiniLM-L6-v2`)
-   Python

------------------------------------------------------------------------

## ✨ Features (Phase 1)

-   Generate embeddings from text
-   Store vectors in Qdrant
-   Perform semantic similarity search
-   Retrieve top-K relevant results

------------------------------------------------------------------------

## 📁 Project Structure

    semantic-search-engine/
    │
    ├── app/
    │   ├── main.py
    │   ├── embeddings.py
    │   ├── db.py
    │
    ├── data/
    │   └── sample_docs.json
    │
    ├── docs/
    │   ├── embeddings.md
    │   └── retrieval.md
    │
    ├── requirements.txt
    └── README.md

------------------------------------------------------------------------

## ▶️ Getting Started

### 1. Start Qdrant

    docker run -p 6333:6333 qdrant/qdrant

### 2. Install dependencies

    pip install -r requirements.txt

### 3. Run the application

    uvicorn app.main:app --reload

------------------------------------------------------------------------

## 🔍 Example Usage

    GET /search?q=What is a database?

### Sample Response

    [
      {
        "text": "PostgreSQL is a powerful relational database"
      }
    ]

------------------------------------------------------------------------

## 🧠 Key Concepts

### Embeddings

-   Text is converted into numerical vectors\
-   Similar meaning → closer vectors

### Cosine Similarity

-   Measures similarity between vectors\
-   Preferred for text embeddings

### Metadata (Payload)

-   Stores original text and attributes\
-   Enables filtering and context building

------------------------------------------------------------------------

## ⚠️ Limitations (Current Phase)

-   No document chunking
-   No metadata filtering
-   No conversational memory
-   No RAG pipeline yet

------------------------------------------------------------------------

## 🛣️ Roadmap

### Phase 2 --- Document Ingestion

-   Implement chunking strategies
-   Support larger documents

### Phase 3 --- RAG Pipeline

-   Inject retrieved context into LLM prompts
-   Generate contextual responses

### Phase 4 --- Chat System

-   Add conversation memory
-   Session management

### Phase 5 --- Production Enhancements

-   Redis caching
-   Logging and observability
-   Rate limiting

------------------------------------------------------------------------

## 💡 Key Learnings

-   Vector databases are similarity search systems, not AI
-   Retrieval quality depends heavily on embeddings and chunking
-   Metadata is critical for effective RAG systems
-   Poor retrieval leads to poor AI responses

------------------------------------------------------------------------

## 👨‍💻 Author

Shankar --- Backend Engineer exploring AI system design with a focus on
practical implementation and production thinking.

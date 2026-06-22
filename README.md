# Multi-Document RAG Search Engine

A **Retrieval-Augmented Generation (RAG)** based question-answering system that enables users to query information across multiple documents using semantic search and LLM-powered answer generation. The project focuses on document ingestion, chunking, embedding generation, vector retrieval, and context-aware responses with source traceability. Based on the project summary in the resume, the system uses a deterministic generation setup (`temperature = 0`), retrieves the **top-8 relevant chunks** per query, and attaches metadata for **page-level source traceability**. citeturn1search1

---

## 🚀 Features

- Query multiple documents through a single natural language interface. citeturn1search1
- Retrieval-Augmented Generation (RAG) pipeline for context-aware question answering. citeturn1search1
- FAISS-based vector similarity search for efficient semantic retrieval. citeturn1search1
- Document ingestion and chunking pipeline for unstructured text processing. citeturn1search1
- Top-8 relevant chunk retrieval to improve response relevance. citeturn1search1
- Page-level source traceability using metadata attached to retrieved context. citeturn1search1
- Deterministic output configuration to keep answers consistent. citeturn1search1

---

## 🧠 Problem Statement

Searching through long documents manually is time-consuming and inefficient. Traditional keyword search often fails to capture semantic meaning, especially when the same concept is expressed using different wording. This project solves that problem by combining **semantic retrieval** with **LLM-based answer generation**, enabling users to ask natural language questions and receive relevant, grounded answers from multiple documents. citeturn1search1

---

## 🏗️ Solution Overview

The application follows a typical RAG workflow:

1. **Document Ingestion**  
   Upload and read one or more documents.
2. **Text Chunking**  
   Split large document text into smaller chunks for better retrieval. citeturn1search1
3. **Embedding Generation**  
   Convert chunks into vector embeddings.
4. **Vector Storage**  
   Store embeddings in **FAISS** for fast similarity search. citeturn1search1
5. **Semantic Retrieval**  
   Retrieve the **top-8** most relevant chunks for a given query. citeturn1search1
6. **LLM Response Generation**  
   Pass retrieved context + user query to the language model.
7. **Source Traceability**  
   Return answers with metadata-backed source/page references. citeturn1search1

---

## 🏛️ Architecture

```text
                 ┌────────────────────┐
                 │   Input Documents   │
                 └─────────┬──────────┘
                           │
                           ▼
                 ┌────────────────────┐
                 │ Ingestion Pipeline │
                 └─────────┬──────────┘
                           │
                           ▼
                 ┌────────────────────┐
                 │   Text Chunking    │
                 └─────────┬──────────┘
                           │
                           ▼
                 ┌────────────────────┐
                 │ Embedding Creation │
                 └─────────┬──────────┘
                           │
                           ▼
                 ┌────────────────────┐
                 │  FAISS Vector DB   │
                 └─────────┬──────────┘
                           │
          User Query       │      Top-K Relevant Chunks
                 ┌─────────▼──────────┐
                 │ Semantic Retrieval │
                 └─────────┬──────────┘
                           │
                           ▼
                 ┌────────────────────┐
                 │   LLM Generation   │
                 └─────────┬──────────┘
                           │
                           ▼
                 ┌────────────────────┐
                 │ Answer + Sources   │
                 └────────────────────┘
```

---

## 🛠️ Tech Stack

- **Language:** Python citeturn1search1
- **Framework / Orchestration:** LangChain citeturn1search1
- **Vector Store:** FAISS citeturn1search1
- **Embeddings / Model Integration:** HuggingFace embeddings, LLM integration citeturn1search1
- **Concepts Used:** RAG, semantic search, prompt engineering, metadata traceability citeturn1search1

---

## 📂 Suggested Project Structure

> Update this section if your actual repository structure is different.

```text
Multi-Document-RAG-Search-Engine/
│
├── data/                     # Input documents
├── notebooks/                # Experimentation / prototyping
├── src/
│   ├── ingestion.py          # Document loading and parsing
│   ├── chunking.py           # Text splitting logic
│   ├── embeddings.py         # Embedding generation
│   ├── vector_store.py       # FAISS indexing and retrieval
│   ├── rag_pipeline.py       # End-to-end RAG flow
│   └── utils.py              # Helper functions
│
├── app.py                    # Entry point / application script
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/jaskaransingh16/Multi-Document-RAG-Search-Engine.git
cd Multi-Document-RAG-Search-Engine
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate      # Linux / Mac
venv\Scripts\activate         # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables (if needed)

If your project uses an LLM API key or local model path, create a `.env` file:

```env
API_KEY=your_api_key_here
MODEL_NAME=your_model_name
```

---

## ▶️ Usage

Depending on your implementation, run the main application using one of the following patterns:

```bash
python app.py
```

or, if your main logic is notebook-based:

```bash
jupyter notebook
```

### Example Workflow

1. Add documents to the input directory.
2. Run the ingestion and indexing pipeline.
3. Ask a natural language question.
4. Retrieve the most relevant chunks.
5. Generate an answer grounded in retrieved context.
6. Display source/page references with the answer. citeturn1search1

---

## 💬 Example Query

**Question:**
```text
What are the key points discussed across the uploaded documents regarding the topic?
```

**System Flow:**
- Convert user question into embedding
- Retrieve top-8 similar chunks from FAISS
- Pass retrieved context to LLM
- Return final answer with source traceability citeturn1search1

---

## 📈 Key Highlights

- Designed a document-centric RAG pipeline for **context-aware question answering**. citeturn1search1
- Implemented **vector similarity search** using **FAISS**. citeturn1search1
- Built a **document ingestion** and **chunking pipeline** for unstructured data. citeturn1search1
- Enabled **1:1 page-level source traceability** using metadata. citeturn1search1
- Used **temperature = 0** for deterministic response generation. citeturn1search1

---

## 🔍 Challenges Solved

- Handling unstructured document content for retrieval. citeturn1search1
- Improving semantic relevance compared to keyword-only search. citeturn1search1
- Maintaining answer grounding through metadata-backed references. citeturn1search1
- Making responses more reproducible using deterministic generation settings. citeturn1search1

---

## 🚧 Future Enhancements

- Add support for more file types (PDF, DOCX, HTML, CSV).
- Integrate re-ranking for improved retrieval precision.
- Introduce conversational memory for multi-turn Q&A.
- Extend to agentic workflows using tool calling / LangGraph.
- Add web interface for document upload and chat.
- Deploy as an API or cloud-hosted application.

---

## 👨‍💻 Author

**Jaskaran Singh**  
- LinkedIn: [jaskaransinghbasra](https://www.linkedin.com/in/jaskaransinghbasra)
- GitHub: [jaskaransingh16](https://github.com/jaskaransingh16)

---
scripts, notebooks, or specific models), you should update the **Installation**, **Project Structure**, and **Usage** sections accordingly. citeturn1search1

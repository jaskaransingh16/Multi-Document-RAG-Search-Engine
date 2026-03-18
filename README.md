# Legal Document Q&A System (Mini-RAG using LangChain)

This project is a Retrieval-Augmented Generation (RAG) system that answers questions **only** from a given PDF document and shows **page numbers** used as sources.

## Features
- Load and process a PDF (text-based)
- Split document into chunks (chunk_size=1000, chunk_overlap=150)
- Create embeddings (SentenceTransformers)
- Store embeddings in FAISS vector database
- Retrieve top-k relevant chunks for a question
- Generate answer using Groq LLM
- Show source attribution (page numbers)

## Project Structure
- `data/legal.pdf` : Input PDF
- `faiss_index/` : Saved FAISS index (`index.faiss`, `index.pkl`)
- `src/02_build_faiss_index.py` : Build and save FAISS index
- `src/03_rag_qa_groq.py` : Ask questions + get answers + page citations

## Setup (Windows / VS Code)

### 1) Create and activate virtual environment
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
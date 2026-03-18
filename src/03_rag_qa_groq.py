import os
from pathlib import Path
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

load_dotenv(dotenv_path=Path(__file__).resolve().parents[1] / ".env")

INDEX_DIR = "faiss_index"
GROQ_MODEL = "llama-3.1-8b-instant"  # fast + good for RAG

SYSTEM_RULES = """You are a legal document assistant.
Answer ONLY using the provided context from the document chunks.
If the answer is not in the context, say exactly:
"I cannot find this information in the provided document."
Also provide the page numbers you used.
"""

def format_context(docs):
    blocks = []
    for d in docs:
        page_label = d.metadata.get("page_label", d.metadata.get("page", "NA"))
        blocks.append(f"[Page {page_label}] {d.page_content}")
    return "\n\n".join(blocks)

def ask_groq(question: str, context: str) -> str:
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("Missing GROQ_API_KEY in .env")

    llm = ChatGroq(
        model=GROQ_MODEL,
        temperature=0,
        groq_api_key=api_key
    )

    prompt = f"{SYSTEM_RULES}\n\nContext:\n{context}\n\nQuestion: {question}\nAnswer:"
    return llm.invoke(prompt).content

def main():
    # Load vector store
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vs = FAISS.load_local(INDEX_DIR, embeddings, allow_dangerous_deserialization=True)

    question = input("Ask a question about the PDF: ").strip()

    # Retrieve (increase k for better legal definitions)
    retrieved = vs.similarity_search(question, k=8)

    # Debug: show retrieved chunks
    print("\n--- Retrieved chunks (debug) ---")
    for i, d in enumerate(retrieved, 1):
        page = d.metadata.get("page_label", d.metadata.get("page"))
        print(f"\n[{i}] Page {page}")
        print(d.page_content[:300])

    context = format_context(retrieved)
    answer = ask_groq(question, context)

    pages = sorted({int(d.metadata.get("page_label", d.metadata.get("page"))) for d in retrieved if str(d.metadata.get("page_label", d.metadata.get("page"))).isdigit()})

    print("\n================= ANSWER =================\n")
    print(answer)
    print("\n================= SOURCES =================\n")
    print("Pages used:", pages)

if __name__ == "__main__":
    main()
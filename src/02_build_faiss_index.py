import os
import pickle
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

PDF_PATH = "data/legal.pdf"
INDEX_DIR = "faiss_index"

def main():
    # 1) Load PDF
    docs = PyPDFLoader(PDF_PATH).load()

    # 2) Split into chunks
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
    chunks = splitter.split_documents(docs)

    # 3) Embeddings (free, local)
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    # 4) Build FAISS vector store
    vectorstore = FAISS.from_documents(chunks, embeddings)

    # 5) Save FAISS index to disk
    os.makedirs(INDEX_DIR, exist_ok=True)
    vectorstore.save_local(INDEX_DIR)

    print("✅ FAISS index created and saved to:", INDEX_DIR)
    print("Pages:", len(docs), "| Chunks:", len(chunks))

if __name__ == "__main__":
    main()
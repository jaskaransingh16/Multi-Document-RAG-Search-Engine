import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader

#load_dotenv()
from pathlib import Path
load_dotenv(dotenv_path=Path(__file__).resolve().parents[1] / ".env")

PDF_PATH = "data/legal.pdf"    # make sure your PDF is here

def main():
    # Check Gemini key exists (we'll use it later)
    key = os.getenv("GEMINI_API_KEY")
    if not key:
        raise ValueError("Missing GEMINI_API_KEY in .env")

    loader = PyPDFLoader(PDF_PATH)
    docs = loader.load()  # one Document per page

    print("Total pages:", len(docs))
    print("First page metadata:", docs[0].metadata)
    print("\n--- First page preview (first 500 chars) ---\n")
    print(docs[0].page_content[:500])

if __name__ == "__main__":
    main()
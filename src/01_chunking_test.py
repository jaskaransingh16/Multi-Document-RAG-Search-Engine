from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

PDF_PATH = "data/legal.pdf"

def main():
    docs = PyPDFLoader(PDF_PATH).load()

    # Chosen values (good default for legal text)
    chunk_size = 1000
    chunk_overlap = 150

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )

    chunks = splitter.split_documents(docs)

    print("Pages:", len(docs))
    print("Chunks:", len(chunks))
    print("Example chunk metadata:", chunks[0].metadata)
    print("\n--- Example chunk text (first 400 chars) ---\n")
    print(chunks[0].page_content[:400])

if __name__ == "__main__":
    main()
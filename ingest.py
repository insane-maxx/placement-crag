import os
import shutil
import re
from langchain_core.documents import Document
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import DirectoryLoader, TextLoader

DOCS_DIR = "./placement_docs"
DB_DIR = "./chroma_db"

def extract_metadata_from_text(text: str) -> dict:
    """Extracts structured metadata safely using bounded regex."""
    # Stop capturing at a pipe (|) or newline (\n)
    company_match = re.search(r"Company:\s*([^|\n]+)", text)
    year_match = re.search(r"Academic Year:\s*([^|\n]+)", text)
    date_match = re.search(r"Notice Date:\s*([^|\n]+)", text)
    doc_type_match = re.search(r"Document Type:\s*([^|\n]+)", text)

    return {
        "company": company_match.group(1).strip() if company_match else "Unknown",
        "academic_year": year_match.group(1).strip() if year_match else "Unknown",
        "notice_date": date_match.group(1).strip() if date_match else "Unknown",
        "doc_type": doc_type_match.group(1).strip() if doc_type_match else "General",
    }

def build_vector_store():
    if not os.path.exists(DOCS_DIR):
        print(f"Error: Directory '{DOCS_DIR}' not found.")
        return

    # Clean up old database to prevent duplication conflicts
    if os.path.exists(DB_DIR):
        shutil.rmtree(DB_DIR)
        print("Cleared old Chroma database directory.")

    print("Loading documents...")
    loader = DirectoryLoader(DOCS_DIR, glob="*.txt", loader_cls=TextLoader)
    raw_documents = loader.load()

    processed_docs = []
    for doc in raw_documents:
        metadata = extract_metadata_from_text(doc.page_content)
        new_doc = Document(page_content=doc.page_content.strip(), metadata=metadata)
        processed_docs.append(new_doc)

    print(f"Total documents processed: {len(processed_docs)}")

    print("Generating embeddings using Ollama...")
    embeddings = OllamaEmbeddings(model="nomic-embed-text")

    print(f"Saving vector database to {DB_DIR}...")
    vectorstore = Chroma.from_documents(
        documents=processed_docs,
        embedding=embeddings,
        persist_directory=DB_DIR
    )
    print("Vector database build complete for Phase 1!")

if __name__ == "__main__":
    build_vector_store()

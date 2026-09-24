import os
from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings, ChatOllama
from langchain_core.prompts import PromptTemplate

DB_DIR = "./chroma_db"

def test_rag_query(query: str, target_year: str = "2024-2025"):
    print(f"\n--- User Query: '{query}' (Target Year: {target_year}) ---")
    
    # 1. Initialize Embeddings and Vector Store
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    vectorstore = Chroma(persist_directory=DB_DIR, embedding_function=embeddings)
    
    # 2. Setup Retriever with Metadata Filtering for Time-Aware CRAG
    retriever = vectorstore.as_retriever(
        search_kwargs={"k": 2, "filter": {"academic_year": target_year}}
    )
    
    docs = retriever.invoke(query)
    
    print(f"Retrieved {len(docs)} document chunk(s) matching year {target_year}:")
    for i, doc in enumerate(docs):
        print(f"\n[Chunk {i+1} Metadata]: Company={doc.metadata.get('company')}, Year={doc.metadata.get('academic_year')}")
        print(f"Content: {doc.page_content.strip()}")

    # 3. Generate response using local LLM
    llm = ChatOllama(model="llama3.2:3b", temperature=0)
    
    context = "\n\n".join([doc.page_content for doc in docs])
    
    prompt_template = """You are a helpful university placement cell assistant. Answer the question accurately using ONLY the provided context. If the criteria changed, make sure to highlight the updated policy.

Context:
{context}

Question: {query}
Answer:"""
    
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "query"])
    chain = prompt | llm
    
    response = chain.invoke({"context": context, "query": query})
    print(f"\n[Generated Answer]:\n{response.content.strip()}")

if __name__ == "__main__":
    # Test query targeting the latest 2025 criteria
    test_rag_query("What is the CGPA and backlog criteria for Amazon?", target_year="2024-2025")
    
    # Test query targeting the older 2024 criteria
    test_rag_query("What was the Amazon CGPA cutoff last year?", target_year="2023-2024")

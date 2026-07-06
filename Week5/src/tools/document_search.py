import os
from src.embeddings import get_embedding
from src.retriever import retrieve_chunks

def force_reload_documents():
    """No longer needed for Pinecone, kept for backward compatibility with app.py if called."""
    pass

def execute_document_search(query: str, top_k: int = 3) -> str:
    """Searches local uploaded documents for the query using Pinecone."""
    try:
        query_emb = get_embedding(query)
        matches = retrieve_chunks(query_emb, top_k=top_k)
        
        results = []
        for match in matches:
            # We can filter low score matches if we want
            if match.get("score", 0) > 0.2:
                metadata = match.get("metadata", {})
                doc_name = metadata.get("document", "Unknown")
                page = metadata.get("page", "Unknown")
                text = metadata.get("text", "")
                results.append(f"Document: {doc_name}\nPage: {page}\nSnippet: {text}")
                
        if not results:
            return "No relevant information found in documents."
            
        return "\n\n".join(results)
    except Exception as e:
        return f"Error searching documents: {str(e)}"

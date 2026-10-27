from pathlib import Path

def retrieve_documents(query):
    # Implementation for retrieving documents based on the query
    knowledge_base_path  = Path(__file__).resolve().parent.parent/"knowledge_base"
    Documents = list(knowledge_base_path.glob("*.txt"))  # Example: Retrieve all text files in the knowledge_base directory
    matched_documents = []
    for doc in Documents:
        content = doc.read_text()
        if query.lower() in content.lower():
            matched_documents.append(doc)
    return matched_documents
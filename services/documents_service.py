from models.non_relational import save_document, get_documents

def upload_document(case_id, document):
    save_document(case_id, document)
    return {"message": "Document uploaded successfully"}

def list_documents(case_id):
    documents = get_documents(case_id)
    return documents

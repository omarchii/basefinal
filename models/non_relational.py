from extensions import mongo
from datetime import datetime

def save_document(case_id, document):
    collection = mongo.db.documents
    collection.insert_one({
        "case_id": case_id,
        "document": document,
        "uploaded_at": datetime.utcnow()
    })

def get_documents(case_id):
    collection = mongo.db.documents
    documents = collection.find({"case_id": case_id})
    return [{"_id": str(doc["_id"]), "case_id": doc["case_id"], "document": doc["document"], "uploaded_at": doc["uploaded_at"]} for doc in documents]


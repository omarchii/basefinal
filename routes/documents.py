from flask import Blueprint, request, jsonify
from extensions import mongo
from models.non_relational import save_document, get_documents
from bson.objectid import ObjectId


documents_bp = Blueprint('documents', __name__)

@documents_bp.route('/<case_id>', methods=['GET'])
def list_documents(case_id):
    documents = get_documents(case_id)
    return jsonify(documents)

@documents_bp.route('/', methods=['POST'])
def upload_document():
    data = request.json
    save_document(data['case_id'], data['document'])
    return jsonify({"message": "Document uploaded"}), 201

@documents_bp.route('/<case_id>/<document_id>', methods=['DELETE'])
def delete_document(case_id, document_id):
    result = mongo.db.documents.delete_one({"_id": ObjectId(document_id), "case_id": case_id})
    if result.deleted_count == 0:
        return jsonify({"error": "Document not found"}), 404
    return jsonify({"message": "Document deleted successfully"}), 200

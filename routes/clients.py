from flask import Blueprint, request, jsonify
from services.client_service import create_client, get_all_clients, get_client_by_id, update_client, delete_client

clients_bp = Blueprint('clients', __name__)

@clients_bp.route('/', methods=['GET'])
def get_clients():
    return jsonify(get_all_clients())

@clients_bp.route('/<int:client_id>', methods=['GET'])
def get_client(client_id):
    return jsonify(get_client_by_id(client_id))

@clients_bp.route('/', methods=['POST'])
def create_new_client():
    data = request.json
    return jsonify(create_client(data))

@clients_bp.route('/<int:client_id>', methods=['PUT'])
def update_existing_client(client_id):
    data = request.json
    return jsonify(update_client(client_id, data))

@clients_bp.route('/<int:client_id>', methods=['DELETE'])
def delete_existing_client(client_id):
    return jsonify(delete_client(client_id))

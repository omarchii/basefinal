from flask import Blueprint, request, jsonify
from services.user_service import create_user_role

users_bp = Blueprint('users', __name__)

@users_bp.route('/create_user', methods=['POST'])
def create_user():
    data = request.json
    user = data.get('user')
    password = data.get('password')
    role = data.get('role')
    if not user or not password or not role:
        return jsonify({"error": "User, password, and role are required"}), 400
    response = create_user_role(user, password, role)
    return jsonify(response)

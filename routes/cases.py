from flask import Blueprint, request, jsonify
from extensions import db
from models.relational import Case

cases_bp = Blueprint('cases', __name__)

@cases_bp.route('/', methods=['GET'])
def get_cases():
    cases = Case.query.all()
    return jsonify([{
        "id": case.id,
        "client_name": case.client_name,
        "case_type": case.case_type,
        "status": case.status
    } for case in cases])

@cases_bp.route('/', methods=['POST'])
def create_case():
    data = request.json
    new_case = Case(
        client_name=data['client_name'],
        case_type=data['case_type'],
        start_date=data['start_date']
    )
    db.session.add(new_case)
    db.session.commit()
    return jsonify({"message": "Case created"}), 201

@cases_bp.route('/<int:case_id>', methods=['PUT'])
def update_case(case_id):
    data = request.json
    case = Case.query.get(case_id)
    if not case:
        return jsonify({"error": "Case not found"}), 404
    case.client_name = data.get('client_name', case.client_name)
    case.case_type = data.get('case_type', case.case_type)
    case.start_date = data.get('start_date', case.start_date)
    db.session.commit()
    return jsonify({"message": "Case updated successfully"})

@cases_bp.route('/<int:case_id>', methods=['DELETE'])
def delete_case(case_id):
    case = Case.query.get(case_id)
    if not case:
        return jsonify({"error": "Case not found"}), 404
    db.session.delete(case)
    db.session.commit()
    return jsonify({"message": "Case deleted successfully"})

@cases_bp.route('/export', methods=['GET'])
def export_cases():
    cases = Case.query.all()
    case_list = [{
        "id": case.id,
        "client_name": case.client_name,
        "case_type": case.case_type,
        "status": case.status
    } for case in cases]
    return jsonify(case_list)



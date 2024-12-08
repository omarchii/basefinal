from flask import Blueprint, jsonify
from models.relational import Activity, Case
from extensions import mongo


reports_bp = Blueprint('reports', __name__)

@reports_bp.route('/case_summary/<int:case_id>', methods=['GET'])
def case_summary(case_id):
    # Busca las actividades relacionadas con el caso
    activities = Activity.query.filter_by(case_id=case_id).all()

    # Busca los documentos relacionados en MongoDB
    documents = mongo.db.documents.find({"case_id": str(case_id)})

    # Devuelve el resumen del caso
    case = Case.query.get(case_id)
    if not case:
        return jsonify({"error": "Case not found"}), 404

    return jsonify({
        "case_details": {
            "id": case.id,
            "client_name": case.client_name,
            "case_type": case.case_type,
            "status": case.status
        },
        "activities": [{
            "id": activity.id,
            "description": activity.description,
            "activity_date": activity.activity_date
        } for activity in activities],
        "documents": list(documents)
    })

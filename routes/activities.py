from flask import Blueprint, request, jsonify
from models.relational import Activity
from extensions import db

# Define el Blueprint
activities_bp = Blueprint('activities', __name__)

@activities_bp.route('/', methods=['POST'])
def create_activity():
    data = request.json
    activity = Activity(case_id=data['case_id'], 
                        description=data['description'], 
                        activity_date=data['activity_date'])
    db.session.add(activity)
    db.session.commit()
    return jsonify({"message": "Activity created successfully"}), 201

@activities_bp.route('/<int:case_id>', methods=['GET'])
def list_activities(case_id):
    activities = Activity.query.filter_by(case_id=case_id).all()
    return jsonify([{
        "id": activity.id,
        "description": activity.description,
        "created_at": activity.created_at
    } for activity in activities])

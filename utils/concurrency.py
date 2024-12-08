from sqlalchemy.exc import StaleDataError, SQLAlchemyError
from app import db, mongo
from models.relational import Case
from datetime import datetime, timedelta

# Bloqueo Optimista en PostgreSQL
def update_case_with_optimistic_locking(case_id, data, version):
    try:
        case = Case.query.filter_by(id=case_id, version=version).first()
        if not case:
            return {"error": "Conflict detected or case not found"}, 409
        
        case.client_name = data.get('client_name', case.client_name)
        case.case_type = data.get('case_type', case.case_type)
        case.version += 1
        db.session.commit()
        return {"message": "Case updated successfully"}, 200
    except StaleDataError:
        db.session.rollback()
        return {"error": "Conflict detected"}, 409

# Bloqueo Pesimista en PostgreSQL
def lock_case_for_update(case_id):
    case = db.session.query(Case).with_for_update().filter_by(id=case_id).first()
    if not case:
        return {"error": "Case not found"}, 404
    return case

# Actualizaciones Atómicas en MongoDB
def update_document_atomic(case_id, new_data, version):
    result = mongo.db.documents.update_one(
        {"case_id": case_id, "version": version},
        {
            "$set": {"document": new_data},
            "$inc": {"version": 1}
        }
    )
    if result.matched_count == 0:
        return {"error": "Conflict detected or document not found"}, 409
    return {"message": "Document updated successfully"}, 200

# Sistema de Bloqueo en MongoDB
def lock_resource(case_id, user_id, lock_duration=5):
    expiration_time = datetime.utcnow() + timedelta(minutes=lock_duration)
    result = mongo.db.locks.update_one(
        {"case_id": case_id},
        {"$setOnInsert": {
            "locked_by": user_id,
            "locked_at": datetime.utcnow(),
            "expires_at": expiration_time
        }},
        upsert=True
    )
    if result.matched_count > 0:
        return {"error": "Resource is already locked"}, 409
    return {"message": "Resource locked successfully"}, 200

def unlock_resource(case_id, user_id):
    result = mongo.db.locks.delete_one({"case_id": case_id, "locked_by": user_id})
    if result.deleted_count == 0:
        return {"error": "No lock found for this user"}, 404
    return {"message": "Resource unlocked successfully"}, 200

# Manejo de Transacciones
def execute_transaction(operation):
    try:
        operation()
        db.session.commit()
        return {"message": "Transaction committed successfully"}, 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return {"error": str(e)}, 500

from models.relational import Case
from extensions import db

def create_case(data):
    new_case = Case(
        client_name=data['client_name'],
        case_type=data['case_type'],
        start_date=data['start_date']
    )
    db.session.add(new_case)
    db.session.commit()
    return {"message": "Case created successfully"}

def list_cases():
    cases = Case.query.all()
    return [{
        "id": case.id,
        "client_name": case.client_name,
        "case_type": case.case_type,
        "start_date": case.start_date.strftime('%Y-%m-%d')
    } for case in cases]

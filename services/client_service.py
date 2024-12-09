from extensions import db
from models.relational import Client

def create_client(data):
    try:
        client = Client(
            name=data['name'],
            email=data['email'],
            phone=data.get('phone'),
            address=data.get('address')
        )
        db.session.add(client)
        db.session.commit()
        return {"message": f"Client {client.name} created successfully."}
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}

def get_all_clients():
    clients = Client.query.all()
    return [{"id": c.id, "name": c.name, "email": c.email, "phone": c.phone, "address": c.address} for c in clients]

def get_client_by_id(client_id):
    client = Client.query.get(client_id)
    if not client:
        return {"error": "Client not found"}
    return {"id": client.id, "name": client.name, "email": client.email, "phone": client.phone, "address": client.address}

def update_client(client_id, data):
    client = Client.query.get(client_id)
    if not client:
        return {"error": "Client not found"}
    try:
        client.name = data.get('name', client.name)
        client.email = data.get('email', client.email)
        client.phone = data.get('phone', client.phone)
        client.address = data.get('address', client.address)
        db.session.commit()
        return {"message": f"Client {client.name} updated successfully."}
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}

def delete_client(client_id):
    client = Client.query.get(client_id)
    if not client:
        return {"error": "Client not found"}
    try:
        db.session.delete(client)
        db.session.commit()
        return {"message": f"Client {client.name} deleted successfully."}
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}

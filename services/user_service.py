from extensions import db

def create_user_role(user, password, role):
    try:
        # Crear el rol
        db.session.execute(f"CREATE ROLE {role} WITH LOGIN PASSWORD '{password}';")
        
        # Asignar privilegios
        db.session.execute(f"GRANT CONNECT ON DATABASE appdb TO {role};")
        db.session.execute(f"GRANT USAGE ON SCHEMA public TO {role};")
        db.session.execute(f"GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO {role};")
        
        # Crear usuario con rol
        db.session.execute(f"CREATE USER {user} WITH PASSWORD '{password}' IN ROLE {role};")
        
        db.session.commit()
        return {"message": f"User '{user}' with role '{role}' created successfully."}
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}
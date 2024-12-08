from flask import Flask
from extensions import db, mongo, jwt
from config import Config
from routes.cases import cases_bp
from routes.documents import documents_bp
from routes.activities import activities_bp
from routes.reports import reports_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializar extensiones
    db.init_app(app)
    mongo.init_app(app)
    jwt.init_app(app)

    # Crear tablas al iniciar la app
    with app.app_context():
        db.create_all()
        print("Tables created")

    # Registrar Blueprints
    app.register_blueprint(cases_bp, url_prefix='/api/cases')
    app.register_blueprint(documents_bp, url_prefix='/api/documents')
    app.register_blueprint(activities_bp, url_prefix='/api/activities')
    app.register_blueprint(reports_bp, url_prefix='/api/reports')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)

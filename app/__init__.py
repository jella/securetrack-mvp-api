from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask_openapi3 import OpenAPI, Info

# Inicializa extensoes
db = SQLAlchemy()
ma = Marshmallow()

info = Info(
    title="SecureTrack API",
    version="1.0.0",
    description="API para gerenciamento de ativos, controles e conformidades."
)

def create_app():
    app = OpenAPI(__name__, info=info)
    CORS(app, resources={r"/*": {"origins": "http://localhost:8000"}})
    

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dbtrack.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    ma.init_app(app)

    with app.app_context():
        from app.controllers.ativos import ativos_bp
        from app.controllers.controles import controles_bp
        from app.controllers.conformidades import conformidade_bp

        app.register_api(ativos_bp)
        app.register_api(controles_bp)
        app.register_api(conformidade_bp)

        db.create_all()

    return app


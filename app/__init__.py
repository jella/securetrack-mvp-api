from flask import Flask, Response
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask_openapi3 import OpenAPI, Info, Tag, APIBlueprint

# Inicializar extensões
db = SQLAlchemy()
ma = Marshmallow()

def create_app():

    

    app = Flask(__name__)
    CORS(app)


    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dbtrack.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Rota padrão para testar se a API está funcionando
    @app.get("/")
    def index():
            return {"message": "SecureTrack API está funcionando!"}
    

    db.init_app(app)
    ma.init_app(app)
   
    info = Info(title="API de Gestão de implementação de controles de segurança da Informação", version="1.0.0")
    openapi = (app, info)


    
    # Criar as tabelas
    with app.app_context():
        from app.controllers.ativos import ativos_bp
        from app.controllers.controles import controles_bp
        from app.controllers.conformidades import conformidade_bp

        # Registro dos Blueprints
        app.register_blueprint(ativos_bp, url_prefix="/ativos")
        app.register_blueprint(controles_bp, url_prefix="/controles")
        app.register_blueprint(conformidade_bp, url_prefix="/conformidade")
        db.create_all()  




    

    




    

    return app
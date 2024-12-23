from flask import Flask, Response,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask_openapi3 import OpenAPI, Info, Tag, APIBlueprint

# Inicializar extensões
db = SQLAlchemy()
ma = Marshmallow()
info = Info(title="SecureTrack API", description="API para gerenciamento de ativos e controles.", version="1.0.0")

def create_app():

    app = OpenAPI(__name__, info=info)
    CORS(app)



    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dbtrack.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Rota padrão para testar se a API está funcionando
    @app.get("/")
    def index():
               return redirect('/openapi/swagger/')
    

    db.init_app(app)
    ma.init_app(app)
   

    
    # Criar as tabelas
    with app.app_context():
        from app.controllers.ativos import ativos_bp
        from app.controllers.controles import controles_bp
        from app.controllers.conformidades import conformidade_bp

        # Registro dos Blueprints
        # app.register_blueprint(ativos_bp, url_prefix="/ativos")
        # app.register_blueprint(controles_bp, url_prefix="/controles")
        # app.register_blueprint(conformidade_bp, url_prefix="/conformidade")

        

   

        db.create_all()  



# register nested api
    

    




    

    return app
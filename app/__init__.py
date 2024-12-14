from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Inicializar extensões
db = SQLAlchemy()
ma = Marshmallow()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///guardium_mvp.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    ma.init_app(app)

    # Importar blueprints
    from app.controllers.ativos import ativos_bp
    from app.controllers.controles import controles_bp
    from app.controllers.conformidades import conformidade_bp

    # Registrar blueprints
    app.register_blueprint(ativos_bp, url_prefix='/ativos')
    app.register_blueprint(controles_bp, url_prefix='/controles')
    app.register_blueprint(conformidade_bp, url_prefix='/conformidade')

    # Criar as tabelas
    with app.app_context():
        db.create_all()

    return app
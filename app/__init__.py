from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

# Inicializa o SQLAlchemy
db = SQLAlchemy()

def create_app():
    """Função de fábrica para criar e configurar a aplicação Flask."""
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializa o SQLAlchemy com o app
    db.init_app(app)

    # Cria as tabelas no banco de dados
    with app.app_context():
        db.create_all()

    return app

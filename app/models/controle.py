from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Ativo(db.Model):
    """
    Modelo para representar os ativos no sistema.
    """
    __tablename__ = 'ativos'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False, unique=True)
    tipo = db.Column(db.String(50), nullable=False)  # Ex.: Hardware ou Software
    status = db.Column(db.String(50), nullable=False)  # Ex.: Em Produção, etc.
    responsavel = db.Column(db.String(100), nullable=False)
    observacoes = db.Column(db.Text, nullable=True)
    data_alteracao = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f'<Ativo {self.nome}>'

class Controle(db.Model):
    """
    Modelo para representar os controles no sistema.
    """
    __tablename__ = 'controles'

    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(200), nullable=False)
    categoria = db.Column(db.String(50), nullable=False)  # Técnico, Administrativo, etc.
    codigo = db.Column(db.String(50), unique=True, nullable=False)
    anotacoes = db.Column(db.Text, nullable=True)
    data_alteracao = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f'<Controle {self.descricao}>'
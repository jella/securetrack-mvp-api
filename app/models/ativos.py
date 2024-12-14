from app import db
from datetime import datetime

class Ativo(db.Model):
    """Modelo para representar ativos no sistema."""
    __tablename__ = 'ativos'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False, unique=True)
    tipo = db.Column(db.String(50), nullable=False)  # Hardware ou Software
    status = db.Column(db.String(50), nullable=False)  # Em Produção, etc.
    responsavel = db.Column(db.String(100), nullable=False)
    observacoes = db.Column(db.Text, nullable=True)
    data_alteracao = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f'<Ativo {self.nome}>'

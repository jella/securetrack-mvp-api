from app import db

class Ativo(db.Model):
    __tablename__ = 'ativos'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    tipo = db.Column(db.String(50), nullable=False)
    responsavel = db.Column(db.String(100), nullable=False)
    observacoes = db.Column(db.Text, nullable=True)
    status = db.Column(db.String(50), nullable=False)
    data_hora_alteracao = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

# app/models/controle_model.py

    def __repr__(self):
        return f'<Ativo {self.nome}>'

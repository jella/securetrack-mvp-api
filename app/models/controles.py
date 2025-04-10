from app import db

class Controle(db.Model):
    __tablename__ = 'controles'

    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(200), nullable=False)
    categoria = db.Column(db.String(50), nullable=False)
    codigo = db.Column(db.String(50), nullable=False)
    anotacoes = db.Column(db.Text, nullable=True)
    data_hora_alteracao = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    def __repr__(self):
        return f'<Controle {self.descricao}>'
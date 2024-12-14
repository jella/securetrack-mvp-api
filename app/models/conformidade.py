from app import db

class Conformidade(db.Model):
    __tablename__ = 'conformidades'

    id = db.Column(db.Integer, primary_key=True)
    ativo_id = db.Column(db.Integer, db.ForeignKey('ativos.id'), nullable=False)
    controle_id = db.Column(db.Integer, db.ForeignKey('controles.id'), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    data_hora_alteracao = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    ativo = db.relationship('Ativo', backref=db.backref('conformidades', lazy=True))
    controle = db.relationship('Controle', backref=db.backref('conformidades', lazy=True))


    def __repr__(self):
        return f'<Conformidade Ativo:{self.ativo_id} Controle:{self.controle_id}>'

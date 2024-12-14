class Conformidade(db.Model):
    """
    Modelo para representar a conformidade entre ativos e controles.
    """
    __tablename__ = 'conformidade'

    id = db.Column(db.Integer, primary_key=True)
    ativo_id = db.Column(db.Integer, db.ForeignKey('ativos.id'), nullable=False)
    controle_id = db.Column(db.Integer, db.ForeignKey('controles.id'), nullable=False)
    status = db.Column(db.String(50), nullable=False)  # Conforme, Não Conforme, etc.
    data_alteracao = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relacionamentos
    ativo = db.relationship('Ativo', backref=db.backref('conformidades', lazy=True))
    controle = db.relationship('Controle', backref=db.backref('conformidades', lazy=True))

    def __repr__(self):
        return f'<Conformidade Ativo:{self.ativo_id} Controle:{self.controle_id}>'

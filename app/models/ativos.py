from app import db

class Ativo(db.Model):
    __tablename__ = 'ativos'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    tipo = db.Column(db.String(50), nullable=False)
    responsavel = db.Column(db.String(100), nullable=False)
    observacoes = db.Column(db.Text, nullable=True)
    status = db.Column(db.String(50), nullable=False)
    ip = db.Column(db.String(45), nullable=True)  # ✅ novo campo IP (IPv4 ou IPv6)
    data_hora_alteracao = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    def __repr__(self):
        return f'<Ativo {self.nome}>'

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'tipo': self.tipo,
            'responsavel': self.responsavel,
            'observacoes': self.observacoes,
            'status': self.status,
            'ip': self.ip,
            'data_hora_alteracao': self.data_hora_alteracao.isoformat()
        }

    def model_validate(self):
        return AtivoSchema(**self.to_dict())
        
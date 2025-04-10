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


    def __repr__(self):
        return f'<Ativo {self.nome}>'

    def to_dict(self):
        """Método para converter o modelo SQLAlchemy para um dicionário"""
        return {
            'id': self.id,
            'nome': self.nome,
            'tipo': self.tipo,
            'responsavel': self.responsavel,
            'observacoes': self.observacoes,
            'status': self.status,
            'data_hora_alteracao': self.data_hora_alteracao.isoformat()  # Converter datetime para string
        }
    
    def model_validate(self):
        """Método para criar a validação Pydantic a partir do modelo SQLAlchemy"""
        return AtivoSchema(**self.to_dict())  # A conversão para o esquema AtivoSchema
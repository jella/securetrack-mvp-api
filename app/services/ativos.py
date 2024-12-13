from app.models.ativos import Ativo
from app import db

class AtivosService:
    """Serviço para gerenciar operações relacionadas aos Ativos."""

    @staticmethod
    def listar_todos():
        """Lista todos os ativos no banco de dados."""
        return Ativo.query.all()

    @staticmethod
    def criar_ativo(dados):
        """Cria um novo ativo no banco de dados."""
        ativo = Ativo(**dados)
        db.session.add(ativo)
        db.session.commit()


    @staticmethod
    def buscar_por_id(ativo_id):
        """Busca um ativo pelo ID."""
        return Ativo.query.get(ativo_id)

    @staticmethod
    def atualizar_ativo(ativo_id, dados):
        """Atualiza um ativo existente."""
        ativo = Ativo.query.get(ativo_id)
        if ativo:
            for key, value in dados.items():
                setattr(ativo, key, value)
            db.session.commit()
        return ativo

    @staticmethod
    def excluir_ativo(ativo_id):
        """Exclui um ativo pelo ID."""
        ativo = Ativo.query.get(ativo_id)
        if ativo:
            db.session.delete(ativo)
            db.session.commit()
        return ativo

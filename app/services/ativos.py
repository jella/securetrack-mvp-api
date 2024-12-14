from app.models.ativos import Ativo
from app import db


class AtivosService:
    """
    Serviço para operações de CRUD no modelo Ativo.
    """

    @staticmethod
    def listar_todos():
        """
        Lista todos os ativos cadastrados no banco de dados.
        """
        return Ativo.query.all()

    @staticmethod
    def buscar_por_id(ativo_id: int):
        """
        Busca um ativo pelo ID.

        Args:
            ativo_id (int): ID do ativo a ser buscado.

        Returns:
            Ativo ou None: O ativo encontrado ou None se não existir.
        """
        return Ativo.query.filter_by(id=ativo_id).first()

    @staticmethod
    def criar_ativo(dados: dict):
        """
        Cria um novo ativo com os dados fornecidos.

        Args:
            dados (dict): Dados para criar o ativo.

        Returns:
            Ativo: O ativo criado.
        """
        novo_ativo = Ativo(**dados)
        db.session.add(novo_ativo)
        db.session.commit()
        return novo_ativo

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
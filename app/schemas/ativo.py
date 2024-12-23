from pydantic import BaseModel
from typing import List
from datetime import datetime

class NovoAtivoSchema(BaseModel):
    nome: str = 'Sistema Financeiro'
    tipo: str = 'Software'
    responsavel: str = 'HJoaso Alfredo'
    observacoes: str = 'Sistema desenvolvido em java'
    status: str = 'Ativo'


class AtivoSchema(BaseModel):
    id: int = 10
    nome: str = 'Sistema Financeiro'
    tipo: str = 'Software'
    responsavel: str = 'HJoaso Alfredo'
    observacoes: str = 'Sistema desenvolvido em java'
    status: str = 'Ativo'
    data_hora_alteracao: datetime = datetime.now()

class ListaAtivosSchema(BaseModel):
    ativos: List[AtivoSchema] = [
        AtivoSchema(
            id=1,
            nome='Sistema Contábil',
            tipo='Software',
            responsavel='Maria Oliveira',
            observacoes='Desenvolvido em Python',
            status='Ativo',
            data_hora_alteracao=datetime.now()
        ),
        AtivoSchema(
            id=2,
            nome='Servidor de Dados',
            tipo='Hardware',
            responsavel='Carlos Silva',
            observacoes='Servidor de alta performance',
            status='Inativo',
            data_hora_alteracao=datetime.now()
        )
    ]

class RespostaErroSchema(BaseModel):
    error: str
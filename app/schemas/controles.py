from pydantic import BaseModel, RootModel, Field
from typing import List
from datetime import datetime

class ControleSchema(BaseModel):
    """
    Esquema principal para o modelo Controle.
    """
    id: int = 1
    descricao: str = "Controle de acesso lógico."
    categoria: str = "Segurança da informação"
    codigo: str = "AC-01"
    anotacoes: str = "Este controle garante que o acesso aos sistemas seja restrito a usuários autorizados."
    data_hora_alteracao: datetime = datetime(2023, 12, 1, 10, 0, 0)

class NovoControleSchema(BaseModel):
    """
    Esquema para criar um novo controle.
    """
    descricao: str = "Controle de mudanças organizacionais."
    categoria: str = "Gestão de mudanças"
    codigo: str = "CM-02"
    anotacoes: str = "Controle voltado para garantir que as mudanças sejam gerenciadas de forma segura e documentada."

class AtualizaControleSchema(BaseModel):
    """
    Esquema para atualizar um controle existente.
    """
    descricao: str = "Nova descrição do controle de ativos."
    categoria: str = "Gestão de ativos"
    codigo: str = "AT-03"
    anotacoes: str = "Descrição atualizada para refletir mudanças nos requisitos de controle."

class RespostaControleSchema(BaseModel):
    """
    Esquema de resposta detalhada de um controle.
    """
    id: int = 2
    descricao: str = "Gerenciamento de incidentes de segurança."
    categoria: str = "Gestão de incidentes"
    codigo: str = "SI-04"
    anotacoes: str = "Este controle descreve o processo de registro, análise e resposta a incidentes de segurança."
    data_hora_alteracao: datetime = datetime(2023, 11, 15, 16, 30, 0)

class RespostaErroSchema(BaseModel):
    """
    Esquema para respostas de erro.
    """
    mensagem: str = "O controle especificado não foi encontrado."

# Modelo de controle já existente com ID
class ControleSchema(NovoControleSchema):
    id: int
    data_hora_alteracao: datetime = datetime(2023, 12, 1, 10, 0, 0)

    class Config:
        from_attributes = True  # Ajustado para Pydantic v2

# ⚡ Wrapper para lista de ControleSchema com RootModel
class ListaControlesSchema(RootModel[list[ControleSchema]]):
    pass

class ControlePathParams(BaseModel):
    id: int = Field(..., description="ID do usuário")

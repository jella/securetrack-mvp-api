from pydantic import BaseModel
from typing import List
from datetime import datetime

class NovoAtivoSchema(BaseModel):
    nome: str
    tipo: str
    responsavel: str
    observacoes: str
    status: str

class AtivoSchema(BaseModel):
    id: int
    nome: str
    tipo: str
    responsavel: str
    observacoes: str
    status: str
    data_hora_alteracao: datetime

class ListaAtivosSchema(BaseModel):
    ativos: List[AtivoSchema]

class RespostaErroSchema(BaseModel):
    error: str
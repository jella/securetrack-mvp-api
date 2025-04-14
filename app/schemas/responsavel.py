from pydantic import BaseModel, RootModel, Field
from typing import Optional, List
from datetime import datetime


class NovoResponsavelSchema(BaseModel):
    nome: str
    email: str
    status: str


# Definindo o esquema para o responsavel
class ResponsavelSchema(BaseModel):
    id: int
    nome: str 
    email: str
    status: str
    data_hora_alteracao: datetime

    model_config = {
        "from_attributes": True
    }


class ResponsavelPathParams(BaseModel):
    id: int = Field(..., description="ID do usuário")

# ✅ Wrapper para lista de responsaveis
class ListaResponsavelSchema(RootModel[list[ResponsavelSchema]]):
    pass

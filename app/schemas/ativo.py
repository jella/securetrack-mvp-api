from pydantic import BaseModel, RootModel, Field
from typing import Optional, List
from datetime import datetime

class NovoAtivoSchema(BaseModel):
    nome: str
    tipo: str
    responsavel: str
    status: str
    observacoes: Optional[str] = None
    ip: Optional[str] = None 

# Definindo o esquema para o Ativo
class AtivoSchema(BaseModel):
    id: int
    nome: str
    tipo: str
    responsavel: str
    status: str
    observacoes: Optional[str] = None
    data_hora_alteracao: datetime
    ip: Optional[str] = None 
    
    model_config = {
        "from_attributes": True
    }


class AtivoPathParams(BaseModel):
    id: int = Field(..., description="ID do usuário")

# ✅ Wrapper para lista de ativos
class ListaAtivosSchema(RootModel[list[AtivoSchema]]):
    pass

class IpQueryParams(BaseModel):
    ip: str = Field(..., description="Endereço IP do ativo (ex: 8.8.8.8)")

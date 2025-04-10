from pydantic import BaseModel, RootModel
from typing import Optional
from datetime import datetime

# Modelo de entrada para um novo controle
class NovoControleSchema(BaseModel):
    descricao: str
    categoria: str
    codigo: str
    anotacoes: Optional[str] = None

# Modelo de controle já existente com ID
class ControleSchema(NovoControleSchema):
    id: int
    data_hora_alteracao: datetime = datetime(2023, 12, 1, 10, 0, 0)

    class Config:
        from_attributes = True  # Ajustado para Pydantic v2

# ⚡ Wrapper para lista de ControleSchema com RootModel
class ListaControlesSchema(RootModel[list[ControleSchema]]):
    pass

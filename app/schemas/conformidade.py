from pydantic import BaseModel, RootModel, Field
from typing import Optional, Literal
from datetime import datetime, timezone

class NovoConformidadeSchema(BaseModel):
    ativo_id: int
    controle_id: int
    status: Optional[Literal["Pendente", "Andamento", "Implementada"]] = "Pendente"
    observacoes: Optional[str] = None

class ConformidadeSchema(NovoConformidadeSchema):
    id: int
    data_hora_alteracao: Optional[datetime] = None  # ou datetime.now(timezone.utc)

    class Config:
        from_attributes = True

class ListaConformidadesSchema(RootModel[list[ConformidadeSchema]]):
    pass
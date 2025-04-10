from pydantic import BaseModel, RootModel
from typing import Optional
from datetime import datetime

# Modelo de entrada para uma nova conformidade
class NovoConformidadeSchema(BaseModel):
    ativo_id: int
    controle_id: int
    status: Optional[str] = "Pendente"  # Padrão de status "Pendente"
    observacoes: Optional[str] = None

# Modelo de conformidade já existente com ID
class ConformidadeSchema(NovoConformidadeSchema):
    id: int
    data_hora_alteracao: datetime = datetime(2023, 12, 1, 10, 0, 0)

    class Config:
        from_attributes = True  # Para compatibilidade com SQLAlchemy ORM

# ⚡ Wrapper para lista de ConformidadeSchema com RootModel
class ListaConformidadesSchema(RootModel[list[ConformidadeSchema]]):
    pass

from pydantic import BaseModel
from typing import Optional

class RespostaErroSchema(BaseModel):
    mensagem: str
    erro: Optional[str] = None
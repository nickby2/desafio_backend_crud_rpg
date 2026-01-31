from typing import Optional, Dict
from pydantic import BaseModel, validator

class Spell(BaseModel):
    id: int
    nome: str
    nivel: int
    escola: str
    tipo: str
    ritual: bool = False
    descricao: str
    execucao: str
    alcance: str
    alvo: str
    duracao: str

    material: bool = False
    custo_em_ouro: Optional[int] = None
    
    dano_base: Optional[str] = None
    progressao_slot: Optional[Dict[int, str]] = None

    @validator("custo em ouro", always=True)
    def validar_custo_material(cls, v, values):
        if values.get("exige_material") and v is None:
            raise ValueError("Magia com componente material exige custo_em_ouro")
        return v
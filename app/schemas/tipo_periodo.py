from pydantic import BaseModel
import datetime

class TipoPeriodoBase(BaseModel):
    descripcion: str

class TipoPeriodoCreate(TipoPeriodoBase):
    pass

class TipoPeriodoOut(TipoPeriodoBase):
    id_tipo_periodo: int

    class Config:
        orm_mode = True
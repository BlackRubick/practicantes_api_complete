from pydantic import BaseModel
import datetime

class CriterioActitudinalBase(BaseModel):
    descripcion: str

class CriterioActitudinalCreate(CriterioActitudinalBase):
    pass

class CriterioActitudinalOut(CriterioActitudinalBase):
    id_criterio: int

    class Config:
        orm_mode = True
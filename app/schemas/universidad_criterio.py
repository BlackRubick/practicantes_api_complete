from pydantic import BaseModel
import datetime

class UniversidadCriterioBase(BaseModel):
    fk_universidad: int
    fk_criterio: int

class UniversidadCriterioCreate(UniversidadCriterioBase):
    pass

class UniversidadCriterioOut(UniversidadCriterioBase):
    id: int

    class Config:
        orm_mode = True
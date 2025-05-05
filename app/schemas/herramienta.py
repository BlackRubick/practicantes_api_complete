from pydantic import BaseModel
import datetime

class HerramientaBase(BaseModel):
    nombre_herramienta: str

class HerramientaCreate(HerramientaBase):
    pass

class HerramientaOut(HerramientaBase):
    id_herramienta: int

    class Config:
        orm_mode = True
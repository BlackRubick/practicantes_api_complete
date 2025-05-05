from pydantic import BaseModel
import datetime

class LenguajeBase(BaseModel):
    nombre_lenguaje: str

class LenguajeCreate(LenguajeBase):
    pass

class LenguajeOut(LenguajeBase):
    id_lenguaje: int

    class Config:
        orm_mode = True
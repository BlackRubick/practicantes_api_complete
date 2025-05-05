from pydantic import BaseModel
import datetime

class PracticanteLenguajeBase(BaseModel):
    fk_curriculum: int
    fk_lenguaje: int

class PracticanteLenguajeCreate(PracticanteLenguajeBase):
    pass

class PracticanteLenguajeOut(PracticanteLenguajeBase):
    id: int

    class Config:
        orm_mode = True
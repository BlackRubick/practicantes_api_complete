from pydantic import BaseModel
import datetime

class EspecialidadBase(BaseModel):
    nombre_especialidad: str

class EspecialidadCreate(EspecialidadBase):
    pass

class EspecialidadOut(EspecialidadBase):
    id_especialidad: int

    class Config:
        orm_mode = True
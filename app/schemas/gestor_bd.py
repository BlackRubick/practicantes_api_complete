from pydantic import BaseModel
import datetime

class GestorBdBase(BaseModel):
    nombre_gestor: str

class GestorBdCreate(GestorBdBase):
    pass

class GestorBdOut(GestorBdBase):
    id_gestor: int

    class Config:
        orm_mode = True
from pydantic import BaseModel
import datetime

class PracticanteBase(BaseModel):
    nombre_completo: str
    telefono: str
    correo: str
    whatsapp: str
    domicilio: str
    red_social: str
    hobbies: str
    foto: str
    estado_asignacion: bool

class PracticanteCreate(PracticanteBase):
    pass

class PracticanteOut(PracticanteBase):
    id_practicante: int

    class Config:
        orm_mode = True
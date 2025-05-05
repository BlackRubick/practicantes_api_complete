from pydantic import BaseModel
import datetime

class AdministracionBase(BaseModel):
    nombre: str
    cargo: str
    correo: str
    telefono: str

class AdministracionCreate(AdministracionBase):
    pass

class AdministracionOut(AdministracionBase):
    id_administracion: int

    class Config:
        orm_mode = True
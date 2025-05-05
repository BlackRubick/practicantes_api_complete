from pydantic import BaseModel
import datetime

class UniversidadBase(BaseModel):
    nombre: str
    fecha_convenio: datetime.date
    duracion: int

class UniversidadCreate(UniversidadBase):
    pass

class UniversidadOut(UniversidadBase):
    id_universidad: int

    class Config:
        orm_mode = True
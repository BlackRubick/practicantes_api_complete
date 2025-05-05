from pydantic import BaseModel
import datetime

class ActividadBase(BaseModel):
    fk_proyecto: int
    nombre: str
    descripcion: str
    fecha_inicio: datetime.date
    fecha_termino: datetime.date
    culminacion: bool

class ActividadCreate(ActividadBase):
    pass

class ActividadOut(ActividadBase):
    id_actividad: int

    class Config:
        orm_mode = True
from pydantic import BaseModel
import datetime

class ProyectoBase(BaseModel):
    nombre_proyecto: str
    descripcion: str
    fecha_asignacion: datetime.date
    porcentaje_avance: int
    observaciones: str

class ProyectoCreate(ProyectoBase):
    pass

class ProyectoOut(ProyectoBase):
    id_proyecto: int

    class Config:
        orm_mode = True
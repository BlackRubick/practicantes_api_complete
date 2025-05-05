from pydantic import BaseModel
import datetime

class NotificacionBase(BaseModel):
    fecha_envio: datetime.date
    tipo: str
    mensaje: str

class NotificacionCreate(NotificacionBase):
    pass

class NotificacionOut(NotificacionBase):
    id_notificacion: int

    class Config:
        orm_mode = True
from pydantic import BaseModel
import datetime

class NotificacionAdministracionBase(BaseModel):
    fk_notificacion: int
    fk_administracion: int

class NotificacionAdministracionCreate(NotificacionAdministracionBase):
    pass

class NotificacionAdministracionOut(NotificacionAdministracionBase):
    id: int

    class Config:
        orm_mode = True
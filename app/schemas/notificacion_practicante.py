from pydantic import BaseModel
import datetime

class NotificacionPracticanteBase(BaseModel):
    fk_notificacion: int
    fk_practicante: int

class NotificacionPracticanteCreate(NotificacionPracticanteBase):
    pass

class NotificacionPracticanteOut(NotificacionPracticanteBase):
    id: int

    class Config:
        orm_mode = True
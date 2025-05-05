from sqlalchemy import Column, Integer, String, Boolean, Text, Date, ForeignKey
from app.database import Base

class NotificacionAdministracion(Base):
    __tablename__ = "notificacion_administracion"
    id = Column(Integer, primary_key=True, index=True)
    fk_notificacion = Column(Integer, ForeignKey('notificacion.id_notificacion'))
    fk_administracion = Column(Integer, ForeignKey('administracion.id_administracion'))
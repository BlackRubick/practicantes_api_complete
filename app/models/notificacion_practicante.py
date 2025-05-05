from sqlalchemy import Column, Integer, String, Boolean, Text, Date, ForeignKey
from app.database import Base

class NotificacionPracticante(Base):
    __tablename__ = "notificacion_practicante"
    id = Column(Integer, primary_key=True, index=True)
    fk_notificacion = Column(Integer, ForeignKey('notificacion.id_notificacion'))
    fk_practicante = Column(Integer, ForeignKey('practicante.id_practicante'))
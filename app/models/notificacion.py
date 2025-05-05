from sqlalchemy import Column, Integer, String, Boolean, Text, Date, ForeignKey
from app.database import Base

class Notificacion(Base):
    __tablename__ = "notificacion"
    id_notificacion = Column(Integer, primary_key=True, index=True)
    fecha_envio = Column(Date)
    tipo = Column(String(255))
    mensaje = Column(Text)
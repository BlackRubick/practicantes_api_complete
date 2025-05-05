from sqlalchemy import Column, Integer, String, Boolean, Text, Date, ForeignKey
from app.database import Base

class Administracion(Base):
    __tablename__ = "administracion"
    id_administracion = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255))
    cargo = Column(String(255))
    correo = Column(String(255))
    telefono = Column(String(255))
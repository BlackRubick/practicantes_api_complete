from sqlalchemy import Column, Integer, String, Boolean, Text, Date, ForeignKey
from app.database import Base

class Cuenta(Base):
    __tablename__ = "cuenta"
    id_cuenta = Column(Integer, primary_key=True, index=True)
    username = Column(String(255))
    password = Column(String(255))
    rol = Column(String(255))
    fk_practicante = Column(Integer, ForeignKey('practicante.id_practicante'), unique=True)
    fk_administracion = Column(Integer, ForeignKey('administracion.id_administracion'), unique=True)
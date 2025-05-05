from sqlalchemy import Column, Integer, String, Boolean, Text, Date, ForeignKey
from app.database import Base

class GestorBd(Base):
    __tablename__ = "gestor_bd"
    id_gestor = Column(Integer, primary_key=True, index=True)
    nombre_gestor = Column(String(255))
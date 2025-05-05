from sqlalchemy import Column, Integer, String, Boolean, Text, Date, ForeignKey
from app.database import Base

class Especialidad(Base):
    __tablename__ = "especialidad"
    id_especialidad = Column(Integer, primary_key=True, index=True)
    nombre_especialidad = Column(String(255))
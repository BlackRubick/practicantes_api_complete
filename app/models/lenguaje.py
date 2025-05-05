from sqlalchemy import Column, Integer, String, Boolean, Text, Date, ForeignKey
from app.database import Base

class Lenguaje(Base):
    __tablename__ = "lenguaje"
    id_lenguaje = Column(Integer, primary_key=True, index=True)
    nombre_lenguaje = Column(String(255))
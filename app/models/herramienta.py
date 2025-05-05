from sqlalchemy import Column, Integer, String, Boolean, Text, Date, ForeignKey
from app.database import Base

class Herramienta(Base):
    __tablename__ = "herramienta"
    id_herramienta = Column(Integer, primary_key=True, index=True)
    nombre_herramienta = Column(String(255))
from sqlalchemy import Column, Integer, String, Boolean, Text, Date, ForeignKey
from app.database import Base

class TipoPeriodo(Base):
    __tablename__ = "tipo_periodo"
    id_tipo_periodo = Column(Integer, primary_key=True, index=True)
    descripcion = Column(String(255))
from sqlalchemy import Column, Integer, String, Boolean, Text, Date, ForeignKey
from app.database import Base

class CriterioActitudinal(Base):
    __tablename__ = "criterio_actitudinal"
    id_criterio = Column(Integer, primary_key=True, index=True)
    descripcion = Column(String(255))
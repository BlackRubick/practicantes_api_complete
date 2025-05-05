from sqlalchemy import Column, Integer, String, Boolean, Text, Date, ForeignKey
from app.database import Base

class Documentacion(Base):
    __tablename__ = "documentacion"
    id_documentacion = Column(Integer, primary_key=True, index=True)
    fk_proyecto = Column(Integer, ForeignKey('proyecto.id_proyecto'))
    nombre_doc = Column(String(255))
    ruta = Column(String(255))
    fecha_subida = Column(Date)
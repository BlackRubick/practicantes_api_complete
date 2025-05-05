from sqlalchemy import Column, Integer, String, Boolean, Text, Date, ForeignKey
from app.database import Base

class Actividad(Base):
    __tablename__ = "actividad"
    id_actividad = Column(Integer, primary_key=True, index=True)
    fk_proyecto = Column(Integer, ForeignKey('proyecto.id_proyecto'))
    nombre = Column(String(255))
    descripcion = Column(Text)
    fecha_inicio = Column(Date)
    fecha_termino = Column(Date)
    culminacion = Column(Boolean)
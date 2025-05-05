from sqlalchemy import Column, Integer, String, Boolean, Text, Date, ForeignKey
from app.database import Base

class Proyecto(Base):
    __tablename__ = "proyecto"
    id_proyecto = Column(Integer, primary_key=True, index=True)
    nombre_proyecto = Column(String(255))
    descripcion = Column(Text)
    fecha_asignacion = Column(Date)
    porcentaje_avance = Column(Integer)
    observaciones = Column(Text)
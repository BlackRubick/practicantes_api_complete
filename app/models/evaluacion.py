from sqlalchemy import Column, Integer, String, Boolean, Text, Date, ForeignKey
from app.database import Base

class Evaluacion(Base):
    __tablename__ = "evaluacion"
    id_evaluacion = Column(Integer, primary_key=True, index=True)
    fk_curriculum = Column(Integer, ForeignKey('curriculum.id_curriculum'))
    fk_proyecto = Column(Integer, ForeignKey('proyecto.id_proyecto'))
    fecha_evaluacion = Column(Date)
    fk_universidad = Column(Integer, ForeignKey('universidad.id_universidad'))
    fk_administracion = Column(Integer, ForeignKey('administracion.id_administracion'))
    es_evaluacion_activa = Column(Boolean, default=True)
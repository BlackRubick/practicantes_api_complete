from sqlalchemy import Column, Integer, String, Boolean, Text, Date, ForeignKey
from app.database import Base

class EvaluacionActitudinal(Base):
    __tablename__ = "evaluacion_actitudinal"
    id_eval_actitudinal = Column(Integer, primary_key=True, index=True)
    fk_evaluacion = Column(Integer, ForeignKey('evaluacion.id_evaluacion'))
    fk_criterio = Column(Integer, ForeignKey('criterio_actitudinal.id_criterio'))
    puntuacion = Column(Integer)
    comentarios = Column(Text)
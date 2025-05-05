from sqlalchemy import Column, Integer, String, Boolean, Text, Date, ForeignKey
from app.database import Base

class Curriculum(Base):
    __tablename__ = "curriculum"
    id_curriculum = Column(Integer, primary_key=True, index=True)
    fk_practicante = Column(Integer, ForeignKey('practicante.id_practicante'))
    fecha_registro = Column(Date)
    periodo_practicas = Column(String(255))
    fk_universidad = Column(Integer, ForeignKey('universidad.id_universidad'))
    fk_tipo_periodo = Column(Integer, ForeignKey('tipo_periodo.id_tipo_periodo'))
    fk_especialidad = Column(Integer, ForeignKey('especialidad.id_especialidad'))
    grado = Column(Integer)
    github = Column(String(255))
    nivel_ingles = Column(String(255))
    fecha_inicio = Column(Date)
    fecha_termino = Column(Date)
    numero_semanas = Column(Integer)
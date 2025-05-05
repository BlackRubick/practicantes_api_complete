from sqlalchemy import Column, Integer, String, Boolean, Text, Date, ForeignKey
from app.database import Base

class CurriculumGestorBd(Base):
    __tablename__ = "curriculum_gestor_bd"
    id = Column(Integer, primary_key=True, index=True)
    fk_curriculum = Column(Integer, ForeignKey('curriculum.id_curriculum'))
    fk_gestor = Column(Integer, ForeignKey('gestor_bd.id_gestor'))
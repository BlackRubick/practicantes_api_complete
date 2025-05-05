from sqlalchemy import Column, Integer, String, Boolean, Text, Date, ForeignKey
from app.database import Base

class CurriculumProyecto(Base):
    __tablename__ = "curriculum_proyecto"
    id = Column(Integer, primary_key=True, index=True)
    fk_curriculum = Column(Integer, ForeignKey('curriculum.id_curriculum'))
    fk_proyecto = Column(Integer, ForeignKey('proyecto.id_proyecto'))
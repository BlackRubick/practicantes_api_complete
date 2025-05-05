from sqlalchemy import Column, Integer, String, Boolean, Text, Date, ForeignKey
from app.database import Base

class CurriculumHerramienta(Base):
    __tablename__ = "curriculum_herramienta"
    id = Column(Integer, primary_key=True, index=True)
    fk_curriculum = Column(Integer, ForeignKey('curriculum.id_curriculum'))
    fk_herramienta = Column(Integer, ForeignKey('herramienta.id_herramienta'))
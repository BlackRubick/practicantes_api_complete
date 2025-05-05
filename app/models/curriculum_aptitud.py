from sqlalchemy import Column, Integer, String, Boolean, Text, Date, ForeignKey
from app.database import Base

class CurriculumAptitud(Base):
    __tablename__ = "curriculum_aptitud"
    id = Column(Integer, primary_key=True, index=True)
    fk_curriculum = Column(Integer, ForeignKey('curriculum.id_curriculum'))
    fk_aptitud = Column(Integer, ForeignKey('aptitud.id_aptitud'))
    valor = Column(Boolean)
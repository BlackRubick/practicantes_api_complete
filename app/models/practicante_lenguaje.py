from sqlalchemy import Column, Integer, String, Boolean, Text, Date, ForeignKey
from app.database import Base

class PracticanteLenguaje(Base):
    __tablename__ = "practicante_lenguaje"
    id = Column(Integer, primary_key=True, index=True)
    fk_curriculum = Column(Integer, ForeignKey('curriculum.id_curriculum'))
    fk_lenguaje = Column(Integer, ForeignKey('lenguaje.id_lenguaje'))
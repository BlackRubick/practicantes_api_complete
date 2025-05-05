from sqlalchemy import Column, Integer, String, Boolean, Text, Date, ForeignKey
from app.database import Base

class UniversidadCriterio(Base):
    __tablename__ = "universidad_criterio"
    id = Column(Integer, primary_key=True, index=True)
    fk_universidad = Column(Integer, ForeignKey('universidad.id_universidad'))
    fk_criterio = Column(Integer, ForeignKey('criterio_actitudinal.id_criterio'))
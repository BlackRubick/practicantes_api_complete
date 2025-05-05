from sqlalchemy import Column, Integer, String, Boolean, Text, Date, ForeignKey
from app.database import Base

class Universidad(Base):
    __tablename__ = "universidad"
    id_universidad = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255))
    fecha_convenio = Column(Date)
    duracion = Column(Integer)
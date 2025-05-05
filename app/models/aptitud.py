from sqlalchemy import Column, Integer, String, Boolean, Text, Date, ForeignKey
from app.database import Base

class Aptitud(Base):
    __tablename__ = "aptitud"
    id_aptitud = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255))
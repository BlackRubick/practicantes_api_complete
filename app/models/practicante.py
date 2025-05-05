from sqlalchemy import Column, Integer, String, Boolean, Text
from app.database import Base

class Practicante(Base):
    __tablename__ = "practicante"

    id_practicante    = Column(Integer, primary_key=True, index=True)
    nombre_completo   = Column(String(255))
    telefono          = Column(String(100))
    correo            = Column(String(150))
    whatsapp          = Column(String(20))
    domicilio         = Column(Text)
    red_social        = Column(String(200))
    hobbies           = Column(Text)
    foto              = Column(String(255))
    estado_asignacion = Column(Boolean, default=False)

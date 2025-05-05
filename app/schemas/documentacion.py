from pydantic import BaseModel
import datetime

class DocumentacionBase(BaseModel):
    fk_proyecto: int
    nombre_doc: str
    ruta: str
    fecha_subida: datetime.date

class DocumentacionCreate(DocumentacionBase):
    pass

class DocumentacionOut(DocumentacionBase):
    id_documentacion: int

    class Config:
        orm_mode = True
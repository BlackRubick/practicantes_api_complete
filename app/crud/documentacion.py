from sqlalchemy.orm import Session
from app.models.documentacion import Documentacion
from app.schemas.documentacion import DocumentacionCreate

def create_documentacion(db: Session, item: DocumentacionCreate):
    db_item = Documentacion(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_documentacions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Documentacion).offset(skip).limit(limit).all()

def get_documentacion_by_id(db: Session, id: int):
    return db.query(Documentacion).filter(Documentacion.id_documentacion == id).first()

def delete_documentacion(db: Session, id: int):
    obj = db.query(Documentacion).filter(Documentacion.id_documentacion == id).first()
    if obj:
        db.delete(obj)
        db.commit()
    return obj
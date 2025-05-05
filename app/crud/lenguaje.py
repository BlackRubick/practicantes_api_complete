from sqlalchemy.orm import Session
from app.models.lenguaje import Lenguaje
from app.schemas.lenguaje import LenguajeCreate

def create_lenguaje(db: Session, item: LenguajeCreate):
    db_item = Lenguaje(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_lenguajes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Lenguaje).offset(skip).limit(limit).all()

def get_lenguaje_by_id(db: Session, id: int):
    return db.query(Lenguaje).filter(Lenguaje.id_lenguaje == id).first()

def delete_lenguaje(db: Session, id: int):
    obj = db.query(Lenguaje).filter(Lenguaje.id_lenguaje == id).first()
    if obj:
        db.delete(obj)
        db.commit()
    return obj
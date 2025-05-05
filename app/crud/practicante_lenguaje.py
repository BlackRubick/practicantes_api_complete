from sqlalchemy.orm import Session
from app.models.practicante_lenguaje import PracticanteLenguaje
from app.schemas.practicante_lenguaje import PracticanteLenguajeCreate

def create_practicante_lenguaje(db: Session, item: PracticanteLenguajeCreate):
    db_item = PracticanteLenguaje(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_practicante_lenguajes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(PracticanteLenguaje).offset(skip).limit(limit).all()

def get_practicante_lenguaje_by_id(db: Session, id: int):
    return db.query(PracticanteLenguaje).filter(PracticanteLenguaje.id == id).first()

def delete_practicante_lenguaje(db: Session, id: int):
    obj = db.query(PracticanteLenguaje).filter(PracticanteLenguaje.id == id).first()
    if obj:
        db.delete(obj)
        db.commit()
    return obj
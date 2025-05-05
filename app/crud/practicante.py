from sqlalchemy.orm import Session
from app.models.practicante import Practicante
from app.schemas.practicante import PracticanteCreate

def create_practicante(db: Session, item: PracticanteCreate):
    db_item = Practicante(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_practicantes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Practicante).offset(skip).limit(limit).all()

def get_practicante_by_id(db: Session, id: int):
    return db.query(Practicante).filter(Practicante.id_practicante == id).first()

def delete_practicante(db: Session, id: int):
    obj = db.query(Practicante).filter(Practicante.id_practicante == id).first()
    if obj:
        db.delete(obj)
        db.commit()
    return obj
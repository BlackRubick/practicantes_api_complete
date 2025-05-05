from sqlalchemy.orm import Session
from app.models.herramienta import Herramienta
from app.schemas.herramienta import HerramientaCreate

def create_herramienta(db: Session, item: HerramientaCreate):
    db_item = Herramienta(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_herramientas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Herramienta).offset(skip).limit(limit).all()

def get_herramienta_by_id(db: Session, id: int):
    return db.query(Herramienta).filter(Herramienta.id_herramienta == id).first()

def delete_herramienta(db: Session, id: int):
    obj = db.query(Herramienta).filter(Herramienta.id_herramienta == id).first()
    if obj:
        db.delete(obj)
        db.commit()
    return obj
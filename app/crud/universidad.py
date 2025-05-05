from sqlalchemy.orm import Session
from app.models.universidad import Universidad
from app.schemas.universidad import UniversidadCreate

def create_universidad(db: Session, item: UniversidadCreate):
    db_item = Universidad(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_universidads(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Universidad).offset(skip).limit(limit).all()

def get_universidad_by_id(db: Session, id: int):
    return db.query(Universidad).filter(Universidad.id_universidad == id).first()

def delete_universidad(db: Session, id: int):
    obj = db.query(Universidad).filter(Universidad.id_universidad == id).first()
    if obj:
        db.delete(obj)
        db.commit()
    return obj
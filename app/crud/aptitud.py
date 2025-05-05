from sqlalchemy.orm import Session
from app.models.aptitud import Aptitud
from app.schemas.aptitud import AptitudCreate

def create_aptitud(db: Session, item: AptitudCreate):
    db_item = Aptitud(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_aptituds(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Aptitud).offset(skip).limit(limit).all()

def get_aptitud_by_id(db: Session, id: int):
    return db.query(Aptitud).filter(Aptitud.id_aptitud == id).first()

def delete_aptitud(db: Session, id: int):
    obj = db.query(Aptitud).filter(Aptitud.id_aptitud == id).first()
    if obj:
        db.delete(obj)
        db.commit()
    return obj
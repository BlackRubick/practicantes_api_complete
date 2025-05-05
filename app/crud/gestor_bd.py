from sqlalchemy.orm import Session
from app.models.gestor_bd import GestorBd
from app.schemas.gestor_bd import GestorBdCreate

def create_gestor_bd(db: Session, item: GestorBdCreate):
    db_item = GestorBd(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_gestor_bds(db: Session, skip: int = 0, limit: int = 100):
    return db.query(GestorBd).offset(skip).limit(limit).all()

def get_gestor_bd_by_id(db: Session, id: int):
    return db.query(GestorBd).filter(GestorBd.id_gestor == id).first()

def delete_gestor_bd(db: Session, id: int):
    obj = db.query(GestorBd).filter(GestorBd.id_gestor == id).first()
    if obj:
        db.delete(obj)
        db.commit()
    return obj
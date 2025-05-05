from sqlalchemy.orm import Session
from app.models.proyecto import Proyecto
from app.schemas.proyecto import ProyectoCreate

def create_proyecto(db: Session, item: ProyectoCreate):
    db_item = Proyecto(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_proyectos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Proyecto).offset(skip).limit(limit).all()

def get_proyecto_by_id(db: Session, id: int):
    return db.query(Proyecto).filter(Proyecto.id_proyecto == id).first()

def delete_proyecto(db: Session, id: int):
    obj = db.query(Proyecto).filter(Proyecto.id_proyecto == id).first()
    if obj:
        db.delete(obj)
        db.commit()
    return obj
from sqlalchemy.orm import Session
from app.models.actividad import Actividad
from app.schemas.actividad import ActividadCreate

def create_actividad(db: Session, item: ActividadCreate):
    db_item = Actividad(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_actividads(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Actividad).offset(skip).limit(limit).all()

def get_actividad_by_id(db: Session, id: int):
    return db.query(Actividad).filter(Actividad.id_actividad == id).first()

def delete_actividad(db: Session, id: int):
    obj = db.query(Actividad).filter(Actividad.id_actividad == id).first()
    if obj:
        db.delete(obj)
        db.commit()
    return obj
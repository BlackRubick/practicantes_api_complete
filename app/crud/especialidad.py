from sqlalchemy.orm import Session
from app.models.especialidad import Especialidad
from app.schemas.especialidad import EspecialidadCreate

def create_especialidad(db: Session, item: EspecialidadCreate):
    db_item = Especialidad(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_especialidads(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Especialidad).offset(skip).limit(limit).all()

def get_especialidad_by_id(db: Session, id: int):
    return db.query(Especialidad).filter(Especialidad.id_especialidad == id).first()

def delete_especialidad(db: Session, id: int):
    obj = db.query(Especialidad).filter(Especialidad.id_especialidad == id).first()
    if obj:
        db.delete(obj)
        db.commit()
    return obj
from sqlalchemy.orm import Session
from app.models.administracion import Administracion
from app.schemas.administracion import AdministracionCreate

def create_administracion(db: Session, item: AdministracionCreate):
    db_item = Administracion(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_administracions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Administracion).offset(skip).limit(limit).all()

def get_administracion_by_id(db: Session, id: int):
    return db.query(Administracion).filter(Administracion.id_administracion == id).first()

def delete_administracion(db: Session, id: int):
    obj = db.query(Administracion).filter(Administracion.id_administracion == id).first()
    if obj:
        db.delete(obj)
        db.commit()
    return obj
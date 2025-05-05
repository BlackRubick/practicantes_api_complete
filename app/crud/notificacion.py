from sqlalchemy.orm import Session
from app.models.notificacion import Notificacion
from app.schemas.notificacion import NotificacionCreate

def create_notificacion(db: Session, item: NotificacionCreate):
    db_item = Notificacion(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_notificacions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Notificacion).offset(skip).limit(limit).all()

def get_notificacion_by_id(db: Session, id: int):
    return db.query(Notificacion).filter(Notificacion.id_notificacion == id).first()

def delete_notificacion(db: Session, id: int):
    obj = db.query(Notificacion).filter(Notificacion.id_notificacion == id).first()
    if obj:
        db.delete(obj)
        db.commit()
    return obj
from sqlalchemy.orm import Session
from app.models.notificacion_administracion import NotificacionAdministracion
from app.schemas.notificacion_administracion import NotificacionAdministracionCreate

def create_notificacion_administracion(db: Session, item: NotificacionAdministracionCreate):
    db_item = NotificacionAdministracion(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_notificacion_administracions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(NotificacionAdministracion).offset(skip).limit(limit).all()

def get_notificacion_administracion_by_id(db: Session, id: int):
    return db.query(NotificacionAdministracion).filter(NotificacionAdministracion.id == id).first()

def delete_notificacion_administracion(db: Session, id: int):
    obj = db.query(NotificacionAdministracion).filter(NotificacionAdministracion.id == id).first()
    if obj:
        db.delete(obj)
        db.commit()
    return obj
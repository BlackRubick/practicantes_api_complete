from sqlalchemy.orm import Session
from app.models.notificacion_practicante import NotificacionPracticante
from app.schemas.notificacion_practicante import NotificacionPracticanteCreate

def create_notificacion_practicante(db: Session, item: NotificacionPracticanteCreate):
    db_item = NotificacionPracticante(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_notificacion_practicantes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(NotificacionPracticante).offset(skip).limit(limit).all()

def get_notificacion_practicante_by_id(db: Session, id: int):
    return db.query(NotificacionPracticante).filter(NotificacionPracticante.id == id).first()

def delete_notificacion_practicante(db: Session, id: int):
    obj = db.query(NotificacionPracticante).filter(NotificacionPracticante.id == id).first()
    if obj:
        db.delete(obj)
        db.commit()
    return obj
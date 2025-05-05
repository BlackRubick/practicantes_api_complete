from sqlalchemy.orm import Session
from app.models.evaluacion import Evaluacion
from app.schemas.evaluacion import EvaluacionCreate

def create_evaluacion(db: Session, item: EvaluacionCreate):
    db_item = Evaluacion(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_evaluacions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Evaluacion).offset(skip).limit(limit).all()

def get_evaluacion_by_id(db: Session, id: int):
    return db.query(Evaluacion).filter(Evaluacion.id_evaluacion == id).first()

def delete_evaluacion(db: Session, id: int):
    obj = db.query(Evaluacion).filter(Evaluacion.id_evaluacion == id).first()
    if obj:
        db.delete(obj)
        db.commit()
    return obj
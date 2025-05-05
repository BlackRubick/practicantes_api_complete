from sqlalchemy.orm import Session
from app.models.evaluacion_actitudinal import EvaluacionActitudinal
from app.schemas.evaluacion_actitudinal import EvaluacionActitudinalCreate

def create_evaluacion_actitudinal(db: Session, item: EvaluacionActitudinalCreate):
    db_item = EvaluacionActitudinal(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_evaluacion_actitudinals(db: Session, skip: int = 0, limit: int = 100):
    return db.query(EvaluacionActitudinal).offset(skip).limit(limit).all()

def get_evaluacion_actitudinal_by_id(db: Session, id: int):
    return db.query(EvaluacionActitudinal).filter(EvaluacionActitudinal.id_eval_actitudinal == id).first()

def delete_evaluacion_actitudinal(db: Session, id: int):
    obj = db.query(EvaluacionActitudinal).filter(EvaluacionActitudinal.id_eval_actitudinal == id).first()
    if obj:
        db.delete(obj)
        db.commit()
    return obj
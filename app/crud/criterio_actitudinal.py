from sqlalchemy.orm import Session
from app.models.criterio_actitudinal import CriterioActitudinal
from app.schemas.criterio_actitudinal import CriterioActitudinalCreate

def create_criterio_actitudinal(db: Session, item: CriterioActitudinalCreate):
    db_item = CriterioActitudinal(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_criterio_actitudinals(db: Session, skip: int = 0, limit: int = 100):
    return db.query(CriterioActitudinal).offset(skip).limit(limit).all()

def get_criterio_actitudinal_by_id(db: Session, id: int):
    return db.query(CriterioActitudinal).filter(CriterioActitudinal.id_criterio == id).first()

def delete_criterio_actitudinal(db: Session, id: int):
    obj = db.query(CriterioActitudinal).filter(CriterioActitudinal.id_criterio == id).first()
    if obj:
        db.delete(obj)
        db.commit()
    return obj
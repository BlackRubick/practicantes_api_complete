from sqlalchemy.orm import Session
from app.models.tipo_periodo import TipoPeriodo
from app.schemas.tipo_periodo import TipoPeriodoCreate

def create_tipo_periodo(db: Session, item: TipoPeriodoCreate):
    db_item = TipoPeriodo(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_tipo_periodos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(TipoPeriodo).offset(skip).limit(limit).all()

def get_tipo_periodo_by_id(db: Session, id: int):
    return db.query(TipoPeriodo).filter(TipoPeriodo.id_tipo_periodo == id).first()

def delete_tipo_periodo(db: Session, id: int):
    obj = db.query(TipoPeriodo).filter(TipoPeriodo.id_tipo_periodo == id).first()
    if obj:
        db.delete(obj)
        db.commit()
    return obj
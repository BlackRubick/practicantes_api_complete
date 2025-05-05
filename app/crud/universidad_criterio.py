from sqlalchemy.orm import Session
from app.models.universidad_criterio import UniversidadCriterio
from app.schemas.universidad_criterio import UniversidadCriterioCreate

def create_universidad_criterio(db: Session, item: UniversidadCriterioCreate):
    db_item = UniversidadCriterio(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_universidad_criterios(db: Session, skip: int = 0, limit: int = 100):
    return db.query(UniversidadCriterio).offset(skip).limit(limit).all()

def get_universidad_criterio_by_id(db: Session, id: int):
    return db.query(UniversidadCriterio).filter(UniversidadCriterio.id == id).first()

def delete_universidad_criterio(db: Session, id: int):
    obj = db.query(UniversidadCriterio).filter(UniversidadCriterio.id == id).first()
    if obj:
        db.delete(obj)
        db.commit()
    return obj
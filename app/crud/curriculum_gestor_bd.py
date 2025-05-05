from sqlalchemy.orm import Session
from app.models.curriculum_gestor_bd import CurriculumGestorBd
from app.schemas.curriculum_gestor_bd import CurriculumGestorBdCreate

def create_curriculum_gestor_bd(db: Session, item: CurriculumGestorBdCreate):
    db_item = CurriculumGestorBd(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_curriculum_gestor_bds(db: Session, skip: int = 0, limit: int = 100):
    return db.query(CurriculumGestorBd).offset(skip).limit(limit).all()

def get_curriculum_gestor_bd_by_id(db: Session, id: int):
    return db.query(CurriculumGestorBd).filter(CurriculumGestorBd.id == id).first()

def delete_curriculum_gestor_bd(db: Session, id: int):
    obj = db.query(CurriculumGestorBd).filter(CurriculumGestorBd.id == id).first()
    if obj:
        db.delete(obj)
        db.commit()
    return obj
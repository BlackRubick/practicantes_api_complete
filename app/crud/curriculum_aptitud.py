from sqlalchemy.orm import Session
from app.models.curriculum_aptitud import CurriculumAptitud
from app.schemas.curriculum_aptitud import CurriculumAptitudCreate

def create_curriculum_aptitud(db: Session, item: CurriculumAptitudCreate):
    db_item = CurriculumAptitud(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_curriculum_aptituds(db: Session, skip: int = 0, limit: int = 100):
    return db.query(CurriculumAptitud).offset(skip).limit(limit).all()

def get_curriculum_aptitud_by_id(db: Session, id: int):
    return db.query(CurriculumAptitud).filter(CurriculumAptitud.id == id).first()

def delete_curriculum_aptitud(db: Session, id: int):
    obj = db.query(CurriculumAptitud).filter(CurriculumAptitud.id == id).first()
    if obj:
        db.delete(obj)
        db.commit()
    return obj
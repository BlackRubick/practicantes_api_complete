from sqlalchemy.orm import Session
from app.models.curriculum import Curriculum
from app.schemas.curriculum import CurriculumCreate

def create_curriculum(db: Session, item: CurriculumCreate):
    db_item = Curriculum(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_curriculums(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Curriculum).offset(skip).limit(limit).all()

def get_curriculum_by_id(db: Session, id: int):
    return db.query(Curriculum).filter(Curriculum.id_curriculum == id).first()

def delete_curriculum(db: Session, id: int):
    obj = db.query(Curriculum).filter(Curriculum.id_curriculum == id).first()
    if obj:
        db.delete(obj)
        db.commit()
    return obj
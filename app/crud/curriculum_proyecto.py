from sqlalchemy.orm import Session
from app.models.curriculum_proyecto import CurriculumProyecto
from app.schemas.curriculum_proyecto import CurriculumProyectoCreate

def create_curriculum_proyecto(db: Session, item: CurriculumProyectoCreate):
    db_item = CurriculumProyecto(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_curriculum_proyectos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(CurriculumProyecto).offset(skip).limit(limit).all()

def get_curriculum_proyecto_by_id(db: Session, id: int):
    return db.query(CurriculumProyecto).filter(CurriculumProyecto.id == id).first()

def delete_curriculum_proyecto(db: Session, id: int):
    obj = db.query(CurriculumProyecto).filter(CurriculumProyecto.id == id).first()
    if obj:
        db.delete(obj)
        db.commit()
    return obj
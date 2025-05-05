from sqlalchemy.orm import Session
from app.models.curriculum_herramienta import CurriculumHerramienta
from app.schemas.curriculum_herramienta import CurriculumHerramientaCreate

def create_curriculum_herramienta(db: Session, item: CurriculumHerramientaCreate):
    db_item = CurriculumHerramienta(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_curriculum_herramientas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(CurriculumHerramienta).offset(skip).limit(limit).all()

def get_curriculum_herramienta_by_id(db: Session, id: int):
    return db.query(CurriculumHerramienta).filter(CurriculumHerramienta.id == id).first()

def delete_curriculum_herramienta(db: Session, id: int):
    obj = db.query(CurriculumHerramienta).filter(CurriculumHerramienta.id == id).first()
    if obj:
        db.delete(obj)
        db.commit()
    return obj
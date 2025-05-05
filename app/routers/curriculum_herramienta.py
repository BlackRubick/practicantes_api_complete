from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.curriculum_herramienta import CurriculumHerramientaCreate, CurriculumHerramientaOut
from app.crud import curriculum_herramienta as crud

router = APIRouter(prefix="/curriculum_herramienta", tags=["CurriculumHerramienta"])

@router.post("/", response_model=CurriculumHerramientaOut)
def create_item(item: CurriculumHerramientaCreate, db: Session = Depends(get_db)):
    return crud.create_curriculum_herramienta(db, item)

@router.get("/", response_model=list[CurriculumHerramientaOut])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_curriculum_herramientas(db, skip=skip, limit=limit)

@router.get("/{item_id}", response_model=CurriculumHerramientaOut)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_obj = crud.get_curriculum_herramienta_by_id(db, item_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Not found")
    return db_obj

@router.delete("/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    obj = crud.delete_curriculum_herramienta(db, item_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    return {"detail": "Deleted"}
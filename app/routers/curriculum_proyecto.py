from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.curriculum_proyecto import CurriculumProyectoCreate, CurriculumProyectoOut
from app.crud import curriculum_proyecto as crud

router = APIRouter(prefix="/curriculum_proyecto", tags=["CurriculumProyecto"])

@router.post("/", response_model=CurriculumProyectoOut)
def create_item(item: CurriculumProyectoCreate, db: Session = Depends(get_db)):
    return crud.create_curriculum_proyecto(db, item)

@router.get("/", response_model=list[CurriculumProyectoOut])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_curriculum_proyectos(db, skip=skip, limit=limit)

@router.get("/{item_id}", response_model=CurriculumProyectoOut)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_obj = crud.get_curriculum_proyecto_by_id(db, item_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Not found")
    return db_obj

@router.delete("/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    obj = crud.delete_curriculum_proyecto(db, item_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    return {"detail": "Deleted"}
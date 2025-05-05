from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.curriculum_aptitud import CurriculumAptitudCreate, CurriculumAptitudOut
from app.crud import curriculum_aptitud as crud

router = APIRouter(prefix="/curriculum_aptitud", tags=["CurriculumAptitud"])

@router.post("/", response_model=CurriculumAptitudOut)
def create_item(item: CurriculumAptitudCreate, db: Session = Depends(get_db)):
    return crud.create_curriculum_aptitud(db, item)

@router.get("/", response_model=list[CurriculumAptitudOut])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_curriculum_aptituds(db, skip=skip, limit=limit)

@router.get("/{item_id}", response_model=CurriculumAptitudOut)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_obj = crud.get_curriculum_aptitud_by_id(db, item_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Not found")
    return db_obj

@router.delete("/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    obj = crud.delete_curriculum_aptitud(db, item_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    return {"detail": "Deleted"}
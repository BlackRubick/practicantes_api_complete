from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.curriculum import CurriculumCreate, CurriculumOut
from app.crud import curriculum as crud

router = APIRouter(prefix="/curriculum", tags=["Curriculum"])

@router.post("/", response_model=CurriculumOut)
def create_item(item: CurriculumCreate, db: Session = Depends(get_db)):
    return crud.create_curriculum(db, item)

@router.get("/", response_model=list[CurriculumOut])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_curriculums(db, skip=skip, limit=limit)

@router.get("/{item_id}", response_model=CurriculumOut)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_obj = crud.get_curriculum_by_id(db, item_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Not found")
    return db_obj

@router.delete("/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    obj = crud.delete_curriculum(db, item_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    return {"detail": "Deleted"}
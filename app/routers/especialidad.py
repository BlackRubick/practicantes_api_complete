from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.especialidad import EspecialidadCreate, EspecialidadOut
from app.crud import especialidad as crud

router = APIRouter(prefix="/especialidad", tags=["Especialidad"])

@router.post("/", response_model=EspecialidadOut)
def create_item(item: EspecialidadCreate, db: Session = Depends(get_db)):
    return crud.create_especialidad(db, item)

@router.get("/", response_model=list[EspecialidadOut])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_especialidads(db, skip=skip, limit=limit)

@router.get("/{item_id}", response_model=EspecialidadOut)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_obj = crud.get_especialidad_by_id(db, item_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Not found")
    return db_obj

@router.delete("/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    obj = crud.delete_especialidad(db, item_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    return {"detail": "Deleted"}
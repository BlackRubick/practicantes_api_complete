from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.universidad import UniversidadCreate, UniversidadOut
from app.crud import universidad as crud

router = APIRouter(prefix="/universidad", tags=["Universidad"])

@router.post("/", response_model=UniversidadOut)
def create_item(item: UniversidadCreate, db: Session = Depends(get_db)):
    return crud.create_universidad(db, item)

@router.get("/", response_model=list[UniversidadOut])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_universidads(db, skip=skip, limit=limit)

@router.get("/{item_id}", response_model=UniversidadOut)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_obj = crud.get_universidad_by_id(db, item_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Not found")
    return db_obj

@router.delete("/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    obj = crud.delete_universidad(db, item_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    return {"detail": "Deleted"}
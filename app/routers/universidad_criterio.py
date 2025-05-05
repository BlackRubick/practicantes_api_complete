from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.universidad_criterio import UniversidadCriterioCreate, UniversidadCriterioOut
from app.crud import universidad_criterio as crud

router = APIRouter(prefix="/universidad_criterio", tags=["UniversidadCriterio"])

@router.post("/", response_model=UniversidadCriterioOut)
def create_item(item: UniversidadCriterioCreate, db: Session = Depends(get_db)):
    return crud.create_universidad_criterio(db, item)

@router.get("/", response_model=list[UniversidadCriterioOut])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_universidad_criterios(db, skip=skip, limit=limit)

@router.get("/{item_id}", response_model=UniversidadCriterioOut)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_obj = crud.get_universidad_criterio_by_id(db, item_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Not found")
    return db_obj

@router.delete("/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    obj = crud.delete_universidad_criterio(db, item_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    return {"detail": "Deleted"}
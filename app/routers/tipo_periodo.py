from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.tipo_periodo import TipoPeriodoCreate, TipoPeriodoOut
from app.crud import tipo_periodo as crud

router = APIRouter(prefix="/tipo_periodo", tags=["TipoPeriodo"])

@router.post("/", response_model=TipoPeriodoOut)
def create_item(item: TipoPeriodoCreate, db: Session = Depends(get_db)):
    return crud.create_tipo_periodo(db, item)

@router.get("/", response_model=list[TipoPeriodoOut])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_tipo_periodos(db, skip=skip, limit=limit)

@router.get("/{item_id}", response_model=TipoPeriodoOut)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_obj = crud.get_tipo_periodo_by_id(db, item_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Not found")
    return db_obj

@router.delete("/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    obj = crud.delete_tipo_periodo(db, item_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    return {"detail": "Deleted"}
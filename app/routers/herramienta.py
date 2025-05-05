from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.herramienta import HerramientaCreate, HerramientaOut
from app.crud import herramienta as crud

router = APIRouter(prefix="/herramienta", tags=["Herramienta"])

@router.post("/", response_model=HerramientaOut)
def create_item(item: HerramientaCreate, db: Session = Depends(get_db)):
    return crud.create_herramienta(db, item)

@router.get("/", response_model=list[HerramientaOut])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_herramientas(db, skip=skip, limit=limit)

@router.get("/{item_id}", response_model=HerramientaOut)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_obj = crud.get_herramienta_by_id(db, item_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Not found")
    return db_obj

@router.delete("/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    obj = crud.delete_herramienta(db, item_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    return {"detail": "Deleted"}
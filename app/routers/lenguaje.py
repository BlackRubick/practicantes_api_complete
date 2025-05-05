from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.lenguaje import LenguajeCreate, LenguajeOut
from app.crud import lenguaje as crud

router = APIRouter(prefix="/lenguaje", tags=["Lenguaje"])

@router.post("/", response_model=LenguajeOut)
def create_item(item: LenguajeCreate, db: Session = Depends(get_db)):
    return crud.create_lenguaje(db, item)

@router.get("/", response_model=list[LenguajeOut])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_lenguajes(db, skip=skip, limit=limit)

@router.get("/{item_id}", response_model=LenguajeOut)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_obj = crud.get_lenguaje_by_id(db, item_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Not found")
    return db_obj

@router.delete("/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    obj = crud.delete_lenguaje(db, item_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    return {"detail": "Deleted"}
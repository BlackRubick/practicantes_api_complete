from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.practicante_lenguaje import PracticanteLenguajeCreate, PracticanteLenguajeOut
from app.crud import practicante_lenguaje as crud

router = APIRouter(prefix="/practicante_lenguaje", tags=["PracticanteLenguaje"])

@router.post("/", response_model=PracticanteLenguajeOut)
def create_item(item: PracticanteLenguajeCreate, db: Session = Depends(get_db)):
    return crud.create_practicante_lenguaje(db, item)

@router.get("/", response_model=list[PracticanteLenguajeOut])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_practicante_lenguajes(db, skip=skip, limit=limit)

@router.get("/{item_id}", response_model=PracticanteLenguajeOut)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_obj = crud.get_practicante_lenguaje_by_id(db, item_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Not found")
    return db_obj

@router.delete("/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    obj = crud.delete_practicante_lenguaje(db, item_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    return {"detail": "Deleted"}
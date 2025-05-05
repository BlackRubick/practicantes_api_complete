from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.practicante import PracticanteCreate, PracticanteOut
from app.crud import practicante as crud

router = APIRouter(prefix="/practicante", tags=["Practicante"])

@router.post("/", response_model=PracticanteOut)
def create_item(item: PracticanteCreate, db: Session = Depends(get_db)):
    return crud.create_practicante(db, item)

@router.get("/", response_model=list[PracticanteOut])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_practicantes(db, skip=skip, limit=limit)

@router.get("/{item_id}", response_model=PracticanteOut)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_obj = crud.get_practicante_by_id(db, item_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Not found")
    return db_obj

@router.delete("/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    obj = crud.delete_practicante(db, item_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    return {"detail": "Deleted"}
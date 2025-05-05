from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.aptitud import AptitudCreate, AptitudOut
from app.crud import aptitud as crud

router = APIRouter(prefix="/aptitud", tags=["Aptitud"])

@router.post("/", response_model=AptitudOut)
def create_item(item: AptitudCreate, db: Session = Depends(get_db)):
    return crud.create_aptitud(db, item)

@router.get("/", response_model=list[AptitudOut])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_aptituds(db, skip=skip, limit=limit)

@router.get("/{item_id}", response_model=AptitudOut)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_obj = crud.get_aptitud_by_id(db, item_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Not found")
    return db_obj

@router.delete("/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    obj = crud.delete_aptitud(db, item_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    return {"detail": "Deleted"}
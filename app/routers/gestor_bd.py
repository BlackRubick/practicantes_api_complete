from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.gestor_bd import GestorBdCreate, GestorBdOut
from app.crud import gestor_bd as crud

router = APIRouter(prefix="/gestor_bd", tags=["GestorBd"])

@router.post("/", response_model=GestorBdOut)
def create_item(item: GestorBdCreate, db: Session = Depends(get_db)):
    return crud.create_gestor_bd(db, item)

@router.get("/", response_model=list[GestorBdOut])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_gestor_bds(db, skip=skip, limit=limit)

@router.get("/{item_id}", response_model=GestorBdOut)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_obj = crud.get_gestor_bd_by_id(db, item_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Not found")
    return db_obj

@router.delete("/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    obj = crud.delete_gestor_bd(db, item_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    return {"detail": "Deleted"}
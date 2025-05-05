from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.actividad import ActividadCreate, ActividadOut
from app.crud import actividad as crud

router = APIRouter(prefix="/actividad", tags=["Actividad"])

@router.post("/", response_model=ActividadOut)
def create_item(item: ActividadCreate, db: Session = Depends(get_db)):
    return crud.create_actividad(db, item)

@router.get("/", response_model=list[ActividadOut])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_actividads(db, skip=skip, limit=limit)

@router.get("/{item_id}", response_model=ActividadOut)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_obj = crud.get_actividad_by_id(db, item_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Not found")
    return db_obj

@router.delete("/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    obj = crud.delete_actividad(db, item_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    return {"detail": "Deleted"}
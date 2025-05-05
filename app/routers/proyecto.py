from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.proyecto import ProyectoCreate, ProyectoOut
from app.crud import proyecto as crud

router = APIRouter(prefix="/proyecto", tags=["Proyecto"])

@router.post("/", response_model=ProyectoOut)
def create_item(item: ProyectoCreate, db: Session = Depends(get_db)):
    return crud.create_proyecto(db, item)

@router.get("/", response_model=list[ProyectoOut])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_proyectos(db, skip=skip, limit=limit)

@router.get("/{item_id}", response_model=ProyectoOut)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_obj = crud.get_proyecto_by_id(db, item_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Not found")
    return db_obj

@router.delete("/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    obj = crud.delete_proyecto(db, item_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    return {"detail": "Deleted"}
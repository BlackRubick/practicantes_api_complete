from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.administracion import AdministracionCreate, AdministracionOut
from app.crud import administracion as crud

router = APIRouter(prefix="/administracion", tags=["Administracion"])

@router.post("/", response_model=AdministracionOut)
def create_item(item: AdministracionCreate, db: Session = Depends(get_db)):
    return crud.create_administracion(db, item)

@router.get("/", response_model=list[AdministracionOut])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_administracions(db, skip=skip, limit=limit)

@router.get("/{item_id}", response_model=AdministracionOut)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_obj = crud.get_administracion_by_id(db, item_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Not found")
    return db_obj

@router.delete("/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    obj = crud.delete_administracion(db, item_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    return {"detail": "Deleted"}
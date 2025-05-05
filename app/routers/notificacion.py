from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.notificacion import NotificacionCreate, NotificacionOut
from app.crud import notificacion as crud

router = APIRouter(prefix="/notificacion", tags=["Notificacion"])

@router.post("/", response_model=NotificacionOut)
def create_item(item: NotificacionCreate, db: Session = Depends(get_db)):
    return crud.create_notificacion(db, item)

@router.get("/", response_model=list[NotificacionOut])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_notificacions(db, skip=skip, limit=limit)

@router.get("/{item_id}", response_model=NotificacionOut)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_obj = crud.get_notificacion_by_id(db, item_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Not found")
    return db_obj

@router.delete("/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    obj = crud.delete_notificacion(db, item_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    return {"detail": "Deleted"}
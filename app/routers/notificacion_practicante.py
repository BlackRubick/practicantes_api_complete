from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.notificacion_practicante import NotificacionPracticanteCreate, NotificacionPracticanteOut
from app.crud import notificacion_practicante as crud

router = APIRouter(prefix="/notificacion_practicante", tags=["NotificacionPracticante"])

@router.post("/", response_model=NotificacionPracticanteOut)
def create_item(item: NotificacionPracticanteCreate, db: Session = Depends(get_db)):
    return crud.create_notificacion_practicante(db, item)

@router.get("/", response_model=list[NotificacionPracticanteOut])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_notificacion_practicantes(db, skip=skip, limit=limit)

@router.get("/{item_id}", response_model=NotificacionPracticanteOut)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_obj = crud.get_notificacion_practicante_by_id(db, item_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Not found")
    return db_obj

@router.delete("/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    obj = crud.delete_notificacion_practicante(db, item_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    return {"detail": "Deleted"}
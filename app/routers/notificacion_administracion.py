from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.notificacion_administracion import NotificacionAdministracionCreate, NotificacionAdministracionOut
from app.crud import notificacion_administracion as crud

router = APIRouter(prefix="/notificacion_administracion", tags=["NotificacionAdministracion"])

@router.post("/", response_model=NotificacionAdministracionOut)
def create_item(item: NotificacionAdministracionCreate, db: Session = Depends(get_db)):
    return crud.create_notificacion_administracion(db, item)

@router.get("/", response_model=list[NotificacionAdministracionOut])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_notificacion_administracions(db, skip=skip, limit=limit)

@router.get("/{item_id}", response_model=NotificacionAdministracionOut)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_obj = crud.get_notificacion_administracion_by_id(db, item_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Not found")
    return db_obj

@router.delete("/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    obj = crud.delete_notificacion_administracion(db, item_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    return {"detail": "Deleted"}
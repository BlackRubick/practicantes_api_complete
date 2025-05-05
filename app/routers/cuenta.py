from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.cuenta import CuentaCreate, CuentaOut
from app.crud import cuenta as crud

router = APIRouter(prefix="/cuenta", tags=["Cuenta"])

@router.post("/", response_model=CuentaOut)
def create_item(item: CuentaCreate, db: Session = Depends(get_db)):
    return crud.create_cuenta(db, item)

@router.get("/", response_model=list[CuentaOut])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_cuentas(db, skip=skip, limit=limit)

@router.get("/{item_id}", response_model=CuentaOut)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_obj = crud.get_cuenta_by_id(db, item_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Not found")
    return db_obj

@router.delete("/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    obj = crud.delete_cuenta(db, item_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    return {"detail": "Deleted"}
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.documentacion import DocumentacionCreate, DocumentacionOut
from app.crud import documentacion as crud

router = APIRouter(prefix="/documentacion", tags=["Documentacion"])

@router.post("/", response_model=DocumentacionOut)
def create_item(item: DocumentacionCreate, db: Session = Depends(get_db)):
    return crud.create_documentacion(db, item)

@router.get("/", response_model=list[DocumentacionOut])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_documentacions(db, skip=skip, limit=limit)

@router.get("/{item_id}", response_model=DocumentacionOut)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_obj = crud.get_documentacion_by_id(db, item_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Not found")
    return db_obj

@router.delete("/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    obj = crud.delete_documentacion(db, item_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    return {"detail": "Deleted"}
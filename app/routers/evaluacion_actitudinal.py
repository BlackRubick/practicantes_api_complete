from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.evaluacion_actitudinal import EvaluacionActitudinalCreate, EvaluacionActitudinalOut
from app.crud import evaluacion_actitudinal as crud

router = APIRouter(prefix="/evaluacion_actitudinal", tags=["EvaluacionActitudinal"])

@router.post("/", response_model=EvaluacionActitudinalOut)
def create_item(item: EvaluacionActitudinalCreate, db: Session = Depends(get_db)):
    return crud.create_evaluacion_actitudinal(db, item)

@router.get("/", response_model=list[EvaluacionActitudinalOut])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_evaluacion_actitudinals(db, skip=skip, limit=limit)

@router.get("/{item_id}", response_model=EvaluacionActitudinalOut)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_obj = crud.get_evaluacion_actitudinal_by_id(db, item_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Not found")
    return db_obj

@router.delete("/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    obj = crud.delete_evaluacion_actitudinal(db, item_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    return {"detail": "Deleted"}
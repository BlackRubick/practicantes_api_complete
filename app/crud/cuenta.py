from sqlalchemy.orm import Session
from app.models.cuenta import Cuenta
from app.schemas.cuenta import CuentaCreate

def create_cuenta(db: Session, item: CuentaCreate):
    db_item = Cuenta(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_cuentas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Cuenta).offset(skip).limit(limit).all()

def get_cuenta_by_id(db: Session, id: int):
    return db.query(Cuenta).filter(Cuenta.id_cuenta == id).first()

def delete_cuenta(db: Session, id: int):
    obj = db.query(Cuenta).filter(Cuenta.id_cuenta == id).first()
    if obj:
        db.delete(obj)
        db.commit()
    return obj
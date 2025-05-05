from pydantic import BaseModel
import datetime

class CuentaBase(BaseModel):
    username: str
    password: str
    rol: str
    fk_practicante: int
    fk_administracion: int

class CuentaCreate(CuentaBase):
    pass

class CuentaOut(CuentaBase):
    id_cuenta: int

    class Config:
        orm_mode = True
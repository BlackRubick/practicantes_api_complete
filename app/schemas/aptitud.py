from pydantic import BaseModel
import datetime

class AptitudBase(BaseModel):
    nombre: str

class AptitudCreate(AptitudBase):
    pass

class AptitudOut(AptitudBase):
    id_aptitud: int

    class Config:
        orm_mode = True
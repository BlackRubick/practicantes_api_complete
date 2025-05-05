from pydantic import BaseModel
import datetime

class CurriculumAptitudBase(BaseModel):
    fk_curriculum: int
    fk_aptitud: int
    valor: bool

class CurriculumAptitudCreate(CurriculumAptitudBase):
    pass

class CurriculumAptitudOut(CurriculumAptitudBase):
    id: int

    class Config:
        orm_mode = True
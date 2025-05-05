from pydantic import BaseModel
import datetime

class CurriculumGestorBdBase(BaseModel):
    fk_curriculum: int
    fk_gestor: int

class CurriculumGestorBdCreate(CurriculumGestorBdBase):
    pass

class CurriculumGestorBdOut(CurriculumGestorBdBase):
    id: int

    class Config:
        orm_mode = True
from pydantic import BaseModel
import datetime

class CurriculumProyectoBase(BaseModel):
    fk_curriculum: int
    fk_proyecto: int

class CurriculumProyectoCreate(CurriculumProyectoBase):
    pass

class CurriculumProyectoOut(CurriculumProyectoBase):
    id: int

    class Config:
        orm_mode = True
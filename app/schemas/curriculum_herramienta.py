from pydantic import BaseModel
import datetime

class CurriculumHerramientaBase(BaseModel):
    fk_curriculum: int
    fk_herramienta: int

class CurriculumHerramientaCreate(CurriculumHerramientaBase):
    pass

class CurriculumHerramientaOut(CurriculumHerramientaBase):
    id: int

    class Config:
        orm_mode = True
from pydantic import BaseModel
import datetime

class EvaluacionBase(BaseModel):
    fk_curriculum: int
    fk_proyecto: int
    fecha_evaluacion: datetime.date
    fk_universidad: int

class EvaluacionCreate(EvaluacionBase):
    pass

class EvaluacionOut(EvaluacionBase):
    id_evaluacion: int

    class Config:
        orm_mode = True
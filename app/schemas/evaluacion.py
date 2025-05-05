from pydantic import BaseModel
import datetime
from typing import Optional

class EvaluacionBase(BaseModel):
    fk_curriculum: int
    fk_proyecto: int
    fecha_evaluacion: datetime.date
    fk_universidad: int
    fk_administracion: Optional[int] = None
    es_evaluacion_activa: Optional[bool] = True

class EvaluacionCreate(EvaluacionBase):
    pass

class EvaluacionOut(EvaluacionBase):
    id_evaluacion: int

    class Config:
        orm_mode = True
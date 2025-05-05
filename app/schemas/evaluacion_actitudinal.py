from pydantic import BaseModel
import datetime

class EvaluacionActitudinalBase(BaseModel):
    fk_evaluacion: int
    fk_criterio: int
    puntuacion: int
    comentarios: str

class EvaluacionActitudinalCreate(EvaluacionActitudinalBase):
    pass

class EvaluacionActitudinalOut(EvaluacionActitudinalBase):
    id_eval_actitudinal: int

    class Config:
        orm_mode = True
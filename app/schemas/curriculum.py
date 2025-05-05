from pydantic import BaseModel
import datetime

class CurriculumBase(BaseModel):
    fk_practicante: int
    fecha_registro: datetime.date
    periodo_practicas: str
    fk_universidad: int
    fk_tipo_periodo: int
    fk_especialidad: int
    grado: int
    github: str
    nivel_ingles: str
    fecha_inicio: datetime.date
    fecha_termino: datetime.date
    numero_semanas: int

class CurriculumCreate(CurriculumBase):
    pass

class CurriculumOut(CurriculumBase):
    id_curriculum: int

    class Config:
        orm_mode = True
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from app.database import get_db
from app.models.practicante import Practicante
from app.models.proyecto import Proyecto
from app.models.curriculum import Curriculum
from app.models.evaluacion import Evaluacion
from app.models.administracion import Administracion
from sqlalchemy import and_, or_
from pydantic import BaseModel
import datetime

router = APIRouter(prefix="/admin", tags=["Admin"])


class PracticanteAsignadoResponse(BaseModel):
    id: int
    practicante_id: int
    practicante_nombre: str
    proyecto_id: Optional[int] = None
    proyecto_nombre: Optional[str] = None
    fecha_solicitud: Optional[datetime.date] = None
    estado: bool
    responsable_id: Optional[int] = None
    responsable_nombre: Optional[str] = None

    class Config:
        orm_mode = True


@router.get("/practicantes-asignados", response_model=List[PracticanteAsignadoResponse])
def get_practicantes_asignados(
        skip: int = 0,
        limit: int = 100,
        nombre: Optional[str] = None,
        id_practicante: Optional[int] = None,
        db: Session = Depends(get_db)
):
    query = db.query(
        Practicante.id_practicante.label("practicante_id"),
        Practicante.nombre_completo.label("practicante_nombre"),
        Practicante.estado_asignacion.label("estado"),
        Proyecto.id_proyecto.label("proyecto_id"),
        Proyecto.nombre_proyecto.label("proyecto_nombre"),
        Proyecto.fecha_asignacion.label("fecha_solicitud"),
        Administracion.id_administracion.label("responsable_id"),
        Administracion.nombre.label("responsable_nombre")
    ).join(
        Curriculum, Curriculum.fk_practicante == Practicante.id_practicante, isouter=True
    ).join(
        Evaluacion, Evaluacion.fk_curriculum == Curriculum.id_curriculum, isouter=True
    ).join(
        Proyecto, Proyecto.id_proyecto == Evaluacion.fk_proyecto, isouter=True
    ).join(
        Administracion, and_(
            Administracion.id_administracion == Evaluacion.fk_administracion,
            Evaluacion.es_evaluacion_activa == True
        ), isouter=True
    )

    if nombre:
        query = query.filter(Practicante.nombre_completo.ilike(f"%{nombre}%"))
    if id_practicante:
        query = query.filter(Practicante.id_practicante == id_practicante)

    results = query.offset(skip).limit(limit).all()

    response_items = []
    for i, result in enumerate(results):
        item_dict = {
            "id": i,  # Asignar un ID secuencial para cada resultado
            "practicante_id": result.practicante_id,
            "practicante_nombre": result.practicante_nombre,
            "proyecto_id": result.proyecto_id,
            "proyecto_nombre": result.proyecto_nombre,
            "fecha_solicitud": result.fecha_solicitud,
            "estado": result.estado,
            "responsable_id": result.responsable_id,
            "responsable_nombre": result.responsable_nombre
        }
        response_items.append(PracticanteAsignadoResponse(**item_dict))

    return response_items


@router.get("/buscar-practicante", response_model=List[PracticanteAsignadoResponse])
def buscar_practicante(
        termino: str,
        db: Session = Depends(get_db)
):
    # Verificar si el término de búsqueda es un número (posible ID)
    try:
        id_practicante = int(termino)
        id_search = True
    except (ValueError, TypeError):
        id_search = False

    query = db.query(
        Practicante.id_practicante.label("practicante_id"),
        Practicante.nombre_completo.label("practicante_nombre"),
        Practicante.estado_asignacion.label("estado"),
        Proyecto.id_proyecto.label("proyecto_id"),
        Proyecto.nombre_proyecto.label("proyecto_nombre"),
        Proyecto.fecha_asignacion.label("fecha_solicitud"),
        Administracion.id_administracion.label("responsable_id"),
        Administracion.nombre.label("responsable_nombre")
    ).join(
        Curriculum, Curriculum.fk_practicante == Practicante.id_practicante, isouter=True
    ).join(
        Evaluacion, Evaluacion.fk_curriculum == Curriculum.id_curriculum, isouter=True
    ).join(
        Proyecto, Proyecto.id_proyecto == Evaluacion.fk_proyecto, isouter=True
    ).join(
        Administracion, and_(
            Administracion.id_administracion == Evaluacion.fk_administracion,
            Evaluacion.es_evaluacion_activa == True
        ), isouter=True
    )

    # Filtrar por ID o por nombre
    if id_search:
        query = query.filter(Practicante.id_practicante == id_practicante)
    else:
        query = query.filter(Practicante.nombre_completo.ilike(f"%{termino}%"))

    results = query.all()

    response_items = []
    for i, result in enumerate(results):
        item_dict = {
            "id": i,
            "practicante_id": result.practicante_id,
            "practicante_nombre": result.practicante_nombre,
            "proyecto_id": result.proyecto_id,
            "proyecto_nombre": result.proyecto_nombre,
            "fecha_solicitud": result.fecha_solicitud,
            "estado": result.estado,
            "responsable_id": result.responsable_id,
            "responsable_nombre": result.responsable_nombre
        }
        response_items.append(PracticanteAsignadoResponse(**item_dict))

    return response_items
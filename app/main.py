from fastapi import FastAPI
from app.database import Base, engine
from app.routers import (
    practicante, cuenta, administracion, universidad, tipo_periodo,
    especialidad, curriculum, aptitud, curriculum_aptitud,
    lenguaje, practicante_lenguaje, herramienta, curriculum_herramienta,
    gestor_bd, curriculum_gestor_bd, proyecto, curriculum_proyecto,
    actividad, documentacion, notificacion,
    notificacion_practicante, notificacion_administracion,
    evaluacion, criterio_actitudinal, universidad_criterio,
    evaluacion_actitudinal, admin_vista
)


# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Practicantes")

for r in [
    practicante.router, cuenta.router, administracion.router,
    universidad.router, tipo_periodo.router, especialidad.router,
    curriculum.router, aptitud.router, curriculum_aptitud.router,
    lenguaje.router, practicante_lenguaje.router, herramienta.router,
    curriculum_herramienta.router, gestor_bd.router,
    curriculum_gestor_bd.router, proyecto.router,
    curriculum_proyecto.router, actividad.router,
    documentacion.router, notificacion.router,
    notificacion_practicante.router,
    notificacion_administracion.router, evaluacion.router,
    criterio_actitudinal.router, universidad_criterio.router,
    evaluacion_actitudinal.router, admin_vista.router  # Agregamos el nuevo router
]:
    app.include_router(r)
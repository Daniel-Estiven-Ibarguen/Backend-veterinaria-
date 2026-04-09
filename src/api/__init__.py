"""
Routers API para entidades del sistema.

Contiene los endpoints FastAPI con respuestas mockeadas
para usuario, animal, cita y consulta.
"""

from src.api.usuario import router as usuario_router
from src.api.animal import router as animal_router
from src.api.cita import router as cita_router
from src.api.consulta import router as consulta_router

__all__ = [
    "usuario_router",
    "animal_router",
    "cita_router",
    "consulta_router",
]

"""
Esquemas base reutilizables para respuestas de API.

Contiene clases base que proporcionan campos comunes de auditoría
y estructura de respuesta para listados.
"""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class AuditFields(BaseModel):
    """Campos de auditoría comunes para modelos de respuesta.

    Incluye identificadores de usuario que creó/editó el registro
    y timestamps de creación y edición.

    Args:
        id_usuario_creacion: ID del usuario que creó el registro.
        id_usuario_edita: ID del usuario que editó (opcional).
        fecha_creacion: Fecha y hora de creación.
        fecha_edicion: Fecha y hora de última edición (opcional).
    """

    id_usuario_creacion: int
    id_usuario_edita: Optional[int] = None
    fecha_creacion: datetime
    fecha_edicion: Optional[datetime] = None


class RequestBase(BaseModel):
    """Clase base vacía para esquemas de request.

    Puede ser extendida para agregar validaciones comunes
    a todos los modelos de petición.
    """

    pass


class ResponseBase(AuditFields):
    """Clase base para esquemas de respuesta.

    Hereda de AuditFields para incluir campos de auditoría
    en todas las respuestas.
    """

    pass


class ListaResponse(BaseModel):
    """Modelo de respuesta para endpoints de listado.

    Envuelve una lista de items con el total de elementos.

    Args:
        total: Cantidad total de elementos en la lista.
        items: Lista de elementos del tipo ResponseBase.
    """

    total: int
    items: list["ResponseBase"]


from src.schemas.usuario import *
from src.schemas.animal import *
from src.schemas.cita import *
from src.schemas.consulta import *

ListaResponse.model_rebuild()

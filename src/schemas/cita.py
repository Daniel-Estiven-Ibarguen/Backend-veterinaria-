"""
Esquemas Pydantic para la entidad Cita.

Contiene los modelos de request y response para las operaciones
CRUD de citas: crear, listar, obtener por id, actualizar y eliminar.
"""

from datetime import date, time, datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class CitaRequest(BaseModel):
    """Modelo de petición para crear una cita.

    Args:
        fecha: Fecha de la cita.
        hora: Hora de la cita.
        tipo: Tipo de cita (default: 'revision').
        estado: Estado de la cita (default: 'pendiente').
        id_animal: ID del animal asociado.
        id_veterinario: ID del veterinario asignado.
        id_usuario_creacion: ID del usuario que crea el registro.
    """

    fecha: date
    hora: time
    tipo: str = "revision"
    estado: str = "pendiente"
    id_animal: int
    id_veterinario: int
    id_usuario_creacion: int


class CitaUpdateRequest(BaseModel):
    """Modelo de petición para actualizar una cita.

    Todos los campos son opcionales para permitir actualizaciones parciales.

    Args:
        fecha: Nueva fecha (opcional).
        hora: Nueva hora (opcional).
        tipo: Nuevo tipo (opcional).
        estado: Nuevo estado (opcional).
        id_usuario_edita: ID del usuario que edita (opcional).
    """

    fecha: Optional[date] = None
    hora: Optional[time] = None
    tipo: Optional[str] = None
    estado: Optional[str] = None
    id_usuario_edita: Optional[int] = None


class CitaResponse(BaseModel):
    """Modelo de respuesta para obtener una cita.

    Incluye todos los campos de la cita incluyendo los de auditoría.

    Args:
        id: Identificador único de la cita.
        fecha: Fecha de la cita.
        hora: Hora de la cita.
        tipo: Tipo de cita.
        estado: Estado de la cita.
        id_animal: ID del animal asociado.
        id_veterinario: ID del veterinario asignado.
        id_usuario_creacion: ID del usuario que creó el registro.
        id_usuario_edita: ID del usuario que editó (opcional).
        fecha_creacion: Fecha y hora de creación.
        fecha_edicion: Fecha y hora de última edición (opcional).
    """

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": 1,
                "fecha": "2026-04-15",
                "hora": "10:30:00",
                "tipo": "revision",
                "estado": "pendiente",
                "id_animal": 1,
                "id_veterinario": 1,
                "id_usuario_creacion": 1,
                "id_usuario_edita": None,
                "fecha_creacion": "2026-01-15T10:30:00",
                "fecha_edicion": None
            }
        }
    )

    id: int
    fecha: date
    hora: time
    tipo: str
    estado: str
    id_animal: int
    id_veterinario: int
    id_usuario_creacion: int
    id_usuario_edita: Optional[int] = None
    fecha_creacion: datetime
    fecha_edicion: Optional[datetime] = None


class CitaDeleteResponse(BaseModel):
    """Modelo de respuesta tras eliminar una cita.

    Args:
        id: Identificador de la cita eliminada.
        eliminado: Indica que la eliminación fue exitosa.
    """

    id: int
    eliminado: bool = True


class CitaListResponse(BaseModel):
    """Modelo de respuesta para listar citas.

    Args:
        total: Número total de citas.
        items: Lista de citas.
    """

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "total": 2,
                "items": [
                    {
                        "id": 1,
                        "fecha": "2026-04-15",
                        "hora": "10:30:00",
                        "tipo": "revision",
                        "estado": "pendiente",
                        "id_animal": 1,
                        "id_veterinario": 1,
                        "id_usuario_creacion": 1,
                        "id_usuario_edita": None,
                        "fecha_creacion": "2026-01-15T10:30:00",
                        "fecha_edicion": None
                    },
                    {
                        "id": 2,
                        "fecha": "2026-04-20",
                        "hora": "14:00:00",
                        "tipo": "urgencia",
                        "estado": "confirmada",
                        "id_animal": 2,
                        "id_veterinario": 1,
                        "id_usuario_creacion": 1,
                        "id_usuario_edita": None,
                        "fecha_creacion": "2026-01-16T11:00:00",
                        "fecha_edicion": None
                    }
                ]
            }
        }
    )

    total: int
    items: list[CitaResponse]

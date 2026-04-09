"""
Esquemas Pydantic para la entidad Consulta.

Contiene los modelos de request y response para las operaciones
CRUD de consultas: crear, listar, obtener por id, actualizar y eliminar.
"""

from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class ConsultaRequest(BaseModel):
    """Modelo de petición para crear una consulta.

    Args:
        fecha: Fecha de la consulta.
        diagnostico: Diagnóstico realizado.
        tratamiento: Tratamiento prescrito.
        observaciones: Observaciones adicionales (opcional).
        tipo_consulta: Tipo de consulta ('revision', 'urgencia').
        motivo_revision: Motivo de revisión (solo para tipo 'revision').
        proxima_cita: Fecha próxima cita (solo para tipo 'revision').
        nivel_urgencia: Nivel 1-5 (solo para tipo 'urgencia').
        sintomas: Síntomas presentados (solo para tipo 'urgencia').
        id_cita: ID de la cita asociada.
        id_animal: ID del animal consultado.
        id_veterinario: ID del veterinario que atendió.
        id_usuario_creacion: ID del usuario que crea el registro.
    """

    fecha: date
    diagnostico: str
    tratamiento: str
    observaciones: Optional[str] = None
    tipo_consulta: str
    motivo_revision: Optional[str] = None
    proxima_cita: Optional[date] = None
    nivel_urgencia: Optional[int] = None
    sintomas: Optional[str] = None
    id_cita: int
    id_animal: int
    id_veterinario: int
    id_usuario_creacion: int


class ConsultaUpdateRequest(BaseModel):
    """Modelo de petición para actualizar una consulta.

    Todos los campos son opcionales para permitir actualizaciones parciales.

    Args:
        fecha: Nueva fecha (opcional).
        diagnostico: Nuevo diagnóstico (opcional).
        tratamiento: Nuevo tratamiento (opcional).
        observaciones: Nuevas observaciones (opcional).
        tipo_consulta: Nuevo tipo (opcional).
        motivo_revision: Nuevo motivo de revisión (opcional).
        proxima_cita: Nueva fecha de próxima cita (opcional).
        nivel_urgencia: Nuevo nivel de urgencia (opcional).
        sintomas: Nuevos síntomas (opcional).
        id_usuario_edita: ID del usuario que edita (opcional).
    """

    fecha: Optional[date] = None
    diagnostico: Optional[str] = None
    tratamiento: Optional[str] = None
    observaciones: Optional[str] = None
    tipo_consulta: Optional[str] = None
    motivo_revision: Optional[str] = None
    proxima_cita: Optional[date] = None
    nivel_urgencia: Optional[int] = None
    sintomas: Optional[str] = None
    id_usuario_edita: Optional[int] = None


class ConsultaResponse(BaseModel):
    """Modelo de respuesta para obtener una consulta.

    Incluye todos los campos de la consulta incluyendo los de auditoría.

    Args:
        id: Identificador único de la consulta.
        fecha: Fecha de la consulta.
        diagnostico: Diagnóstico realizado.
        tratamiento: Tratamiento prescrito.
        observaciones: Observaciones adicionales (opcional).
        tipo_consulta: Tipo de consulta.
        motivo_revision: Motivo de revisión (opcional).
        proxima_cita: Fecha próxima cita (opcional).
        nivel_urgencia: Nivel de urgencia (opcional).
        sintomas: Síntomas presentados (opcional).
        id_cita: ID de la cita asociada.
        id_animal: ID del animal consultado.
        id_veterinario: ID del veterinario que atendió.
        id_usuario_creacion: ID del usuario que creó el registro.
        id_usuario_edita: ID del usuario que editó (opcional).
        fecha_creacion: Fecha y hora de creación.
        fecha_edicion: Fecha y hora de última edición (opcional).
    """

    model_config = ConfigDict(from_attributes=True)

    id: int
    fecha: date
    diagnostico: str
    tratamiento: str
    observaciones: Optional[str] = None
    tipo_consulta: str
    motivo_revision: Optional[str] = None
    proxima_cita: Optional[date] = None
    nivel_urgencia: Optional[int] = None
    sintomas: Optional[str] = None
    id_cita: int
    id_animal: int
    id_veterinario: int
    id_usuario_creacion: int
    id_usuario_edita: Optional[int] = None
    fecha_creacion: datetime
    fecha_edicion: Optional[datetime] = None


class ConsultaDeleteResponse(BaseModel):
    """Modelo de respuesta tras eliminar una consulta.

    Args:
        id: Identificador de la consulta eliminada.
        eliminado: Indica que la eliminación fue exitosa.
    """

    id: int
    eliminado: bool = True

"""
Endpoints API para la entidad Consulta.

Proporciona operaciones CRUD mockeadas:
- GET /consultas - Lista todas las consultas
- GET /consultas/{id} - Obtiene una consulta por ID
- POST /consultas - Crea una nueva consulta
- PUT /consultas/{id} - Actualiza una consulta
- DELETE /consultas/{id} - Elimina una consulta
"""

from datetime import date, datetime
from typing import Optional

from fastapi import APIRouter, HTTPException, Path

from src.schemas.consulta import (
    ConsultaRequest,
    ConsultaUpdateRequest,
    ConsultaResponse,
    ConsultaDeleteResponse,
)

router = APIRouter(prefix="/consultas", tags=["consultas"])

MOCK_CONSULTAS = [
    {
        "id": 1,
        "fecha": date(2024, 3, 15),
        "diagnostico": "Control de salud general",
        "tratamiento": "Vacuna anual aplicada",
        "observaciones": "Animal en buen estado",
        "tipo_consulta": "revision",
        "motivo_revision": "Chequeo anual",
        "proxima_cita": date(2025, 3, 15),
        "nivel_urgencia": None,
        "sintomas": None,
        "id_cita": 1,
        "id_animal": 1,
        "id_veterinario": 1,
        "id_usuario_creacion": 1,
        "id_usuario_edita": None,
        "fecha_creacion": datetime(2024, 3, 15, 10, 30, 0),
        "fecha_edicion": None,
    },
    {
        "id": 2,
        "fecha": date(2024, 3, 16),
        "diagnostico": "Intoxicación alimentaria",
        "tratamiento": "Hidratación y dieta blanda por 3 días",
        "observaciones": "Seguimiento en 48 horas",
        "tipo_consulta": "urgencia",
        "motivo_revision": None,
        "proxima_cita": None,
        "nivel_urgencia": 3,
        "sintomas": "Vómitos, letargo",
        "id_cita": 2,
        "id_animal": 2,
        "id_veterinario": 1,
        "id_usuario_creacion": 1,
        "id_usuario_edita": None,
        "fecha_creacion": datetime(2024, 3, 16, 12, 0, 0),
        "fecha_edicion": None,
    },
]


@router.get("", response_model=dict)
async def listar_consultas():
    """Lista todas las consultas registradas.

    Returns:
        Diccionario con total y lista de consultas.
    """
    return {
        "total": len(MOCK_CONSULTAS),
        "items": MOCK_CONSULTAS,
    }


@router.get("/{id}", response_model=ConsultaResponse)
async def obtener_consulta(id: int = Path(..., description="ID de la consulta")):
    """Obtiene una consulta por su ID.

    Args:
        id: Identificador único de la consulta.

    Returns:
        Datos de la consulta encontrada.

    Raises:
        HTTPException: Si no se encuentra la consulta.
    """
    for consulta in MOCK_CONSULTAS:
        if consulta["id"] == id:
            return consulta
    raise HTTPException(status_code=404, detail="Consulta no encontrada")


@router.post("", response_model=ConsultaResponse, status_code=201)
async def crear_consulta(request: ConsultaRequest):
    """Crea una nueva consulta.

    Args:
        request: Datos de la consulta a crear.

    Returns:
        Consulta creada con ID asignado.
    """
    nuevo_id = max(c["id"] for c in MOCK_CONSULTAS) + 1
    return {
        "id": nuevo_id,
        "fecha": request.fecha,
        "diagnostico": request.diagnostico,
        "tratamiento": request.tratamiento,
        "observaciones": request.observaciones,
        "tipo_consulta": request.tipo_consulta,
        "motivo_revision": request.motivo_revision,
        "proxima_cita": request.proxima_cita,
        "nivel_urgencia": request.nivel_urgencia,
        "sintomas": request.sintomas,
        "id_cita": request.id_cita,
        "id_animal": request.id_animal,
        "id_veterinario": request.id_veterinario,
        "id_usuario_creacion": request.id_usuario_creacion,
        "id_usuario_edita": None,
        "fecha_creacion": datetime.now(),
        "fecha_edicion": None,
    }


@router.put("/{id}", response_model=ConsultaResponse)
async def actualizar_consulta(
    id: int,
    request: ConsultaUpdateRequest,
):
    """Actualiza una consulta existente.

    Args:
        id: ID de la consulta a actualizar.
        request: Campos a actualizar (todos opcionales).

    Returns:
        Consulta con los campos actualizados.

    Raises:
        HTTPException: Si no se encuentra la consulta.
    """
    for consulta in MOCK_CONSULTAS:
        if consulta["id"] == id:
            update_data = request.model_dump(exclude_unset=True)
            consulta.update(update_data)
            consulta["fecha_edicion"] = datetime.now()
            return consulta
    raise HTTPException(status_code=404, detail="Consulta no encontrada")


@router.delete("/{id}", response_model=ConsultaDeleteResponse)
async def eliminar_consulta(id: int):
    """Elimina una consulta por su ID.

    Args:
        id: ID de la consulta a eliminar.

    Returns:
        Confirmación de eliminación.

    Raises:
        HTTPException: Si no se encuentra la consulta.
    """
    for consulta in MOCK_CONSULTAS:
        if consulta["id"] == id:
            return {"id": id, "eliminado": True}
    raise HTTPException(status_code=404, detail="Consulta no encontrada")

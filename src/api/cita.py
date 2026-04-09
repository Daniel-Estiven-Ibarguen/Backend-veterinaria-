"""
Endpoints API para la entidad Cita.

Proporciona operaciones CRUD mockeadas:
- GET /citas - Lista todas las citas
- GET /citas/{id} - Obtiene una cita por ID
- POST /citas - Crea una nueva cita
- PUT /citas/{id} - Actualiza una cita
- DELETE /citas/{id} - Elimina una cita
"""

from datetime import date, time, datetime
from typing import Optional

from fastapi import APIRouter, HTTPException, Path

from src.schemas.cita import (
    CitaRequest,
    CitaUpdateRequest,
    CitaResponse,
    CitaDeleteResponse,
)

router = APIRouter(prefix="/citas", tags=["citas"])

MOCK_CITAS = [
    {
        "id": 1,
        "fecha": date(2024, 3, 15),
        "hora": time(10, 0),
        "tipo": "revision",
        "estado": "confirmada",
        "id_animal": 1,
        "id_veterinario": 1,
        "id_usuario_creacion": 1,
        "id_usuario_edita": None,
        "fecha_creacion": datetime(2024, 3, 1, 9, 0, 0),
        "fecha_edicion": None,
    },
    {
        "id": 2,
        "fecha": date(2024, 3, 16),
        "hora": time(11, 30),
        "tipo": "urgencias",
        "estado": "pendiente",
        "id_animal": 2,
        "id_veterinario": 1,
        "id_usuario_creacion": 1,
        "id_usuario_edita": None,
        "fecha_creacion": datetime(2024, 3, 2, 14, 30, 0),
        "fecha_edicion": None,
    },
    {
        "id": 3,
        "fecha": date(2024, 3, 17),
        "hora": time(16, 0),
        "tipo": "revision",
        "estado": "pendiente",
        "id_animal": 3,
        "id_veterinario": 2,
        "id_usuario_creacion": 2,
        "id_usuario_edita": None,
        "fecha_creacion": datetime(2024, 3, 3, 8, 15, 0),
        "fecha_edicion": None,
    },
]


@router.get("", response_model=dict)
async def listar_citas():
    """Lista todas las citas registradas.

    Returns:
        Diccionario con total y lista de citas.
    """
    return {
        "total": len(MOCK_CITAS),
        "items": MOCK_CITAS,
    }


@router.get("/{id}", response_model=CitaResponse)
async def obtener_cita(id: int = Path(..., description="ID de la cita")):
    """Obtiene una cita por su ID.

    Args:
        id: Identificador único de la cita.

    Returns:
        Datos de la cita encontrada.

    Raises:
        HTTPException: Si no se encuentra la cita.
    """
    for cita in MOCK_CITAS:
        if cita["id"] == id:
            return cita
    raise HTTPException(status_code=404, detail="Cita no encontrada")


@router.post("", response_model=CitaResponse, status_code=201)
async def crear_cita(request: CitaRequest):
    """Crea una nueva cita.

    Args:
        request: Datos de la cita a crear.

    Returns:
        Cita creada con ID asignado.
    """
    nuevo_id = max(c["id"] for c in MOCK_CITAS) + 1
    return {
        "id": nuevo_id,
        "fecha": request.fecha,
        "hora": request.hora,
        "tipo": request.tipo,
        "estado": request.estado,
        "id_animal": request.id_animal,
        "id_veterinario": request.id_veterinario,
        "id_usuario_creacion": request.id_usuario_creacion,
        "id_usuario_edita": None,
        "fecha_creacion": datetime.now(),
        "fecha_edicion": None,
    }


@router.put("/{id}", response_model=CitaResponse)
async def actualizar_cita(
    id: int,
    request: CitaUpdateRequest,
):
    """Actualiza una cita existente.

    Args:
        id: ID de la cita a actualizar.
        request: Campos a actualizar (todos opcionales).

    Returns:
        Cita con los campos actualizados.

    Raises:
        HTTPException: Si no se encuentra la cita.
    """
    for cita in MOCK_CITAS:
        if cita["id"] == id:
            update_data = request.model_dump(exclude_unset=True)
            cita.update(update_data)
            cita["fecha_edicion"] = datetime.now()
            return cita
    raise HTTPException(status_code=404, detail="Cita no encontrada")


@router.delete("/{id}", response_model=CitaDeleteResponse)
async def eliminar_cita(id: int):
    """Elimina una cita por su ID.

    Args:
        id: ID de la cita a eliminar.

    Returns:
        Confirmación de eliminación.

    Raises:
        HTTPException: Si no se encuentra la cita.
    """
    for cita in MOCK_CITAS:
        if cita["id"] == id:
            return {"id": id, "eliminado": True}
    raise HTTPException(status_code=404, detail="Cita no encontrada")

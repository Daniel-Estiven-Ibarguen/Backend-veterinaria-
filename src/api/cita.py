"""
Endpoints API para la entidad Cita.

Proporciona operaciones CRUD conectadas a la base de datos:
- GET /citas - Lista todas las citas
- GET /citas/{id} - Obtiene una cita por ID
- POST /citas - Crea una nueva cita
- PUT /citas/{id} - Actualiza una cita
- DELETE /citas/{id} - Elimina una cita
"""

from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.orm import Session

from src.database import get_db
from src.crud.cita_crud import CitaCrud
from src.schemas.cita import (
    CitaRequest,
    CitaUpdateRequest,
    CitaResponse,
    CitaDeleteResponse,
)

router = APIRouter(prefix="/citas", tags=["citas"])


@router.get("", response_model=dict)
async def listar_citas(db: Session = Depends(get_db)):
    """Lista todas las citas registradas.

    Args:
        db: Sesión de base de datos.

    Returns:
        Diccionario con total y lista de citas.
    """
    crud = CitaCrud(db)
    citas = crud.listar_citas()
    return {
        "total": len(citas),
        "items": [CitaResponse.model_validate(c) for c in citas],
    }


@router.get("/{id}", response_model=CitaResponse)
async def obtener_cita(
    id: int = Path(..., description="ID de la cita"),
    db: Session = Depends(get_db),
):
    """Obtiene una cita por su ID.

    Args:
        id: Identificador único de la cita.
        db: Sesión de base de datos.

    Returns:
        Datos de la cita encontrada.

    Raises:
        HTTPException: Si no se encuentra la cita.
    """
    crud = CitaCrud(db)
    cita = crud.buscar_cita(id)
    if not cita:
        raise HTTPException(status_code=404, detail="Cita no encontrada")
    return cita


@router.post("", response_model=CitaResponse, status_code=201)
async def crear_cita(request: CitaRequest, db: Session = Depends(get_db)):
    """Crea una nueva cita.

    Args:
        request: Datos de la cita a crear.
        db: Sesión de base de datos.

    Returns:
        Cita creada con ID asignado.
    """
    crud = CitaCrud(db)
    cita = crud.crear_cita(
        fecha=request.fecha,
        hora=request.hora,
        id_animal=request.id_animal,
        id_veterinario=request.id_veterinario,
        tipo=request.tipo,
        estado=request.estado,
        id_usuario_creacion=request.id_usuario_creacion,
    )
    return cita


@router.put("/{id}", response_model=CitaResponse)
async def actualizar_cita(
    id: int,
    request: CitaUpdateRequest,
    db: Session = Depends(get_db),
):
    """Actualiza una cita existente.

    Args:
        id: ID de la cita a actualizar.
        request: Campos a actualizar (todos opcionales).
        db: Sesión de base de datos.

    Returns:
        Cita con los campos actualizados.

    Raises:
        HTTPException: Si no se encuentra la cita.
    """
    crud = CitaCrud(db)
    update_data = request.model_dump(exclude_unset=True)
    cita = crud.actualizar_cita(id, **update_data)
    if not cita:
        raise HTTPException(status_code=404, detail="Cita no encontrada")
    return cita


@router.delete("/{id}", response_model=CitaDeleteResponse)
async def eliminar_cita(id: int, db: Session = Depends(get_db)):
    """Elimina una cita por su ID.

    Args:
        id: ID de la cita a eliminar.
        db: Sesión de base de datos.

    Returns:
        Confirmación de eliminación.

    Raises:
        HTTPException: Si no se encuentra la cita.
    """
    crud = CitaCrud(db)
    eliminado = crud.eliminar_cita(id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Cita no encontrada")
    return {"id": id, "eliminado": True}

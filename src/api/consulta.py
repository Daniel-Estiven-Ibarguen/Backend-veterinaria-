"""
Endpoints API para la entidad Consulta.

Proporciona operaciones CRUD conectadas a la base de datos:
- GET /consultas - Lista todas las consultas
- GET /consultas/{id} - Obtiene una consulta por ID
- POST /consultas - Crea una nueva consulta
- PUT /consultas/{id} - Actualiza una consulta
- DELETE /consultas/{id} - Elimina una consulta
"""

from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from src.database import get_db
from src.crud.consulta_crud import ConsultaCrud
from src.schemas.consulta import (
    ConsultaRequest,
    ConsultaUpdateRequest,
    ConsultaResponse,
    ConsultaDeleteResponse,
)

router = APIRouter(prefix="/consultas", tags=["consultas"])


@router.get("", response_model=dict)
async def listar_consultas(db: Session = Depends(get_db)):
    """Lista todas las consultas registradas.

    Args:
        db: Sesión de base de datos.

    Returns:
        Diccionario con total y lista de consultas.
    """
    crud = ConsultaCrud(db)
    consultas = crud.listar_consultas()
    return {
        "total": len(consultas),
        "items": [ConsultaResponse.model_validate(c) for c in consultas],
    }


@router.get("/{id}", response_model=ConsultaResponse)
async def obtener_consulta(
    id: int = Path(..., description="ID de la consulta"),
    db: Session = Depends(get_db),
):
    """Obtiene una consulta por su ID.

    Args:
        id: Identificador único de la consulta.
        db: Sesión de base de datos.

    Returns:
        Datos de la consulta encontrada.

    Raises:
        HTTPException: Si no se encuentra la consulta.
    """
    crud = ConsultaCrud(db)
    consulta = crud.buscar_consulta(id)
    if not consulta:
        raise HTTPException(status_code=404, detail="Consulta no encontrada")
    return consulta


@router.post("", response_model=ConsultaResponse, status_code=201)
async def crear_consulta(request: ConsultaRequest, db: Session = Depends(get_db)):
    """Crea una nueva consulta.

    Args:
        request: Datos de la consulta a crear.
        db: Sesión de base de datos.

    Returns:
        Consulta creada con ID asignado.

    Raises:
        HTTPException: Si la cita, animal, veterinario o usuario no existen.
    """
    crud = ConsultaCrud(db)
    try:
        consulta = crud.crear_consulta(
            fecha=request.fecha,
            diagnostico=request.diagnostico,
            tratamiento=request.tratamiento,
            observaciones=request.observaciones,
            tipo_consulta=request.tipo_consulta,
            motivo_revision=request.motivo_revision,
            proxima_cita=request.proxima_cita,
            nivel_urgencia=request.nivel_urgencia,
            sintomas=request.sintomas,
            id_cita=request.id_cita,
            id_animal=request.id_animal,
            id_veterinario=request.id_veterinario,
            id_usuario_creacion=request.id_usuario_creacion,
        )
        return consulta
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=404,
            detail="La cita, animal, veterinario o usuario no existen"
        )


@router.put("/{id}", response_model=ConsultaResponse)
async def actualizar_consulta(
    id: int,
    request: ConsultaUpdateRequest,
    db: Session = Depends(get_db),
):
    """Actualiza una consulta existente.

    Args:
        id: ID de la consulta a actualizar.
        request: Campos a actualizar (todos opcionales).
        db: Sesión de base de datos.

    Returns:
        Consulta con los campos actualizados.

    Raises:
        HTTPException: Si no se encuentra la consulta o el usuario no existe.
    """
    crud = ConsultaCrud(db)
    update_data = request.model_dump(exclude_unset=True)
    if not update_data:
        raise HTTPException(status_code=400, detail="No se proporcionaron campos para actualizar")
    try:
        consulta = crud.actualizar_consulta(id, **update_data)
        if not consulta:
            raise HTTPException(status_code=404, detail="Consulta no encontrada")
        return consulta
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=404,
            detail="El usuario de edición no existe"
        )


@router.delete("/{id}", response_model=ConsultaDeleteResponse)
async def eliminar_consulta(id: int, db: Session = Depends(get_db)):
    """Elimina una consulta por su ID.

    Args:
        id: ID de la consulta a eliminar.
        db: Sesión de base de datos.

    Returns:
        Confirmación de eliminación.

    Raises:
        HTTPException: Si no se encuentra la consulta.
    """
    crud = ConsultaCrud(db)
    eliminado = crud.eliminar_consulta(id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Consulta no encontrada")
    return {"id": id, "eliminado": True}

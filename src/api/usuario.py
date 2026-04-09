"""
Endpoints API para la entidad Usuario.

Proporciona operaciones CRUD conectadas a la base de datos:
- GET /usuarios - Lista todos los usuarios
- GET /usuarios/{id} - Obtiene un usuario por ID
- POST /usuarios - Crea un nuevo usuario
- PUT /usuarios/{id} - Actualiza un usuario
- DELETE /usuarios/{id} - Elimina un usuario
"""

from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from src.database import get_db
from src.crud.usuario_crud import UsuarioCrud
from src.schemas.usuario import (
    UsuarioRequest,
    UsuarioUpdateRequest,
    UsuarioResponse,
    UsuarioDeleteResponse,
)

router = APIRouter(prefix="/usuarios", tags=["usuarios"])


@router.get("", response_model=dict)
async def listar_usuarios(db: Session = Depends(get_db)):
    """Lista todos los usuarios registrados.

    Args:
        db: Sesión de base de datos.

    Returns:
        Diccionario con total y lista de usuarios.
    """
    crud = UsuarioCrud(db)
    usuarios = crud.listar_usuarios()
    return {
        "total": len(usuarios),
        "items": [UsuarioResponse.model_validate(u) for u in usuarios],
    }


@router.get("/{id_usuario}", response_model=UsuarioResponse)
async def obtener_usuario(
    id_usuario: int = Path(..., description="ID del usuario"),
    db: Session = Depends(get_db),
):
    """Obtiene un usuario por su ID.

    Args:
        id_usuario: Identificador único del usuario.
        db: Sesión de base de datos.

    Returns:
        Datos del usuario encontrado.

    Raises:
        HTTPException: Si no se encuentra el usuario.
    """
    crud = UsuarioCrud(db)
    usuario = crud.buscar_usuario(id_usuario)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario


@router.post("", response_model=UsuarioResponse, status_code=201)
async def crear_usuario(request: UsuarioRequest, db: Session = Depends(get_db)):
    """Crea un nuevo usuario.

    Args:
        request: Datos del usuario a crear.
        db: Sesión de base de datos.

    Returns:
        Usuario creado con ID asignado.

    Raises:
        HTTPException: Si el username o email ya existen.
    """
    crud = UsuarioCrud(db)
    try:
        usuario = crud.crear_usuario(
            username=request.username,
            email=request.email,
            password_hash=request.password_hash,
            nombre=request.nombre,
            rol=request.rol,
        )
        return usuario
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="El username o email ya existen en el sistema"
        )


@router.put("/{id_usuario}", response_model=UsuarioResponse)
async def actualizar_usuario(
    id_usuario: int,
    request: UsuarioUpdateRequest,
    db: Session = Depends(get_db),
):
    """Actualiza un usuario existente.

    Args:
        id_usuario: ID del usuario a actualizar.
        request: Campos a actualizar (todos opcionales).
        db: Sesión de base de datos.

    Returns:
        Usuario con los campos actualizados.

    Raises:
        HTTPException: Si no se encuentra el usuario o si el username/email ya existen.
    """
    crud = UsuarioCrud(db)
    update_data = request.model_dump(exclude_unset=True)
    if not update_data:
        raise HTTPException(status_code=400, detail="No se proporcionaron campos para actualizar")
    try:
        usuario = crud.actualizar_usuario(id_usuario, **update_data)
        if not usuario:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        return usuario
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="El username o email ya existen en el sistema"
        )


@router.delete("/{id_usuario}", response_model=UsuarioDeleteResponse)
async def eliminar_usuario(id_usuario: int, db: Session = Depends(get_db)):
    """Elimina un usuario por su ID.

    Args:
        id_usuario: ID del usuario a eliminar.
        db: Sesión de base de datos.

    Returns:
        Confirmación de eliminación.

    Raises:
        HTTPException: Si no se encuentra el usuario.
    """
    crud = UsuarioCrud(db)
    eliminado = crud.eliminar_usuario(id_usuario)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return {"id_usuario": id_usuario, "eliminado": True}

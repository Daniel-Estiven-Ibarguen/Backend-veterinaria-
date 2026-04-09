"""
Endpoints API para la entidad Usuario.

Proporciona operaciones CRUD mockeadas:
- GET /usuarios - Lista todos los usuarios
- GET /usuarios/{id} - Obtiene un usuario por ID
- POST /usuarios - Crea un nuevo usuario
- PUT /usuarios/{id} - Actualiza un usuario
- DELETE /usuarios/{id} - Elimina un usuario
"""

from datetime import datetime
from typing import Optional

from fastapi import APIRouter, HTTPException, Path
from fastapi.responses import JSONResponse

from src.schemas.usuario import (
    UsuarioRequest,
    UsuarioUpdateRequest,
    UsuarioResponse,
    UsuarioDeleteResponse,
)

router = APIRouter(prefix="/usuarios", tags=["usuarios"])

MOCK_USUARIOS = [
    {
        "id_usuario": 1,
        "username": "drgarcia",
        "email": "drgarcia@vet.cl",
        "nombre": "Dr. María García",
        "rol": "veterinario",
        "fecha_creacion": datetime(2024, 1, 15, 8, 30, 0),
        "fecha_edicion": None,
    },
    {
        "id_usuario": 2,
        "username": "adminvet",
        "email": "admin@vet.cl",
        "nombre": "Carlos Admin",
        "rol": "admin",
        "fecha_creacion": datetime(2024, 1, 10, 9, 0, 0),
        "fecha_edicion": datetime(2024, 2, 20, 14, 30, 0),
    },
]


@router.get("", response_model=dict)
async def listar_usuarios():
    """Lista todos los usuarios registrados.

    Returns:
        Diccionario con total y lista de usuarios.
    """
    return {
        "total": len(MOCK_USUARIOS),
        "items": MOCK_USUARIOS,
    }


@router.get("/{id_usuario}", response_model=UsuarioResponse)
async def obtener_usuario(id_usuario: int = Path(..., description="ID del usuario")):
    """Obtiene un usuario por su ID.

    Args:
        id_usuario: Identificador único del usuario.

    Returns:
        Datos del usuario encontrado.

    Raises:
        HTTPException: Si no se encuentra el usuario.
    """
    for usuario in MOCK_USUARIOS:
        if usuario["id_usuario"] == id_usuario:
            return usuario
    raise HTTPException(status_code=404, detail="Usuario no encontrado")


@router.post("", response_model=UsuarioResponse, status_code=201)
async def crear_usuario(request: UsuarioRequest):
    """Crea un nuevo usuario.

    Args:
        request: Datos del usuario a crear.

    Returns:
        Usuario creado con ID asignado.
    """
    nuevo_id = max(u["id_usuario"] for u in MOCK_USUARIOS) + 1
    return {
        "id_usuario": nuevo_id,
        "username": request.username,
        "email": request.email,
        "nombre": request.nombre,
        "rol": request.rol,
        "fecha_creacion": datetime.now(),
        "fecha_edicion": None,
    }


@router.put("/{id_usuario}", response_model=UsuarioResponse)
async def actualizar_usuario(
    id_usuario: int,
    request: UsuarioUpdateRequest,
):
    """Actualiza un usuario existente.

    Args:
        id_usuario: ID del usuario a actualizar.
        request: Campos a actualizar (todos opcionales).

    Returns:
        Usuario con los campos actualizados.

    Raises:
        HTTPException: Si no se encuentra el usuario.
    """
    for usuario in MOCK_USUARIOS:
        if usuario["id_usuario"] == id_usuario:
            update_data = request.model_dump(exclude_unset=True)
            usuario.update(update_data)
            usuario["fecha_edicion"] = datetime.now()
            return usuario
    raise HTTPException(status_code=404, detail="Usuario no encontrado")


@router.delete("/{id_usuario}", response_model=UsuarioDeleteResponse)
async def eliminar_usuario(id_usuario: int):
    """Elimina un usuario por su ID.

    Args:
        id_usuario: ID del usuario a eliminar.

    Returns:
        Confirmación de eliminación.

    Raises:
        HTTPException: Si no se encuentra el usuario.
    """
    for usuario in MOCK_USUARIOS:
        if usuario["id_usuario"] == id_usuario:
            return {"id_usuario": id_usuario, "eliminado": True}
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

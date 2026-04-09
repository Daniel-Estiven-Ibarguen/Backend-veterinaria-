"""
Esquemas Pydantic para la entidad Usuario.

Contiene los modelos de request y response para las operaciones
CRUD de usuarios: crear, listar, obtener por id, actualizar y eliminar.
"""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, ConfigDict


class UsuarioRequest(BaseModel):
    """Modelo de petición para crear un usuario.

    Args:
        username: Nombre de usuario único.
        email: Correo electrónico único.
        password_hash: Hash de la contraseña.
        nombre: Nombre completo del usuario.
        rol: Rol del usuario (default: 'veterinario').
    """

    username: str
    email: EmailStr
    password_hash: str
    nombre: str
    rol: str = "veterinario"


class UsuarioUpdateRequest(BaseModel):
    """Modelo de petición para actualizar un usuario.

    Todos los campos son opcionales para permitir actualizaciones parciales.

    Args:
        username: Nuevo nombre de usuario (opcional).
        email: Nuevo correo electrónico (opcional).
        nombre: Nuevo nombre completo (opcional).
        rol: Nuevo rol (opcional).
    """

    username: Optional[str] = None
    email: Optional[EmailStr] = None
    nombre: Optional[str] = None
    rol: Optional[str] = None


class UsuarioResponse(BaseModel):
    """Modelo de respuesta para obtener un usuario.

    Incluye todos los campos del usuario incluyendo los de auditoría.

    Args:
        id_usuario: Identificador único del usuario.
        username: Nombre de usuario.
        email: Correo electrónico.
        nombre: Nombre completo.
        rol: Rol del usuario.
        fecha_creacion: Fecha y hora de creación.
        fecha_edicion: Fecha y hora de última edición (opcional).
    """

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id_usuario": 1,
                "username": "admin1",
                "email": "admin1@example.com",
                "nombre": "Admin Principal",
                "rol": "veterinario",
                "fecha_creacion": "2026-01-15T10:30:00",
                "fecha_edicion": None
            }
        }
    )

    id_usuario: int
    username: str
    email: str
    nombre: str
    rol: str
    fecha_creacion: datetime
    fecha_edicion: Optional[datetime] = None


class UsuarioDeleteResponse(BaseModel):
    """Modelo de respuesta tras eliminar un usuario.

    Args:
        id_usuario: Identificador del usuario eliminado.
        eliminado: Indica que la eliminación fue exitosa.
    """

    id_usuario: int
    eliminado: bool = True


class UsuarioListResponse(BaseModel):
    """Modelo de respuesta para listar usuarios.

    Args:
        total: Número total de usuarios.
        items: Lista de usuarios.
    """

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "total": 2,
                "items": [
                    {
                        "id_usuario": 1,
                        "username": "admin1",
                        "email": "admin1@example.com",
                        "nombre": "Admin Principal",
                        "rol": "veterinario",
                        "fecha_creacion": "2026-01-15T10:30:00",
                        "fecha_edicion": None
                    },
                    {
                        "id_usuario": 2,
                        "username": "vet1",
                        "email": "vet1@example.com",
                        "nombre": "Veterinario Uno",
                        "rol": "veterinario",
                        "fecha_creacion": "2026-01-16T11:00:00",
                        "fecha_edicion": None
                    }
                ]
            }
        }
    )

    total: int
    items: list[UsuarioResponse]

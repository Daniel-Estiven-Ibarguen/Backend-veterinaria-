"""
Esquemas Pydantic para la entidad Animal y sus subclases Gato y Perro.

Contiene los modelos de request y response para las operaciones
CRUD de animales: crear, listar, obtener por id, actualizar y eliminar.
"""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class AnimalRequest(BaseModel):
    """Modelo de petición para crear un animal.

    Args:
        nombre: Nombre del animal.
        edad: Edad en años.
        especie: Especie del animal (perro, gato, etc.).
        tipo: Discriminador para herencia polimórfica (default: 'animal').
        id_usuario_creacion: ID del usuario que crea el registro.
    """

    nombre: str
    edad: int
    especie: str
    tipo: str = "animal"
    id_usuario_creacion: int


class AnimalUpdateRequest(BaseModel):
    """Modelo de petición para actualizar un animal.

    Todos los campos son opcionales para permitir actualizaciones parciales.

    Args:
        nombre: Nuevo nombre (opcional).
        edad: Nueva edad (opcional).
        especie: Nueva especie (opcional).
        id_usuario_edita: ID del usuario que edita (opcional).
    """

    nombre: Optional[str] = None
    edad: Optional[int] = None
    especie: Optional[str] = None
    id_usuario_edita: Optional[int] = None


class AnimalResponse(BaseModel):
    """Modelo de respuesta para obtener un animal.

    Incluye todos los campos del animal incluyendo los de auditoría.

    Args:
        id: Identificador único del animal.
        nombre: Nombre del animal.
        edad: Edad en años.
        especie: Especie del animal.
        tipo: Discriminador de herencia polimórfica.
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
                "nombre": "Max",
                "edad": 5,
                "especie": "canino",
                "tipo": "perro",
                "id_usuario_creacion": 1,
                "id_usuario_edita": None,
                "fecha_creacion": "2026-01-15T10:30:00",
                "fecha_edicion": None
            }
        }
    )

    id: int
    nombre: str
    edad: int
    especie: str
    tipo: str
    id_usuario_creacion: int
    id_usuario_edita: Optional[int] = None
    fecha_creacion: datetime
    fecha_edicion: Optional[datetime] = None


class GatoRequest(AnimalRequest):
    """Modelo de petición para crear un gato.

    Hereda de AnimalRequest con tipo='gato' por defecto.
    """

    tipo: str = "gato"


class GatoUpdateRequest(AnimalUpdateRequest):
    """Modelo de petición para actualizar un gato.

    Hereda de AnimalUpdateRequest sin modificaciones.
    """

    pass


class GatoResponse(AnimalResponse):
    """Modelo de respuesta para obtener un gato.

    Hereda de AnimalResponse.
    """

    model_config = ConfigDict(from_attributes=True)


class PerroRequest(AnimalRequest):
    """Modelo de petición para crear un perro.

    Hereda de AnimalRequest con tipo='perro' por defecto.
    """

    tipo: str = "perro"


class PerroUpdateRequest(AnimalUpdateRequest):
    """Modelo de petición para actualizar un perro.

    Hereda de AnimalUpdateRequest sin modificaciones.
    """

    pass


class PerroResponse(AnimalResponse):
    """Modelo de respuesta para obtener un perro.

    Hereda de AnimalResponse.
    """

    model_config = ConfigDict(from_attributes=True)


class AnimalDeleteResponse(BaseModel):
    """Modelo de respuesta tras eliminar un animal.

    Args:
        id: Identificador del animal eliminado.
        eliminado: Indica que la eliminación fue exitosa.
    """

    id: int
    eliminado: bool = True


class AnimalListResponse(BaseModel):
    """Modelo de respuesta para listar animales.

    Args:
        total: Número total de animales.
        items: Lista de animales.
    """

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "total": 2,
                "items": [
                    {
                        "id": 1,
                        "nombre": "Max",
                        "edad": 5,
                        "especie": "canino",
                        "tipo": "perro",
                        "id_usuario_creacion": 1,
                        "id_usuario_edita": None,
                        "fecha_creacion": "2026-01-15T10:30:00",
                        "fecha_edicion": None
                    },
                    {
                        "id": 2,
                        "nombre": "Luna",
                        "edad": 3,
                        "especie": "felino",
                        "tipo": "gato",
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
    items: list[AnimalResponse]

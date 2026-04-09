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

    model_config = ConfigDict(from_attributes=True)

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

"""
Endpoints API para la entidad Animal y sus subclases Gato y Perro.

Proporciona operaciones CRUD mockeadas:
- GET /animales - Lista todos los animales
- GET /animales/{id} - Obtiene un animal por ID
- POST /animales - Crea un nuevo animal
- PUT /animales/{id} - Actualiza un animal
- DELETE /animales/{id} - Elimina un animal
"""

from datetime import datetime
from typing import Optional

from fastapi import APIRouter, HTTPException, Path

from src.schemas.animal import (
    AnimalRequest,
    AnimalUpdateRequest,
    AnimalResponse,
    AnimalDeleteResponse,
    GatoRequest,
    GatoUpdateRequest,
    GatoResponse,
    PerroRequest,
    PerroUpdateRequest,
    PerroResponse,
)

router = APIRouter(prefix="/animales", tags=["animales"])

MOCK_ANIMALES = [
    {
        "id": 1,
        "nombre": "Luna",
        "edad": 3,
        "especie": "felino",
        "tipo": "gato",
        "id_usuario_creacion": 1,
        "id_usuario_edita": None,
        "fecha_creacion": datetime(2024, 2, 1, 10, 0, 0),
        "fecha_edicion": None,
    },
    {
        "id": 2,
        "nombre": "Max",
        "edad": 5,
        "especie": "canino",
        "tipo": "perro",
        "id_usuario_creacion": 1,
        "id_usuario_edita": None,
        "fecha_creacion": datetime(2024, 2, 5, 11, 30, 0),
        "fecha_edicion": None,
    },
    {
        "id": 3,
        "nombre": "Rocky",
        "edad": 2,
        "especie": "canino",
        "tipo": "perro",
        "id_usuario_creacion": 2,
        "id_usuario_edita": None,
        "fecha_creacion": datetime(2024, 2, 10, 9, 15, 0),
        "fecha_edicion": None,
    },
]


@router.get("", response_model=dict)
async def listar_animales():
    """Lista todos los animales registrados.

    Returns:
        Diccionario con total y lista de animales.
    """
    return {
        "total": len(MOCK_ANIMALES),
        "items": MOCK_ANIMALES,
    }


@router.get("/{id}", response_model=AnimalResponse)
async def obtener_animal(id: int = Path(..., description="ID del animal")):
    """Obtiene un animal por su ID.

    Args:
        id: Identificador único del animal.

    Returns:
        Datos del animal encontrado.

    Raises:
        HTTPException: Si no se encuentra el animal.
    """
    for animal in MOCK_ANIMALES:
        if animal["id"] == id:
            return animal
    raise HTTPException(status_code=404, detail="Animal no encontrado")


@router.post("", response_model=AnimalResponse, status_code=201)
async def crear_animal(request: AnimalRequest):
    """Crea un nuevo animal.

    Args:
        request: Datos del animal a crear.

    Returns:
        Animal creado con ID asignado.
    """
    nuevo_id = max(a["id"] for a in MOCK_ANIMALES) + 1
    return {
        "id": nuevo_id,
        "nombre": request.nombre,
        "edad": request.edad,
        "especie": request.especie,
        "tipo": request.tipo,
        "id_usuario_creacion": request.id_usuario_creacion,
        "id_usuario_edita": None,
        "fecha_creacion": datetime.now(),
        "fecha_edicion": None,
    }


@router.put("/{id}", response_model=AnimalResponse)
async def actualizar_animal(
    id: int,
    request: AnimalUpdateRequest,
):
    """Actualiza un animal existente.

    Args:
        id: ID del animal a actualizar.
        request: Campos a actualizar (todos opcionales).

    Returns:
        Animal con los campos actualizados.

    Raises:
        HTTPException: Si no se encuentra el animal.
    """
    for animal in MOCK_ANIMALES:
        if animal["id"] == id:
            update_data = request.model_dump(exclude_unset=True)
            animal.update(update_data)
            animal["fecha_edicion"] = datetime.now()
            return animal
    raise HTTPException(status_code=404, detail="Animal no encontrado")


@router.delete("/{id}", response_model=AnimalDeleteResponse)
async def eliminar_animal(id: int):
    """Elimina un animal por su ID.

    Args:
        id: ID del animal a eliminar.

    Returns:
        Confirmación de eliminación.

    Raises:
        HTTPException: Si no se encuentra el animal.
    """
    for animal in MOCK_ANIMALES:
        if animal["id"] == id:
            return {"id": id, "eliminado": True}
    raise HTTPException(status_code=404, detail="Animal no encontrado")


@router.post("/gatos", response_model=GatoResponse, status_code=201)
async def crear_gato(request: GatoRequest):
    """Crea un nuevo gato.

    Args:
        request: Datos del gato a crear.

    Returns:
        Gato creado con ID asignado.
    """
    nuevo_id = max(a["id"] for a in MOCK_ANIMALES) + 1
    return {
        "id": nuevo_id,
        "nombre": request.nombre,
        "edad": request.edad,
        "especie": request.especie,
        "tipo": "gato",
        "id_usuario_creacion": request.id_usuario_creacion,
        "id_usuario_edita": None,
        "fecha_creacion": datetime.now(),
        "fecha_edicion": None,
    }


@router.post("/perros", response_model=PerroResponse, status_code=201)
async def crear_perro(request: PerroRequest):
    """Crea un nuevo perro.

    Args:
        request: Datos del perro a crear.

    Returns:
        Perro creado con ID asignado.
    """
    nuevo_id = max(a["id"] for a in MOCK_ANIMALES) + 1
    return {
        "id": nuevo_id,
        "nombre": request.nombre,
        "edad": request.edad,
        "especie": request.especie,
        "tipo": "perro",
        "id_usuario_creacion": request.id_usuario_creacion,
        "id_usuario_edita": None,
        "fecha_creacion": datetime.now(),
        "fecha_edicion": None,
    }

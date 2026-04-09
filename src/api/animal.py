"""
Endpoints API para la entidad Animal y sus subclases Gato y Perro.

Proporciona operaciones CRUD conectadas a la base de datos:
- GET /animales - Lista todos los animales
- GET /animales/{id} - Obtiene un animal por ID
- POST /animales - Crea un nuevo animal
- PUT /animales/{id} - Actualiza un animal
- DELETE /animales/{id} - Elimina un animal
"""

from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from src.database import get_db
from src.crud.animal_crud import AnimalCrud
from src.schemas.animal import (
    AnimalRequest,
    AnimalUpdateRequest,
    AnimalResponse,
    AnimalDeleteResponse,
    AnimalListResponse,
    GatoRequest,
    GatoResponse,
    PerroRequest,
    PerroResponse,
)

router = APIRouter(prefix="/animales", tags=["animales"])


@router.get("", response_model=AnimalListResponse)
async def listar_animales(db: Session = Depends(get_db)):
    """Lista todos los animales registrados.

    Args:
        db: Sesión de base de datos.

    Returns:
        Diccionario con total y lista de animales.
    """
    crud = AnimalCrud(db)
    animales = crud.listar_animales()
    return {
        "total": len(animales),
        "items": [AnimalResponse.model_validate(a) for a in animales],
    }


@router.get("/{id}", response_model=AnimalResponse)
async def obtener_animal(
    id: int = Path(..., description="ID del animal"),
    db: Session = Depends(get_db),
):
    """Obtiene un animal por su ID.

    Args:
        id: Identificador único del animal.
        db: Sesión de base de datos.

    Returns:
        Datos del animal encontrado.

    Raises:
        HTTPException: Si no se encuentra el animal.
    """
    crud = AnimalCrud(db)
    animal = crud.buscar_animal(id)
    if not animal:
        raise HTTPException(status_code=404, detail="Animal no encontrado")
    return animal


@router.post("", response_model=AnimalResponse, status_code=201)
async def crear_animal(request: AnimalRequest, db: Session = Depends(get_db)):
    """Crea un nuevo animal.

    Args:
        request: Datos del animal a crear.
        db: Sesión de base de datos.

    Returns:
        Animal creado con ID asignado.

    Raises:
        HTTPException: Si el usuario de creación no existe.
    """
    crud = AnimalCrud(db)
    try:
        animal = crud.crear_animal(
            nombre=request.nombre,
            edad=request.edad,
            especie=request.especie,
            tipo=request.tipo,
            id_usuario_creacion=request.id_usuario_creacion,
        )
        return animal
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=404,
            detail="El usuario de creación no existe"
        )


@router.put("/{id}", response_model=AnimalResponse)
async def actualizar_animal(
    id: int,
    request: AnimalUpdateRequest,
    db: Session = Depends(get_db),
):
    """Actualiza un animal existente.

    Args:
        id: ID del animal a actualizar.
        request: Campos a actualizar (todos opcionales).
        db: Sesión de base de datos.

    Returns:
        Animal con los campos actualizados.

    Raises:
        HTTPException: Si no se encuentra el animal o el usuario no existe.
    """
    crud = AnimalCrud(db)
    update_data = request.model_dump(exclude_unset=True)
    if not update_data:
        raise HTTPException(status_code=400, detail="No se proporcionaron campos para actualizar")
    try:
        animal = crud.actualizar_animal(id, **update_data)
        if not animal:
            raise HTTPException(status_code=404, detail="Animal no encontrado")
        return animal
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=404,
            detail="El usuario de edición no existe"
        )


@router.delete("/{id}", response_model=AnimalDeleteResponse)
async def eliminar_animal(id: int, db: Session = Depends(get_db)):
    """Elimina un animal por su ID.

    Args:
        id: ID del animal a eliminar.
        db: Sesión de base de datos.

    Returns:
        Confirmación de eliminación.

    Raises:
        HTTPException: Si no se encuentra el animal.
    """
    crud = AnimalCrud(db)
    eliminado = crud.eliminar_animal(id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Animal no encontrado")
    return {"id": id, "eliminado": True}


@router.post("/gatos", response_model=GatoResponse, status_code=201)
async def crear_gato(request: GatoRequest, db: Session = Depends(get_db)):
    """Crea un nuevo gato.

    Args:
        request: Datos del gato a crear.
        db: Sesión de base de datos.

    Returns:
        Gato creado con ID asignado.

    Raises:
        HTTPException: Si el usuario de creación no existe.
    """
    crud = AnimalCrud(db)
    try:
        gato = crud.crear_gato(
            nombre=request.nombre,
            edad=request.edad,
            especie=request.especie,
            id_usuario_creacion=request.id_usuario_creacion,
        )
        return gato
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=404,
            detail="El usuario de creación no existe"
        )


@router.post("/perros", response_model=PerroResponse, status_code=201)
async def crear_perro(request: PerroRequest, db: Session = Depends(get_db)):
    """Crea un nuevo perro.

    Args:
        request: Datos del perro a crear.
        db: Sesión de base de datos.

    Returns:
        Perro creado con ID asignado.

    Raises:
        HTTPException: Si el usuario de creación no existe.
    """
    crud = AnimalCrud(db)
    try:
        perro = crud.crear_perro(
            nombre=request.nombre,
            edad=request.edad,
            especie=request.especie,
            id_usuario_creacion=request.id_usuario_creacion,
        )
        return perro
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=404,
            detail="El usuario de creación no existe"
        )

from typing import List, Optional

from sqlalchemy.orm import Session

from src.models.animal import Animal
from src.models.gato import Gato
from src.models.perro import Perro


class AnimalCrud:
    """CRUD para la entidad Animal y sus subclases Gato y Perro.

    Maneja las operaciones de base de datos para la tabla 'animales'
    usando una sesión de SQLAlchemy.

    Args:
        db: Sesión activa de SQLAlchemy.
    """

    def __init__(self, db: Session):
        self.db = db

    def crear_animal(
        self,
        nombre: str,
        edad: int,
        especie: str,
        tipo: str = "animal",
        id_usuario_creacion: int = None,  # type: ignore
    ) -> Animal:
        """Crea un nuevo animal en la base de datos.

        Args:
            nombre: Nombre del animal.
            edad: Edad en años.
            especie: Especie del animal.
            tipo: Discriminador para herencia polimórfica.
            id_usuario_creacion: ID del usuario que crea el registro.

        Returns:
            El objeto Animal recién creado con su ID asignado.
        """
        animal = Animal(
            nombre=nombre.strip(),
            edad=edad,
            especie=especie.strip().lower(),
            tipo=tipo.lower(),
            id_usuario_creacion=id_usuario_creacion,
        )

        self.db.add(animal)
        self.db.commit()
        self.db.refresh(animal)
        return animal

    def crear_gato(
        self,
        nombre: str,
        edad: int,
        especie: str = "felino",
        id_usuario_creacion: int = None,  # type: ignore
    ) -> Gato:
        """Crea un nuevo gato en la base de datos.

        Args:
            nombre: Nombre del gato.
            edad: Edad en años.
            especie: Especie del gato (default: 'felino').
            id_usuario_creacion: ID del usuario que crea el registro.

        Returns:
            El objeto Gato recién creado con su ID asignado.
        """
        gato = Gato(
            nombre=nombre.strip(),
            edad=edad,
            especie=especie.strip().lower(),
            tipo="gato",
            id_usuario_creacion=id_usuario_creacion,
        )

        self.db.add(gato)
        self.db.commit()
        self.db.refresh(gato)
        return gato

    def crear_perro(
        self,
        nombre: str,
        edad: int,
        especie: str = "canino",
        id_usuario_creacion: int = None,  # type: ignore
    ) -> Perro:
        """Crea un nuevo perro en la base de datos.

        Args:
            nombre: Nombre del perro.
            edad: Edad en años.
            especie: Especie del perro (default: 'canino').
            id_usuario_creacion: ID del usuario que crea el registro.

        Returns:
            El objeto Perro recién creado con su ID asignado.
        """
        perro = Perro(
            nombre=nombre.strip(),
            edad=edad,
            especie=especie.strip().lower(),
            tipo="perro",
            id_usuario_creacion=id_usuario_creacion,
        )

        self.db.add(perro)
        self.db.commit()
        self.db.refresh(perro)
        return perro

    def buscar_animal(self, id: int) -> Optional[Animal]:
        """Busca un animal por su ID.

        Args:
            id: ID del animal a buscar.

        Returns:
            El objeto Animal si existe, None si no se encuentra.
        """
        return self.db.query(Animal).filter(Animal.id == id).first()

    def listar_animales(self) -> List[Animal]:
        """Obtiene todos los animales registrados en la base de datos.

        Returns:
            Lista de objetos Animal. Retorna una lista vacía si no hay animales.
        """
        return self.db.query(Animal).all()

    def listar_gatos(self) -> List[Gato]:
        """Obtiene todos los gatos registrados en la base de datos.

        Returns:
            Lista de objetos Gato.
        """
        return self.db.query(Gato).all()

    def listar_perros(self) -> List[Perro]:
        """Obtiene todos los perros registrados en la base de datos.

        Returns:
            Lista de objetos Perro.
        """
        return self.db.query(Perro).all()

    def actualizar_animal(self, id: int, **kwargs) -> Optional[Animal]:
        """Actualiza los campos de un animal existente.

        Solo se actualizan los campos que se pasen como argumentos.
        Los campos que no existan en el modelo son ignorados.

        Args:
            id: ID del animal a actualizar.
            **kwargs: Campos a actualizar con sus nuevos valores.

        Returns:
            El objeto Animal actualizado, None si no existe.
        """
        animal = self.buscar_animal(id)

        if not animal:
            return None

        for key, value in kwargs.items():
            if hasattr(animal, key):
                setattr(animal, key, value)

        self.db.commit()
        return animal

    def eliminar_animal(self, id: int) -> bool:
        """Elimina un animal de la base de datos.

        Args:
            id: ID del animal a eliminar.

        Returns:
            True si el animal fue eliminado, False si no existe.
        """
        animal = self.buscar_animal(id)

        if not animal:
            return False

        self.db.delete(animal)
        self.db.commit()
        return True

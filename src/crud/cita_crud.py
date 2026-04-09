from typing import List, Optional

from sqlalchemy.orm import Session

from src.models.cita import Cita


class CitaCrud:
    """CRUD para la entidad Cita.

    Maneja las operaciones de base de datos para la tabla 'citas'
    usando una sesión de SQLAlchemy.

    Args:
        db: Sesión activa de SQLAlchemy.
    """

    def __init__(self, db: Session):
        self.db = db

    def crear_cita(
        self,
        fecha,
        hora,
        id_animal: int,
        id_veterinario: int,
        tipo: str = "revision",
        estado: str = "pendiente",
        id_usuario_creacion: int = None,  # type: ignore
    ) -> Cita:
        """Crea una nueva cita en la base de datos.

        Args:
            fecha: Fecha de la cita.
            hora: Hora de la cita.
            id_animal: ID del animal asociado.
            id_veterinario: ID del veterinario asignado.
            tipo: Tipo de cita (default: 'revision').
            estado: Estado de la cita (default: 'pendiente').
            id_usuario_creacion: ID del usuario que crea el registro.

        Returns:
            El objeto Cita recién creado con su ID asignado.
        """
        cita = Cita(
            fecha=fecha,
            hora=hora,
            tipo=tipo.lower(),
            estado=estado.lower(),
            id_animal=id_animal,
            id_veterinario=id_veterinario,
            id_usuario_creacion=id_usuario_creacion,
        )

        self.db.add(cita)
        self.db.commit()
        self.db.refresh(cita)
        return cita

    def buscar_cita(self, id: int) -> Optional[Cita]:
        """Busca una cita por su ID.

        Args:
            id: ID de la cita a buscar.

        Returns:
            El objeto Cita si existe, None si no se encuentra.
        """
        return self.db.query(Cita).filter(Cita.id == id).first()

    def listar_citas(self) -> List[Cita]:
        """Obtiene todas las citas registradas en la base de datos.

        Returns:
            Lista de objetos Cita. Retorna una lista vacía si no hay citas.
        """
        return self.db.query(Cita).all()

    def actualizar_cita(self, id: int, **kwargs) -> Optional[Cita]:
        """Actualiza los campos de una cita existente.

        Solo se actualizan los campos que se pasen como argumentos.
        Los campos que no existan en el modelo son ignorados.

        Args:
            id: ID de la cita a actualizar.
            **kwargs: Campos a actualizar con sus nuevos valores.

        Returns:
            El objeto Cita actualizado, None si no existe.
        """
        cita = self.buscar_cita(id)

        if not cita:
            return None

        for key, value in kwargs.items():
            if hasattr(cita, key):
                setattr(cita, key, value)

        self.db.commit()
        self.db.refresh(cita)
        return cita

    def eliminar_cita(self, id: int) -> bool:
        """Elimina una cita de la base de datos.

        Args:
            id: ID de la cita a eliminar.

        Returns:
            True si la cita fue eliminada, False si no existe.
        """
        cita = self.buscar_cita(id)

        if not cita:
            return False

        self.db.delete(cita)
        self.db.commit()
        return True

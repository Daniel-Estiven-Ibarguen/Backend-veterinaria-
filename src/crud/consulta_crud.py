from typing import List, Optional

from sqlalchemy.orm import Session

from src.models.consulta import Consulta


class ConsultaCrud:
    """CRUD para la entidad Consulta.

    Maneja las operaciones de base de datos para la tabla 'consultas'
    usando una sesión de SQLAlchemy.

    Args:
        db: Sesión activa de SQLAlchemy.
    """

    def __init__(self, db: Session):
        self.db = db

    def crear_consulta(
        self,
        fecha,
        diagnostico: str,
        tratamiento: str,
        tipo_consulta: str,
        id_cita: int,
        id_animal: int,
        id_veterinario: int,
        observaciones: Optional[str] = None,
        motivo_revision: Optional[str] = None,
        proxima_cita=None,
        nivel_urgencia: Optional[int] = None,
        sintomas: Optional[str] = None,
        id_usuario_creacion: int = None,  # type: ignore
    ) -> Consulta:
        """Crea una nueva consulta en la base de datos.

        Args:
            fecha: Fecha de la consulta.
            diagnostico: Diagnóstico realizado.
            tratamiento: Tratamiento prescrito.
            tipo_consulta: Tipo de consulta ('revision', 'urgencia').
            id_cita: ID de la cita asociada.
            id_animal: ID del animal consultado.
            id_veterinario: ID del veterinario que atendió.
            observaciones: Observaciones adicionales (opcional).
            motivo_revision: Motivo de revisión (solo para tipo 'revision').
            proxima_cita: Fecha próxima cita (solo para tipo 'revision').
            nivel_urgencia: Nivel 1-5 (solo para tipo 'urgencia').
            sintomas: Síntomas presentados (solo para tipo 'urgencia').
            id_usuario_creacion: ID del usuario que crea el registro.

        Returns:
            El objeto Consulta recién creado con su ID asignado.
        """
        consulta = Consulta(
            fecha=fecha,
            diagnostico=diagnostico,
            tratamiento=tratamiento,
            observaciones=observaciones,
            tipo_consulta=tipo_consulta.lower(),
            motivo_revision=motivo_revision,
            proxima_cita=proxima_cita,
            nivel_urgencia=nivel_urgencia,
            sintomas=sintomas,
            id_cita=id_cita,
            id_animal=id_animal,
            id_veterinario=id_veterinario,
            id_usuario_creacion=id_usuario_creacion,
        )

        self.db.add(consulta)
        self.db.commit()
        self.db.refresh(consulta)
        return consulta

    def buscar_consulta(self, id: int) -> Optional[Consulta]:
        """Busca una consulta por su ID.

        Args:
            id: ID de la consulta a buscar.

        Returns:
            El objeto Consulta si existe, None si no se encuentra.
        """
        return self.db.query(Consulta).filter(Consulta.id == id).first()

    def listar_consultas(self) -> List[Consulta]:
        """Obtiene todas las consultas registradas en la base de datos.

        Returns:
            Lista de objetos Consulta. Retorna una lista vacía si no hay consultas.
        """
        return self.db.query(Consulta).all()

    def actualizar_consulta(self, id: int, **kwargs) -> Optional[Consulta]:
        """Actualiza los campos de una consulta existente.

        Solo se actualizan los campos que se pasen como argumentos.
        Los campos que no existan en el modelo son ignorados.

        Args:
            id: ID de la consulta a actualizar.
            **kwargs: Campos a actualizar con sus nuevos valores.

        Returns:
            El objeto Consulta actualizado, None si no existe.
        """
        consulta = self.buscar_consulta(id)

        if not consulta:
            return None

        for key, value in kwargs.items():
            if hasattr(consulta, key):
                setattr(consulta, key, value)

        self.db.commit()
        return consulta

    def eliminar_consulta(self, id: int) -> bool:
        """Elimina una consulta de la base de datos.

        Args:
            id: ID de la consulta a eliminar.

        Returns:
            True si la consulta fue eliminada, False si no existe.
        """
        consulta = self.buscar_consulta(id)

        if not consulta:
            return False

        self.db.delete(consulta)
        self.db.commit()
        return True

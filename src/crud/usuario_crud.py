from typing import List, Optional

from sqlalchemy.orm import Session

from src.models.usuario import Usuario


class UsuarioCrud:
    """CRUD para la entidad Usuario.

    Maneja las operaciones de base de datos para la tabla 'usuarios'
    usando una sesión de SQLAlchemy.

    Args:
        db: Sesión activa de SQLAlchemy.
    """

    def __init__(self, db: Session):
        self.db = db

    def crear_usuario(
        self,
        username: str,
        email: str,
        password_hash: str,
        nombre: str,
        rol: str = "veterinario",
    ) -> Usuario:
        """Crea un nuevo usuario en la base de datos.

        Args:
            username: Nombre de usuario único.
            email: Correo electrónico único.
            password_hash: Hash de la contraseña del usuario.
            nombre: Nombre completo del usuario.
            rol: Rol del usuario, puede ser 'veterinario' o 'admin'.

        Returns:
            El objeto Usuario recién creado con su ID asignado.
        """
        usuario = Usuario(
            username=username.strip().lower(),
            email=email.strip().lower(),
            password_hash=password_hash,
            nombre=nombre.strip(),
            rol=rol.strip().lower(),
        )

        self.db.add(usuario)
        self.db.commit()
        self.db.refresh(usuario)
        return usuario

    def buscar_usuario(self, id_usuario: int) -> Optional[Usuario]:
        """Busca un usuario por su ID.

        Args:
            id_usuario: ID del usuario a buscar.

        Returns:
            El objeto Usuario si existe, None si no se encuentra.
        """
        return (
            self.db.query(Usuario)
            .filter(Usuario.id_usuario == id_usuario)
            .first()
        )

    def buscar_por_username(self, username: str) -> Optional[Usuario]:
        """Busca un usuario por su nombre de usuario.

        Args:
            username: Nombre de usuario a buscar.

        Returns:
            El objeto Usuario si existe, None si no se encuentra.
        """
        return (
            self.db.query(Usuario)
            .filter(Usuario.username == username.strip().lower())
            .first()
        )

    def listar_usuarios(self) -> List[Usuario]:
        """Obtiene todos los usuarios registrados en la base de datos.

        Returns:
            Lista de objetos Usuario. Retorna una lista vacía si no hay usuarios.
        """
        return self.db.query(Usuario).all()

    def actualizar_usuario(self, id_usuario: int, **kwargs) -> Optional[Usuario]:
        """Actualiza los campos de un usuario existente.

        Solo se actualizan los campos que se pasen como argumentos.
        Los campos que no existan en el modelo son ignorados.

        Args:
            id_usuario: ID del usuario a actualizar.
            **kwargs: Campos a actualizar con sus nuevos valores.

        Returns:
            El objeto Usuario actualizado, None si no existe.
        """
        usuario = self.buscar_usuario(id_usuario)

        if not usuario:
            return None

        for key, value in kwargs.items():
            if hasattr(usuario, key):
                setattr(usuario, key, value)

        self.db.commit()
        return usuario

    def eliminar_usuario(self, id_usuario: int) -> bool:
        """Elimina un usuario de la base de datos.

        Args:
            id_usuario: ID del usuario a eliminar.

        Returns:
            True si el usuario fue eliminado, False si no existe.
        """
        usuario = self.buscar_usuario(id_usuario)

        if not usuario:
            return False

        self.db.delete(usuario)
        self.db.commit()
        return True
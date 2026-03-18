"""
Módulo de entidad Usuario.

Define la tabla 'usuarios' en la base de datos PostgreSQL/Neon.
Esta entidad es fundamental ya que otras tablas referencian
a los usuarios para las columnas de auditoría.

Atributos:
- id_usuario: Primary key de la tabla
- username: Nombre de usuario único
- email: Correo electrónico único
- password_hash: Hash de la contraseña
- nombre: Nombre completo del usuario
- rol: Rol del usuario (veterinario, admin, etc.)
"""

from sqlalchemy import Column, Integer, String
from src.database import Base


class Usuario(Base):
    __tablename__ = "usuarios"

    id_usuario = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False, index=True)
    email = Column(String(100), unique=True, nullable=False, index=True)
    password_hash = Column(String(255), nullable=False)
    nombre = Column(String(100), nullable=False)
    rol = Column(String(20), nullable=False, default="veterinario")

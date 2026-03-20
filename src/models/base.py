"""
Módulo de modelo base con columnas de auditoría.

Este módulo define BaseModel, una clase abstracta que proporciona
columnas de auditoría comunes para todas las entidades que requieren
trazabilidad de creación y modificación.

Columnas inclusivas:
- id: Primary key genérico
- id_usuario_creacion: FK al usuario que creó el registro
- id_usuario_edita: FK al usuario que editó el registro
- fecha_creacion: Fecha y hora de creación (server_default=func.now())
- fecha_edicion: Fecha y hora de edición (onupdate=func.now())
"""

from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from src.database import Base


class BaseModel(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True)

    id_usuario_creacion = Column(
        Integer,
        ForeignKey("usuarios.id_usuario", name="fk_base_usuario_creacion"),
        nullable=False
    )

    id_usuario_edita = Column(
        Integer,
        ForeignKey("usuarios.id_usuario", name="fk_base_usuario_edita"),
        nullable=True
    )

    fecha_creacion = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )

    fecha_edicion = Column(
        DateTime(timezone=True),
        onupdate=func.now(),
        nullable=True
    )

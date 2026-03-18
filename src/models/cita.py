"""
Módulo de entidad Cita.

Define la tabla 'citas' en la base de datos PostgreSQL/Neon.
Esta entidad representa citas médicas agendadas en la veterinaria
y hereda las columnas de auditoría de BaseModel.

Atributos:
- id: Primary key (heredado)
- fecha: Fecha de la cita
- hora: Hora de la cita
- tipo: Tipo de cita ('revision', 'urgencias')
- estado: Estado de la cita ('pendiente', 'confirmada', 'cancelada')
- id_animal: FK a animales.id
- id_veterinario: FK a usuarios.id_usuario
- Columnas de auditoría (heredadas de BaseModel)
"""

from sqlalchemy import Column, Integer, String, Date, Time, ForeignKey, Enum
from sqlalchemy.orm import relationship
from src.models.base import BaseModel
import enum


class TipoCita(enum.Enum):
    REVISION = "revision"
    URGENCIAS = "urgencias"


class EstadoCita(enum.Enum):
    PENDIENTE = "pendiente"
    CONFIRMADA = "confirmada"
    CANCELADA = "cancelada"


class Cita(BaseModel):
    __tablename__ = "citas"

    fecha = Column(Date, nullable=False)
    hora = Column(Time, nullable=False)
    tipo = Column(String(20), nullable=False, default="revision")
    estado = Column(String(20), nullable=False, default="pendiente")
    id_animal = Column(
        Integer,
        ForeignKey("animales.id", name="fk_cita_animal"),
        nullable=False
    )
    id_veterinario = Column(
        Integer,
        ForeignKey("usuarios.id_usuario", name="fk_cita_veterinario"),
        nullable=False
    )

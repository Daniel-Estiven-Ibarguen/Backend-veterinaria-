"""
Módulo de entidad Animal.

Define la tabla 'animales' en la base de datos PostgreSQL/Neon.
Esta entidad representa cualquier animal registrado en la veterinaria
y hereda las columnas de auditoría de BaseModel.

Es la clase base para herencia de tabla (joined table inheritance)
con las subclases Gato y Perro.

Atributos:
- id: Primary key (heredado)
- nombre: Nombre del animal
- edad: Edad en años
- especie: Especie del animal (perro, gato, etc.)
- tipo: Discriminador para herencia polimórfica
- Columnas de auditoría (heredadas de BaseModel)
"""

from sqlalchemy import Column, Integer, String
from src.models.base import BaseModel


class Animal(BaseModel):
    __tablename__ = "animales"

    nombre = Column(String(100), nullable=False)
    edad = Column(Integer, nullable=False)
    especie = Column(String(50), nullable=False)
    tipo = Column(String(20), nullable=False, default="animal")

    __mapper_args__ = {
        "polymorphic_on": tipo,
        "polymorphic_identity": "animal"
    }

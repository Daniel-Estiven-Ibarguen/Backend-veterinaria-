"""
Módulo de entidad Perro.

Define la tabla 'perros' en la base de datos PostgreSQL/Neon.
Esta entidad representa perros específicos en la veterinaria,
con una relación FK a la tabla animales (herencia de tabla).

Atributos:
- id_animal: FK a animales.id (primary key y relación de herencia)
"""

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.models.animal import Animal


class Perro(Animal):
    __tablename__ = "perros"

    id = Column(
        Integer,
        ForeignKey("animales.id", name="fk_perro_animal"),
        primary_key=True
    )

    # Aquí, joined table inheritance se emplea para implementar
    # la herencia a lo largo de varias tablas. Así, cada clase se
    # representa con su propia tabla que incluye solo los atributos
    # específicos de esa clase, y una clave foránea que apunta a la
    # tabla base.

    __mapper_args__ = {
        "polymorphic_identity": "perro"
    }

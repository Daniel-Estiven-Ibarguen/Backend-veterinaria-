"""
Módulo de entidad Gato.

Define la tabla 'gatos' en la base de datos PostgreSQL/Neon.
Esta entidad representa gatos específicos en la veterinaria,
con una relación FK a la tabla animales (herencia de tabla).

Atributos:
- id_animal: FK a animales.id (primary key y relación de herencia)
"""

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.models.animal import Animal


class Gato(Animal):
    __tablename__ = "gatos"

    id = Column(
        Integer,
        ForeignKey("animales.id", name="fk_gato_animal"),
        primary_key=True
    )

    __mapper_args__ = {
        "polymorphic_identity": "gato"
    }

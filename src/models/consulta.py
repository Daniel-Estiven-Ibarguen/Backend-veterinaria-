"""
Módulo de entidad Consulta.

Define la tabla 'consultas' en la base de datos PostgreSQL/Neon.
Esta entidad representa consultas médicas realizadas en la veterinaria
y consolida los tipos de consulta (revisión y urgencias) mediante un
campo discriminador.

Atributos:
- id: Primary key (heredado)
- fecha: Fecha de la consulta
- diagnostico: Diagnóstico realizado
- tratamiento: Tratamiento prescrito
- observaciones: Observaciones adicionales
- tipo_consulta: Tipo de consulta ('revision', 'urgencia')
- motivo_revision: Motivo de revisión (solo para tipo 'revision')
- proxima_cita: Fecha próxima cita (solo para tipo 'revision')
- nivel_urgencia: Nivel 1-5 (solo para tipo 'urgencia')
- sintomas: Síntomas presentados (solo para tipo 'urgencia')
- id_cita: FK a citas.id
- id_animal: FK a animales.id
- id_veterinario: FK a usuarios.id_usuario
- Columnas de auditoría (heredadas de BaseModel)
"""

from sqlalchemy import Column, Integer, String, Date, ForeignKey
from src.models.base import BaseModel


class Consulta(BaseModel):
    __tablename__ = "consultas"

    fecha = Column(Date, nullable=False)
    diagnostico = Column(String(500), nullable=False)
    tratamiento = Column(String(500), nullable=False)
    observaciones = Column(String(500), nullable=True)
    tipo_consulta = Column(String(20), nullable=False)

    motivo_revision = Column(String(200), nullable=True)
    proxima_cita = Column(Date, nullable=True)

    nivel_urgencia = Column(Integer, nullable=True)
    sintomas = Column(String(500), nullable=True)

    id_cita = Column(
        Integer,
        ForeignKey("citas.id", name="fk_consulta_cita"),
        nullable=False
    )
    id_animal = Column(
        Integer,
        ForeignKey("animales.id", name="fk_consulta_animal"),
        nullable=False
    )
    id_veterinario = Column(
        Integer,
        ForeignKey("usuarios.id_usuario", name="fk_consulta_veterinario"),
        nullable=False
    )

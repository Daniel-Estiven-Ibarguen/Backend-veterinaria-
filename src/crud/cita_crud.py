from typing import List, Optional
from uuid import UUID

from entities.cita import Cita
from sqlalchemy.orm import Session  # type: ignore


class CitaCrud:

    def __init__(self, db: Session):
        self.db = db

    def crear_cita(
        self,
        id_cita: int,
        fecha: str,
        hora: str,
        nombre_mascota: str,
        nombre_veterinario: str,
        tipo: str,
        estado: str,
    ) -> Cita:

        cita = Cita(
            id_cita,
            fecha=fecha.strip(),
            hora=hora.strip(),
            nombre_mascota=nombre_mascota.strip().lower(),
            nombre_veterinario=nombre_veterinario.strip().lower(),
            tipo=tipo.lower(),
            estado=estado.lower(),
        )

        self.db.add(cita)
        self.db.commit()
        self.db.refresh(cita)
        return cita

    def buscar_cita(self, id_cita) -> Optional[Cita]:

        return self.db.query(Cita).filter(Cita.id_cita == id_cita).first()

    def actualizar_cita(self, id_cita: UUID, **kwargs) -> Optional[Cita]:

        cita = self.db.query(Cita).filter(Cita.id_cita == id_cita).first

        if not cita:
            return None

        if "fecha" in kwargs:
            fecha = kwargs["fecha"]

        if "hora" in kwargs:
            hora = kwargs["hora"]

        if "nombre_mascota" in kwargs:
            nombre_mascota = kwargs["nombre_mascota"]

        if "nombre_veterinario" in kwargs:
            nombre_veterinario = kwargs["nombre_veterinario"]

        if "tipo" in kwargs:
            tipo = kwargs["tipo"]

        if "estado" in kwargs:
            estado = kwargs["estado"]

        for key, value in kwargs.items():
            if hasattr(cita, key):
                setattr(cita, key, value)

        self.db.commit()
        self.db.refresh()

        return cita

    def eliminar_cita(self, id_cita) -> bool:

        cita = self.db.query(Cita).filter(Cita.id_cita == id_cita).first()

        if cita:
            self.db.delete(cita)
            self.db.commit()
            return True

        return False

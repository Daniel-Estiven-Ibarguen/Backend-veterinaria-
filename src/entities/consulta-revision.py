from src.entities.consulta import consulta


class ConsultaRevision(consulta):

    def __init__(
        self,
        id_consulta: int,
        fecha: str,
        diagnostico: str,
        tratamiento: str,
        observaciones: str,
        id_cita: int,
        id_mascota: int,
        id_veterinario: int,
        motivo_revision: str,
        proxima_cita: str,
    ) -> None:

        super().__init__(
            id_consulta,
            fecha,
            diagnostico,
            tratamiento,
            observaciones,
            id_cita,
            id_mascota,
            id_veterinario,
        )
        self.__motivo_revision = motivo_revision
        self.__proxima_cita = proxima_cita

    @property
    def motivo_revision(self) -> str:
        return self.__motivo_revision

    @property
    def proxima_cita(self) -> str:
        return self.__proxima_cita

    @motivo_revision.setter
    def motivo_revision(self, nuevo_valor: str) -> None:
        if nuevo_valor is None or nuevo_valor == "":
            print("El motivo de revisión no puede estar vacío")
        else:
            self.__motivo_revision = nuevo_valor

    @proxima_cita.setter
    def proxima_cita(self, nuevo_valor: str) -> None:
        if nuevo_valor is None or nuevo_valor == "":
            print("La próxima cita no puede estar vacía")
        else:
            self.__proxima_cita = nuevo_valor

    def __str__(self) -> str:
        return (
            f"ConsultaRevision [ID: {self.id_consulta}] - Fecha: {self.fecha} | "
            f"Motivo: {self.__motivo_revision} | Próxima cita: {self.__proxima_cita}"
        )
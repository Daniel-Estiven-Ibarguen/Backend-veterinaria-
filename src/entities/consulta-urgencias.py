from src.entities.consulta import consulta


class ConsultaUrgencias(consulta):

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
        nivel_urgencia: int,
        sintomas: str,
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
        self.__nivel_urgencia = nivel_urgencia
        self.__sintomas = sintomas

    @property
    def nivel_urgencia(self) -> int:
        return self.__nivel_urgencia

    @property
    def sintomas(self) -> str:
        return self.__sintomas

    @nivel_urgencia.setter
    def nivel_urgencia(self, nuevo_valor: int) -> None:
        if nuevo_valor is None or not (1 <= nuevo_valor <= 5):
            print("El nivel de urgencia debe estar entre 1 y 5")
        else:
            self.__nivel_urgencia = nuevo_valor

    @sintomas.setter
    def sintomas(self, nuevo_valor: str) -> None:
        if nuevo_valor is None or nuevo_valor == "":
            print("Los síntomas no pueden estar vacíos")
        else:
            self.__sintomas = nuevo_valor

    def __str__(self) -> str:
        return (
            f"ConsultaUrgencias [ID: {self.id_consulta}] - Fecha: {self.fecha} | "
            f"Nivel urgencia: {self.__nivel_urgencia}/5 | Síntomas: {self.__sintomas}"
        )
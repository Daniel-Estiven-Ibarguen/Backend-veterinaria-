class consulta:

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
    ) -> None:

        self.__id_consulta = id_consulta
        self.__fecha = fecha
        self.__diagnostico = diagnostico
        self.__tratamiento = tratamiento
        self.__observaciones = observaciones
        self.__id_cita = id_cita
        self.__id_mascota = id_mascota
        self.__id_veterinario = id_veterinario

    @property
    def id_consulta(self) -> int:

        return self.__id_consulta

    @property
    def fecha(self) -> str:

        return self.__fecha

    @property
    def diagnostico(self) -> str:

        return self.__diagnostico

    @property
    def tratamiento(self) -> str:

        return self.__tratamiento

    @property
    def observaciones(self) -> str:

        return self.__observaciones

    @property
    def id_cita(self) -> int:

        return self.__id_cita

    @property
    def id_mascota(self) -> int:

        return self.__id_mascota

    @property
    def id_veterinario(self) -> int:

        return self.__id_veterinario

    @diagnostico.setter
    def diagnostico(self, nuevo_valor: str) -> None:

        if nuevo_valor is None or nuevo_valor == "":
            print("El diagnostico no puede estar vacio")

        else:
            self.__diagnostico = nuevo_valor

    @tratamiento.setter
    def tratamiento(self, nuevo_valor: str) -> None:

        if nuevo_valor is None or nuevo_valor == "":
            print("El tratamiento no puede estar vacio")

        else:
            self.__tratamiento = nuevo_valor

    @observaciones.setter
    def observaciones(self, nuevo_valor) -> None:

        if nuevo_valor is None or nuevo_valor == "":
            print("Las observaciones no pueden estar vacias")

        else:

            self.__observaciones = nuevo_valor

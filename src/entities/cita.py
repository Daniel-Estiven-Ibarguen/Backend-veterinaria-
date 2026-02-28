class Cita:

    def __init__(
        self,
        id_cita: int,
        fecha: str,
        hora: str,
        nombre_mascota: str,
        nombre_veterinario: str,
        tipo: str,
        estado: str = "pendiente",
    ) -> None:

        self.__id_cita = id_cita
        self.__fecha = fecha
        self.__hora = hora
        self.__nombre_mascota = nombre_mascota
        self.__nombre_veterinario = nombre_veterinario
        self.__tipo = tipo
        self.__estado = estado

    @property
    def id_cita(self) -> int:
        return self.__id_cita

    @property
    def fecha(self) -> str:
        return self.__fecha

    @property
    def hora(self) -> str:
        return self.__hora

    @property
    def nombre_mascota(self) -> str:
        return self.__nombre_mascota

    @property
    def nombre_veterinario(self) -> str:
        return self.__nombre_veterinario

    @property
    def tipo(self) -> str:
        return self.__tipo

    @property
    def estado(self) -> str:
        return self.__estado

    @fecha.setter
    def fecha(self, nuevo_valor: str) -> None:
        if nuevo_valor is None or nuevo_valor == "":
            print("La fecha no puede estar vacía")
        else:
            self.__fecha = nuevo_valor

    @hora.setter
    def hora(self, nuevo_valor: str) -> None:
        if nuevo_valor is None or nuevo_valor == "":
            print("La hora no puede estar vacía")
        else:
            self.__hora = nuevo_valor

    @nombre_mascota.setter
    def nombre_mascota(self, nuevo_valor: str) -> None:
        if nuevo_valor is None or nuevo_valor == "":
            print("El nombre de la mascota no puede estar vacío")
        else:
            self.__nombre_mascota = nuevo_valor

    @nombre_veterinario.setter
    def nombre_veterinario(self, nuevo_valor: str) -> None:
        if nuevo_valor is None or nuevo_valor == "":
            print("El nombre del veterinario no puede estar vacío")
        else:
            self.__nombre_veterinario = nuevo_valor

    @tipo.setter
    def tipo(self, nuevo_valor: str) -> None:
        if nuevo_valor not in ("revision", "urgencias"):
            print("El tipo debe ser 'revision' o 'urgencias'")
        else:
            self.__tipo = nuevo_valor

    @estado.setter
    def estado(self, nuevo_valor: str) -> None:
        if nuevo_valor not in ("pendiente", "confirmada", "cancelada"):
            print("El estado debe ser 'pendiente', 'confirmada' o 'cancelada'")
        else:
            self.__estado = nuevo_valor

    def __str__(self) -> str:
        return (
            f"[{self.__id_cita}] {self.__fecha} {self.__hora} | "
            f"Mascota: {self.__nombre_mascota} | "
            f"Veterinario: {self.__nombre_veterinario} | "
            f"Tipo: {self.__tipo} | Estado: {self.__estado}"
        )
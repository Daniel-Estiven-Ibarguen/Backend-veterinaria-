class Animal:
    """Representa un animal en la veterinaria."""

    def __init__(self, nombre: str, edad: int, especie: str) -> None:
        self.__nombre = nombre
        self.__edad = edad
        self.__especie = especie

    @property
    def nombre(self) -> str:
        """Retorna el nombre del animal."""
        return self.__nombre

    @property
    def edad(self) -> int:
        """Retorna la edad del animal."""
        return self.__edad

    def emitir_sonido(self) -> str:
        """Retorna el sonido genérico del animal."""
        return "..."

    def __str__(self) -> str:
        return f"{self.__especie}: {self.__nombre}, {self.__edad} años"

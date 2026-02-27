from typing import override

from src.entities.animal import Animal


class Gato(Animal):
    def __init__(self, nombre: str, edad: int) -> None:
        super().__init__(nombre, edad, "Perro")

    @override
    def emitir_sonido(self) -> str:
        return "Guau"

    def cavar(self) -> None:
        print("El perro está cavando")

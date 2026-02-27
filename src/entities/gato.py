from typing import override

from src.entities.animal import Animal


class Gato(Animal):
    def __init__(self, nombre: str, edad: int) -> None:
        super().__init__(nombre, edad, "Gato")

    @override
    def emitir_sonido(self) -> str:
        return "Miau"

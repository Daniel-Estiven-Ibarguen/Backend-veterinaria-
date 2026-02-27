from src.entities.animal import Animal


class Gato(Animal):
    def __init__(self, nombre: str, edad: int) -> None:
        super().__init__(nombre, edad, "Perro")

    def hacer_sonido(self) -> str:
        return "Guau"

    def cavar() -> None:
        print("El perro está cavando")

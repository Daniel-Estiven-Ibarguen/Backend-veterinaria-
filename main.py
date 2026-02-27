from src.entities.animal import Animal
from src.entities.gato import Gato
from src.entities.perro import Perro

# Lista para almacenar los animales
animales: list[Animal] = []


def crear_gato() -> None:
    """Crea un nuevo gato y lo agrega a la lista."""
    nombre = input("Nombre del gato: ")
    edad = int(input("Edad del gato: "))
    gato = Gato(nombre, edad)
    animales.append(gato)
    print(f"Gato '{nombre}' creado correctamente")


def crear_perro() -> None:
    """Crea un nuevo perro y lo agrega a la lista."""
    nombre = input("Nombre del perro: ")
    edad = int(input("Edad del perro: "))
    perro = Perro(nombre, edad)
    animales.append(perro)
    print(f"Perro '{nombre}' creado correctamente")


def crear_animal() -> None:
    """Crea un animal genérico y lo agrega a la lista."""
    nombre = input("Nombre del animal: ")
    edad = int(input("Edad del animal: "))
    especie = input("Especie del animal: ")
    animal = Animal(nombre, edad, especie)
    animales.append(animal)
    print(f"Animal '{nombre}' ({especie}) creado correctamente")


def consultar_animales() -> None:
    """Muestra todos los animales registrados."""
    if not animales:
        print("No hay animales registrados")
        return

    print("\n=== Animales Registrados ===")
    for i, animal in enumerate(animales, 1):
        print(f"{i}. {animal} - Sonido: {animal.emitir_sonido()}")
    print()


def mostrar_menu() -> None:
    """Muestra el menú principal."""
    print("=== Menú Veterinaria ===")
    print("1. Crear gato")
    print("2. Crear perro")
    print("3. Crear animal genérico")
    print("4. Consultar animales")
    print("5. Salir")


def ejecutar_opcion(opcion: str) -> None:
    """Ejecuta la opción seleccionada."""
    match opcion:
        case "1":
            crear_gato()
        case "2":
            crear_perro()
        case "3":
            crear_animal()
        case "4":
            consultar_animales()
        case "5":
            print("¡Hasta luego!")
        case _:
            print("Opción inválida")


def main() -> None:
    """Función principal del programa."""
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción: ")
        if opcion == "5":
            ejecutar_opcion(opcion)
            break
        ejecutar_opcion(opcion)


if __name__ == "__main__":
    main()

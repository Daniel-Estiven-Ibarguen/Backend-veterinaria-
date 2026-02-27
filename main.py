from src.entities.animal import Animal
from src.entities.gato import Gato
from src.entities.perro import Perro

# Lista para almacenar los animales
animales: list[Animal] = []


def es_entero_positivo(valor: str) -> bool:
    """Valida que el valor sea un entero positivo."""
    try:
        num = int(valor)
        return num > 0
    except ValueError:
        return False


def es_string_no_vacio(valor: str) -> bool:
    """Valida que el valor no sea vacío o solo espacios."""
    return bool(valor and valor.strip())


def obtener_nombre(prompt: str) -> str:
    """Obtiene un nombre válido (string no vacío)."""
    while True:
        nombre = input(prompt)
        if es_string_no_vacio(nombre):
            return nombre.strip()
        print("Error: El nombre no puede estar vacío")


def obtener_edad(prompt: str) -> int:
    """Obtiene una edad válida (entero positivo)."""
    while True:
        edad = input(prompt)
        if es_entero_positivo(edad):
            return int(edad)
        print("Error: La edad debe ser un número entero positivo")


def obtener_especie(prompt: str) -> str:
    """Obtiene una especie válida (string no vacío)."""
    while True:
        especie = input(prompt)
        if es_string_no_vacio(especie):
            return especie.strip()
        print("Error: La especie no puede estar vacía")


def crear_gato() -> None:
    """Crea un nuevo gato y lo agrega a la lista."""
    nombre = obtener_nombre("Nombre del gato: ")
    edad = obtener_edad("Edad del gato: ")
    gato = Gato(nombre, edad)
    animales.append(gato)
    print(f"Gato '{nombre}' creado correctamente")


def crear_perro() -> None:
    """Crea un nuevo perro y lo agrega a la lista."""
    nombre = obtener_nombre("Nombre del perro: ")
    edad = obtener_edad("Edad del perro: ")
    perro = Perro(nombre, edad)
    animales.append(perro)
    print(f"Perro '{nombre}' creado correctamente")


def crear_animal() -> None:
    """Crea un animal genérico y lo agrega a la lista."""
    nombre = obtener_nombre("Nombre del animal: ")
    edad = obtener_edad("Edad del animal: ")
    especie = obtener_especie("Especie del animal: ")
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

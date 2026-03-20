from src.entities.animal import Animal
from src.entities.gato import Gato
from src.entities.perro import Perro
from src.entities.cita import Cita

# Listas para almacenar los registros
animales: list[Animal] = []
citas: list[Cita] = []
contador_citas: int = 0


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


# --- Animales ---

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


# --- CRUD Citas ---

def _buscar_cita(id_cita: int) -> Cita | None:
    """Busca una cita por su ID."""
    for cita in citas:
        if cita.id_cita == id_cita:
            return cita
    return None


def crear_cita() -> None:
    """Crea una nueva cita y la agrega a la lista."""
    global contador_citas

    fecha = obtener_nombre("Fecha (dd/mm/aaaa): ")
    hora = obtener_nombre("Hora (hh:mm): ")
    nombre_mascota = obtener_nombre("Nombre de la mascota: ")
    nombre_veterinario = obtener_nombre("Nombre del veterinario: ")

    while True:
        tipo = input("Tipo de cita (revision/urgencias): ").strip().lower()
        if tipo in ("revision", "urgencias"):
            break
        print("Error: El tipo debe ser 'revision' o 'urgencias'")

    contador_citas += 1
    cita = Cita(contador_citas, fecha, hora, nombre_mascota, nombre_veterinario, tipo)
    citas.append(cita)
    print(f"Cita #{contador_citas} creada correctamente")


def listar_citas() -> None:
    """Muestra todas las citas registradas."""
    if not citas:
        print("No hay citas registradas")
        return

    print("\n=== Citas Registradas ===")
    for cita in citas:
        print(f"  {cita}")
    print()


def actualizar_cita() -> None:
    """Actualiza los datos de una cita existente."""
    listar_citas()
    if not citas:
        return

    while True:
        id_input = input("ID de la cita a actualizar: ")
        if es_entero_positivo(id_input):
            break
        print("Error: Ingrese un ID válido")

    cita = _buscar_cita(int(id_input))
    if cita is None:
        print(f"No se encontró la cita con ID {id_input}")
        return

    print(f"\nCita encontrada: {cita}")
    print("Deje en blanco para mantener el valor actual\n")

    nueva_fecha = input(f"Nueva fecha [{cita.fecha}]: ").strip()
    if nueva_fecha:
        cita.fecha = nueva_fecha

    nueva_hora = input(f"Nueva hora [{cita.hora}]: ").strip()
    if nueva_hora:
        cita.hora = nueva_hora

    nuevo_mascota = input(f"Nueva mascota [{cita.nombre_mascota}]: ").strip()
    if nuevo_mascota:
        cita.nombre_mascota = nuevo_mascota

    nuevo_vet = input(f"Nuevo veterinario [{cita.nombre_veterinario}]: ").strip()
    if nuevo_vet:
        cita.nombre_veterinario = nuevo_vet

    nuevo_tipo = input(f"Nuevo tipo [{cita.tipo}] (revision/urgencias): ").strip().lower()
    if nuevo_tipo:
        cita.tipo = nuevo_tipo

    nuevo_estado = input(f"Nuevo estado [{cita.estado}] (pendiente/confirmada/cancelada): ").strip().lower()
    if nuevo_estado:
        cita.estado = nuevo_estado

    print("Cita actualizada correctamente")


def eliminar_cita() -> None:
    """Elimina una cita por su ID."""
    listar_citas()
    if not citas:
        return

    while True:
        id_input = input("ID de la cita a eliminar: ")
        if es_entero_positivo(id_input):
            break
        print("Error: Ingrese un ID válido")

    cita = _buscar_cita(int(id_input))
    if cita is None:
        print(f"No se encontró la cita con ID {id_input}")
        return

    citas.remove(cita)
    print(f"Cita #{id_input} eliminada correctamente")
    
# --- CRUD Usuarios ---
def crear_usuario() -> None:
    """Solicita los datos por consola y crea un nuevo usuario en la base de datos.

    Valida que el rol ingresado sea 'veterinario' o 'admin' antes de guardar.
    """
    username = obtener_nombre("Username: ")
    email = obtener_nombre("Email: ")
    password_hash = obtener_nombre("Password hash: ")
    nombre = obtener_nombre("Nombre completo: ")

    while True:
        rol = input("Rol (veterinario/admin): ").strip().lower()
        if rol in ("veterinario", "admin"):
            break
        print("Error: El rol debe ser 'veterinario' o 'admin'")

    db = SessionLocal()
    try:
        crud = UsuarioCrud(db)
        usuario = crud.crear_usuario(username, email, password_hash, nombre, rol)
        print(f"Usuario '{usuario.username}' creado con ID {usuario.id_usuario}")
    finally:
        db.close()


def listar_usuarios() -> None:
    """Consulta la base de datos y muestra todos los usuarios registrados por consola."""
    db = SessionLocal()
    try:
        crud = UsuarioCrud(db)
        usuarios = crud.listar_usuarios()
        if not usuarios:
            print("No hay usuarios registrados")
            return
        print("\n=== Usuarios Registrados ===")
        for u in usuarios:
            print(f"  [{u.id_usuario}] {u.username} | {u.email} | {u.nombre} | rol: {u.rol}")
        print()
    finally:
        db.close()


def actualizar_usuario() -> None:
    """Solicita por consola qué campos modificar y actualiza el usuario en la base de datos.

    Muestra la lista de usuarios, pide el ID a modificar y permite cambiar
    nombre, email y rol. Los campos que se dejen en blanco no se modifican.
    """
    listar_usuarios()

    while True:
        id_input = input("ID del usuario a actualizar: ")
        if es_entero_positivo(id_input):
            break
        print("Error: Ingrese un ID válido")

    db = SessionLocal()
    try:
        crud = UsuarioCrud(db)
        usuario = crud.buscar_usuario(int(id_input))
        if not usuario:
            print(f"No se encontró el usuario con ID {id_input}")
            return

        print(f"\nUsuario encontrado: {usuario.username} ({usuario.nombre})")
        print("Deje en blanco para mantener el valor actual\n")

        cambios = {}

        nuevo_nombre = input(f"Nuevo nombre [{usuario.nombre}]: ").strip()
        if nuevo_nombre:
            cambios["nombre"] = nuevo_nombre

        nuevo_email = input(f"Nuevo email [{usuario.email}]: ").strip()
        if nuevo_email:
            cambios["email"] = nuevo_email.lower()

        nuevo_rol = input(f"Nuevo rol [{usuario.rol}] (veterinario/admin): ").strip().lower()
        if nuevo_rol and nuevo_rol in ("veterinario", "admin"):
            cambios["rol"] = nuevo_rol

        if cambios:
            crud.actualizar_usuario(int(id_input), **cambios)
            print("Usuario actualizado correctamente")
        else:
            print("No se realizaron cambios")
    finally:
        db.close()


def eliminar_usuario() -> None:
    """Solicita un ID por consola y elimina el usuario correspondiente de la base de datos.

    Muestra la lista de usuarios antes de pedir el ID para facilitar la selección.
    """
    listar_usuarios()

    while True:
        id_input = input("ID del usuario a eliminar: ")
        if es_entero_positivo(id_input):
            break
        print("Error: Ingrese un ID válido")

    db = SessionLocal()
    try:
        crud = UsuarioCrud(db)
        eliminado = crud.eliminar_usuario(int(id_input))
        if eliminado:
            print(f"Usuario #{id_input} eliminado correctamente")
        else:
            print(f"No se encontró el usuario con ID {id_input}")
    finally:
        db.close()

# --- Menú ---

def mostrar_menu() -> None:
    """Muestra el menú principal."""
    print("\n=== Menú Veterinaria ===")
    print("--- Animales ---")
    print("1. Crear gato")
    print("2. Crear perro")
    print("3. Crear animal genérico")
    print("4. Listar animales")
    print("--- Citas ---")
    print("5. Crear cita")
    print("6. Listar citas")
    print("7. Actualizar cita")
    print("8. Eliminar cita")
    print("----------------")
    print("9. Salir")


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
            crear_cita()
        case "6":
            listar_citas()
        case "7":
            actualizar_cita()
        case "8":
            eliminar_cita()
        case "9":
            print("¡Hasta luego!")
        case _:
            print("Opción inválida")


def main() -> None:
    """Función principal del programa."""
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción: ")
        if opcion == "9":
            ejecutar_opcion(opcion)
            break
        ejecutar_opcion(opcion)


if __name__ == "__main__":
    main()
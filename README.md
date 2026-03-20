# Backend Veterinaria

Sistema de gestión para una veterinaria que permite gestionar animales y citas mediante programación orientada a objetos.

## Descripción

Este proyecto implementa un sistema de gestión para una veterinaria. Permite crear y consultar diferentes tipos de animales (gatos, perros y genéricos), y gestionar citas médicas con operaciones CRUD completas. Utiliza conceptos de Programación Orientada a Objetos (POO) para modelar la jerarquía de entidades.

## Instalación

Es necesario crear un entorno virtual e instalar las dependencias:

```bash
python -m venv .venv
pip install -r requirements.txt
```

Adicionalmente, es necesario establecer las credenciales de acceso de la base de datos Postgres (Neon) en el archivo `.env`. Se puede usar el archivo `.env.example` como plantilla.

```bash
cp .env.example .env
```

## Clases Implementadas

### Animal (Clase Base)
Representa un animal genérico en la veterinaria.

- **Atributos privados**: `__nombre`, `__edad`, `__especie`
- **Propiedades**: `nombre`, `edad` (solo lectura)
- **Métodos**: `emitir_sonido()`, `__str__()`

### Gato (hereda de Animal)
- Override de `emitir_sonido()` → retorna `"Miau"`

### Perro (hereda de Animal)
- Override de `emitir_sonido()` → retorna `"Guau"`
- Método adicional: `cavar()`

---

### Consulta (Clase Base)
Representa una consulta médica en la veterinaria.

- **Atributos privados**: `__id_consulta`, `__fecha`, `__diagnostico`, `__tratamiento`, `__observaciones`, `__id_cita`, `__id_mascota`, `__id_veterinario`
- **Setters con validación**: `diagnostico`, `tratamiento`, `observaciones`

### ConsultaRevision (hereda de Consulta)
Consulta de tipo revisión periódica.

- **Atributos adicionales**: `motivo_revision`, `proxima_cita`
- Setters con validación para ambos atributos

### ConsultaUrgencias (hereda de Consulta)
Consulta de tipo urgencia médica.

- **Atributos adicionales**: `nivel_urgencia` (1-5), `sintomas`
- Setter de `nivel_urgencia` valida rango 1-5

---

### Cita
Representa una cita médica agendada.

- **Atributos**: `id_cita`, `fecha`, `hora`, `nombre_mascota`, `nombre_veterinario`, `tipo`, `estado`
- `tipo`: `"revision"` o `"urgencias"`
- `estado`: `"pendiente"` (por defecto), `"confirmada"` o `"cancelada"`

## Técnicas de POO Aplicadas

| Técnica | Descripción |
|---------|-------------|
| **Herencia** | `Gato`, `Perro` → `Animal` / `ConsultaRevision`, `ConsultaUrgencias` → `Consulta` |
| **Polimorfismo** | Override de `emitir_sonido()` en subclases |
| **Encapsulamiento** | Atributos privados con `@property` y setters validados |
| **Abstracción** | Clases base `Animal` y `Consulta` como modelos del dominio |

## Estructura del Proyecto

```
Backend-veterinaria-/
├── main.py                        # Punto de entrada con menú interactivo
├── readme.md                      # Documentación del proyecto
└── src/
    └── entities/
        ├── animal.py              # Clase base Animal
        ├── gato.py                # Clase Gato
        ├── perro.py               # Clase Perro
        ├── consulta.py            # Clase base Consulta
        ├── consulta_revision.py   # Clase ConsultaRevision
        ├── consulta_urgencias.py  # Clase ConsultaUrgencias
        └── cita.py                # Clase Cita
```

## Uso del Menú

Ejecutar `python main.py` y seleccionar una opción:

**Animales**
1. Crear gato
2. Crear perro
3. Crear animal genérico
4. Listar animales

**Citas (CRUD)**
5. Crear cita
6. Listar citas
7. Actualizar cita
8. Eliminar cita

---
9. Salir

---

## Base de Datos

### Tecnología

- **Neon**: PostgreSQL en la nube (https://neon.tech)
- **SQLAlchemy**: ORM para gestión de modelos y relaciones
- **Alembic**: Sistema de migraciones para evolución del esquema

### Configuración

1. Copiar el archivo de ejemplo:
```bash
cp .env.example .env
```

2. Editar `.env` con las credenciales de Neon:
```
DATABASE_URL=postgresql://usuario:contraseña@host.neon.tech/nombre_db?sslmode=require
```

### Migraciones

Las migraciones se encuentran en el directorio `alembic/versions/`.

**Comandos útiles:**

```bash
# Ver estado de migraciones
alembic current

# Crear una nueva migración
alembic revision --autogenerate -m "descripcion_del_cambio"

# Aplicar migraciones pendientes
alembic upgrade head

# Revertir última migración
alembic downgrade -1

# Ver historial de migraciones
alembic history
```
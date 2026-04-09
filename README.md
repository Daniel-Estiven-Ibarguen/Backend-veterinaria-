# Backend Veterinaria API

Sistema de gestión para una veterinaria con API REST construida con FastAPI.

## Descripción

Este proyecto implementa una API REST para gestionar animales, citas y consultas de una veterinaria. Utiliza FastAPI para los endpoints, SQLAlchemy para la persistencia en PostgreSQL (Neon), y Alembic para migraciones de base de datos.

## Tecnologías

- **FastAPI**: Framework web async para API REST
- **SQLAlchemy**: ORM para gestión de modelos y relaciones
- **PostgreSQL/Neon**: Base de datos relacional en la nube
- **Alembic**: Sistema de migraciones para evolución del esquema
- **Pydantic**: Validación de datos y schemas de request/response

## Instalación

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
```

## Configuración

1. Copiar el archivo de ejemplo:
```bash
cp .env.example .env
```

2. Editar `.env` con las credenciales de Neon:
```
DATABASE_URL=postgresql://usuario:contraseña@host.neon.tech/nombre_db?sslmode=require
DATABASE_ECHO=false
```

## Ejecución

```bash
# Aplicar migraciones
alembic upgrade head

# Iniciar el servidor
uvicorn src.api.main:app --reload --port 8000
```

La API estará disponible en `http://localhost:8000`

## Endpoints

### Animales
| Método | Endpoint | Descripción |
|--------|-----------|-------------|
| GET | `/animales` | Lista todos los animales |
| GET | `/animales/{id}` | Obtiene un animal por ID |
| POST | `/animales` | Crea un nuevo animal |
| PUT | `/animales/{id}` | Actualiza un animal |
| DELETE | `/animales/{id}` | Elimina un animal |
| POST | `/animales/gatos` | Crea un gato |
| POST | `/animales/perros` | Crea un perro |

### Usuarios
| Método | Endpoint | Descripción |
|--------|-----------|-------------|
| GET | `/usuarios` | Lista todos los usuarios |
| GET | `/usuarios/{id}` | Obtiene un usuario por ID |
| POST | `/usuarios` | Crea un nuevo usuario |
| PUT | `/usuarios/{id}` | Actualiza un usuario |
| DELETE | `/usuarios/{id}` | Elimina un usuario |

### Citas
| Método | Endpoint | Descripción |
|--------|-----------|-------------|
| GET | `/citas` | Lista todas las citas |
| GET | `/citas/{id}` | Obtiene una cita por ID |
| POST | `/citas` | Crea una nueva cita |
| PUT | `/citas/{id}` | Actualiza una cita |
| DELETE | `/citas/{id}` | Elimina una cita |

### Consultas
| Método | Endpoint | Descripción |
|--------|-----------|-------------|
| GET | `/consultas` | Lista todas las consultas |
| GET | `/consultas/{id}` | Obtiene una consulta por ID |
| POST | `/consultas` | Crea una nueva consulta |
| PUT | `/consultas/{id}` | Actualiza una consulta |
| DELETE | `/consultas/{id}` | Elimina una consulta |

## Documentación Interactive

FastAPI genera automáticamente documentación interactiva:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Manejo de Errores

La API retorna códigos de error HTTP apropiados:

| Código | Descripción |
|--------|-------------|
| 400 | Bad Request - Body vacío en PUT |
| 404 | Not Found - Recurso no existe o FK no existe |
| 409 | Conflict - Duplicado (username/email ya existe) |
| 422 | Unprocessable Entity - Validación de datos |

## Base de Datos

### Migraciones

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

## Estructura del Proyecto

```
Backend-veterinaria-/
├── main.py                    # CLI legacy (menú interactivo)
├── alembic/                   # Migraciones de base de datos
│   └── versions/
├── src/
│   ├── api/                   # Endpoints FastAPI
│   │   ├── main.py           # App FastAPI
│   │   ├── animal.py
│   │   ├── usuario.py
│   │   ├── cita.py
│   │   └── consulta.py
│   ├── crud/                  # Operaciones de base de datos
│   │   ├── animal_crud.py
│   │   ├── usuario_crud.py
│   │   ├── cita_crud.py
│   │   └── consulta_crud.py
│   ├── models/                # Modelos SQLAlchemy
│   │   ├── animal.py
│   │   ├── usuario.py
│   │   ├── cita.py
│   │   └── consulta.py
│   ├── schemas/               # Schemas Pydantic
│   │   ├── animal.py
│   │   ├── usuario.py
│   │   ├── cita.py
│   │   └── consulta.py
│   └── database.py            # Configuración de conexión
├── .env.example
└── requirements.txt
```

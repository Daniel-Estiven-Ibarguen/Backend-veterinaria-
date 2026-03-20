# Mapeo entre Entities y Models

## Resumen de Migración

Este documento describe el mapeo entre las clases del módulo `src/entities` (clases de dominio puras en Python) y las clases del módulo `src/models` (modelos ORM SQLAlchemy).

---

## Tabla de Mapeo

| Entity (src/entities) | Model (src/models) | Cambios Principales |
|----------------------|--------------------|--------------------|
| `Animal` | `Animal` | Hereda de `BaseModel`, agrega columnas de auditoría y campo `tipo` para herencia polimórfica |
| `Perro` | `Perro` | Usa joined table inheritance con FK a `animales.id` |
| `Gato` | `Gato` | Usa joined table inheritance con FK a `animales.id` |
| `Cita` | `Cita` | Hereda de `BaseModel`, usa FKs en lugar de nombres, agrega auditoría |
| `consulta` | `Consulta` | Hereda de `BaseModel`, consolida revisiones y urgencias en una tabla |
| `ConsultaRevision` | Consolidado en `Consulta` | Campos específicos: `motivo_revision`, `proxima_cita` |
| `ConsultaUrgencias` | Consolidado en `Consulta` | Campos específicos: `nivel_urgencia`, `sintomas` |
| - | `Usuario` | Nuevo modelo para gestión de usuarios |
| - | `BaseModel` | Nueva clase abstracta con columnas de auditoría |

---

## Detalle por Clase

### 1. Animal

**Entity (`src/entities/animal.py`):**
```python
class Animal:
    def __init__(self, nombre: str, edad: int, especie: str) -> None:
        self.__nombre = nombre
        self.__edad = edad
        self.__especie = especie
```

**Model (`src/models/animal.py`):**
```python
class Animal(BaseModel):
    __tablename__ = "animales"
    nombre = Column(String(100), nullable=False)
    edad = Column(Integer, nullable=False)
    especie = Column(String(50), nullable=False)
    tipo = Column(String(20), nullable=False, default="animal")
```

**Cambios:**
- Hereda de `BaseModel` (agrega `id` y columnas de auditoría)
- Agrega campo `tipo` como discriminador para herencia polimórfica
- Los atributos privados (`__nombre`) se reemplazan por columnas ORM

---

### 2. Perro

**Entity (`src/entities/perro.py`):**
```python
class Perro(Animal):
    def __init__(self, nombre: str, edad: int) -> None:
        super().__init__(nombre, edad, "Perro")
    
    def emitir_sonido(self) -> str:
        return "Guau"
    
    def cavar(self) -> None:
        print("El perro está cavando")
```

**Model (`src/models/perro.py`):**
```python
class Perro(Animal):
    __tablename__ = "perros"
    id = Column(Integer, ForeignKey("animales.id"), primary_key=True)
```

**Cambios:**
- Implementa joined table inheritance
- El método `emitir_sonido()` y `cavar()` se eliminan (no mapeables a BD)
- Usa FK a `animales.id` como primary key

---

### 3. Gato

**Entity (`src/entities/gato.py`):**
```python
class Gato(Animal):
    def __init__(self, nombre: str, edad: int) -> None:
        super().__init__(nombre, edad, "Gato")
    
    def emitir_sonido(self) -> str:
        return "Miau"
```

**Model (`src/models/gato.py`):**
```python
class Gato(Animal):
    __tablename__ = "gatos"
    id = Column(Integer, ForeignKey("animales.id"), primary_key=True)
```

**Cambios:**
- Implementa joined table inheritance
- El método `emitir_sonido()` se elimina
- Usa FK a `animales.id` como primary key

---

### 4. Cita

**Entity (`src/entities/cita.py`):**
```python
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
        # Atributos privados con getters/setters
```

**Model (`src/models/cita.py`):**
```python
class Cita(BaseModel):
    __tablename__ = "citas"
    fecha = Column(Date, nullable=False)
    hora = Column(Time, nullable=False)
    tipo = Column(String(20), nullable=False, default="revision")
    estado = Column(String(20), nullable=False, default="pendiente")
    id_animal = Column(Integer, ForeignKey("animales.id"), nullable=False)
    id_veterinario = Column(Integer, ForeignKey("usuarios.id_usuario"), nullable=False)
```

**Cambios:**
- Hereda de `BaseModel` (agrega `id` y auditoría)
- `nombre_mascota` → `id_animal` (FK a animales)
- `nombre_veterinario` → `id_veterinario` (FK a usuarios)
- Tipos de datos: `str` → `Date`/`Time` apropiados
- Los setters con validación se eliminan (validación en schemas Pydantic)

---

### 5. Consulta (Consolidación)

**Entity - Clase base (`src/entities/consulta.py`):**
```python
class consulta:
    def __init__(
        self,
        id_consulta: int,
        fecha: str,
        diagnostico: str,
        tratamiento: str,
        observaciones: str,
        id_cita: int,
        id_mascota: int,
        id_veterinario: int,
    ) -> None:
```

**Entity - ConsultaRevision (`src/entities/consulta-revision.py`):**
```python
class ConsultaRevision(consulta):
    def __init__(
        self,
        # ... parámetros base ...
        motivo_revision: str,
        proxima_cita: str,
    ) -> None:
```

**Entity - ConsultaUrgencias (`src/entities/consulta-urgencias.py`):**
```python
class ConsultaUrgencias(consulta):
    def __init__(
        self,
        # ... parámetros base ...
        nivel_urgencia: int,
        sintomas: str,
    ) -> None:
```

**Model - Consolidado (`src/models/consulta.py`):**
```python
class Consulta(BaseModel):
    __tablename__ = "consultas"
    fecha = Column(Date, nullable=False)
    diagnostico = Column(String(500), nullable=False)
    tratamiento = Column(String(500), nullable=False)
    observaciones = Column(String(500), nullable=True)
    tipo_consulta = Column(String(20), nullable=False)
    
    # Campos para revisión
    motivo_revision = Column(String(200), nullable=True)
    proxima_cita = Column(Date, nullable=True)
    
    # Campos para urgencias
    nivel_urgencia = Column(Integer, nullable=True)
    sintomas = Column(String(500), nullable=True)
    
    # Foreign Keys
    id_cita = Column(Integer, ForeignKey("citas.id"), nullable=False)
    id_animal = Column(Integer, ForeignKey("animales.id"), nullable=False)
    id_veterinario = Column(Integer, ForeignKey("usuarios.id_usuario"), nullable=False)
```

**Cambios:**
- Las 3 clases (`consulta`, `ConsultaRevision`, `ConsultaUrgencias`) se consolidan en una sola tabla
- Se usa campo `tipo_consulta` como discriminador
- `id_mascota` → `id_animal` (consistencia de nomenclatura)
- Hereda auditoría de `BaseModel`

---

### 6. Usuario (Nuevo)

**Model (`src/models/usuario.py`):**
```python
class Usuario(Base):
    __tablename__ = "usuarios"
    id_usuario = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False, index=True)
    email = Column(String(100), unique=True, nullable=False, index=True)
    password_hash = Column(String(255), nullable=False)
    nombre = Column(String(100), nullable=False)
    rol = Column(String(20), nullable=False, default="veterinario")
```

**Nota:** Esta clase no existía en `entities`. Fue creada para:
- Gestionar autenticación y autorización
- Referenciar en columnas de auditoría
- Asociar citas y consultas a veterinarios

---

### 7. BaseModel (Nuevo)

**Model (`src/models/base.py`):**
```python
class BaseModel(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True, index=True)
    id_usuario_creacion = Column(Integer, ForeignKey("usuarios.id_usuario"), nullable=False)
    id_usuario_edita = Column(Integer, ForeignKey("usuarios.id_usuario"), nullable=True)
    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    fecha_edicion = Column(DateTime(timezone=True), onupdate=func.now(), nullable=True)
```

**Nota:** Clase abstracta que proporciona:
- Primary key genérica `id`
- Trazabilidad de creación y modificación
- Reutilizada por `Animal`, `Cita`, `Consulta`

---

## Estrategias de Herencia

### Entity → Model: Herencia de Tabla (Joined Table Inheritance)

```
┌─────────────────────────────────────────────────────────────┐
│                      ANIMALES (tabla base)                  │
│  id | nombre | edad | especie | tipo | auditoría...         │
└─────────────────────────────────────────────────────────────┘
                    ▲                         ▲
                    │                         │
        ┌───────────┴───────────┐  ┌──────────┴────────────┐
        │       PERROS          │  │        GATOS          │
        │  id (PK, FK)          │  │  id (PK, FK)          │
        └───────────────────────┘  └───────────────────────┘
```

### Entity → Model: Consolidación de Consultas

```
┌─────────────────────────────────────────────────────────────┐
│               ENTITIES (3 clases separadas)                 │
│  consulta (base)                                            │
│  ├── ConsultaRevision                                       │
│  └── ConsultaUrgencias                                      │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                  MODELS (1 tabla consolidada)               │
│  CONSULTAS                                                  │
│  tipo_consulta = 'revision' | 'urgencia'                    │
│  + campos específicos nullable                              │
└─────────────────────────────────────────────────────────────┘
```

---

## Consideraciones de Diseño

1. **Herencia polimórfica en animales**: Se eligió joined table inheritance para mantener la estructura de herencia del dominio mientras permite consultas eficientes por tipo.

2. **Consolidación de consultas**: En lugar de usar herencia polimórfica como en entities, se consolidó en una tabla con campos nullable para simplificar las migraciones y queries.

3. **Auditoría centralizada**: `BaseModel` proporciona trazabilidad uniforme sin duplicar código.

4. **FKs vs nombres**: Los models usan foreign keys numéricos en lugar de nombres de strings, siguiendo buenas prácticas de normalización.

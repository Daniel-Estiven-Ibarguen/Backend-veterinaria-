# Backend Veterinaria

Sistema de gestión para una veterinaria que permite gestionar animales y citas mediante programación orientada a objetos.

## Descripción

Este proyecto implementa un sistema de gestión para una veterinaria. Permite crear y consultar diferentes tipos de animales (gatos, perros y genéricos), y gestionar citas médicas con operaciones CRUD completas. Utiliza conceptos de Programación Orientada a Objetos (POO) para modelar la jerarquía de entidades.

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
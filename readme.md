# Backend Veterinaria

Sistema de gestión para una veterinaria que permite gestionar animales mediante programación orientada a objetos.

## 📌 Descripción

Este proyecto implementa un sistema de gestión de animales para una veterinaria, permitiendo crear y consultar diferentes tipos de animales (gatos, perros y genéricos). Utiliza conceptos de Programación Orientada a Objetos (POO) para modelar la jerarquía de animales.

## 🧩 Clases Implementadas

### Animal (Clase Base)
Clase abstracta que representa un animal genérico en la veterinaria.

- **Atributos privados**: `__nombre`, `__edad`, `__especie`
- **Propiedades**: `nombre`, `edad` (solo lectura)
- **Métodos**:
  - `emitir_sonido()`: Retorna el sonido del animal
  - `__str__()`: Representación en cadena del animal

### Gato (Hereda de Animal)
Clase especializada que representa un gato.

- **Especialización**: Override del método `emitir_sonido()` → retorna "Miau"

### Perro (Hereda de Animal)
Clase especializada que representa un perro.

- **Especialización**: Override del método `emitir_sonido()` → retorna "Guau"
- **Método adicional**: `cavar()` → método específico del perro

## 🛠️ Técnicas de POO Aplicadas

| Técnica | Descripción |
|---------|-------------|
| **Herencia** | `Gato` y `Perro` heredan de `Animal` |
| **Polimorfismo** | Override del método `emitir_sonido()` en subclases |
| **Encapsulamiento** | Atributos privados con `@property` para acceso controlado |
| **Abstracción** | Clase `Animal` como base abstracta del dominio |

## 📂 Estructura del Proyecto

```
Backend-veterinaria-/
├── main.py                 # Punto de entrada con menú interactivo
├── readme.md               # Documentación del proyecto
└── src/
    └── entities/
        ├── animal.py       # Clase base Animal
        ├── gato.py         # Clase Gato
        └── perro.py        # Clase Perro
```

## 🚀 Uso del Menú

Ejecutar `python main.py` y seleccionar una opción:

1. **Crear gato** - Registrar un nuevo gato
2. **Crear perro** - Registrar un nuevo perro
3. **Crear animal genérico** - Registrar cualquier animal
4. **Consultar animales** - Ver todos los animales registrados
5. **Salir** - Finalizar el programa

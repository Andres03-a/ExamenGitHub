# PhotoCampus - Gestión de Servicios Fotográficos

## Descripción

PhotoCampus es una aplicación en Python que permite gestionar servicios fotográficos desde la consola.
El sistema permite registrar, editar y eliminar servicios, guardando la información en un archivo JSON.

---

## Funcionalidades

* Registrar servicios fotográficos
* Editar servicios existentes
* Eliminar servicios
* Almacenamiento persistente en archivo JSON

---

## Estructura del proyecto

```
EXAMENGITHUB/
│
├── main.py
├── registrar.py
├── edit.py
├── delete.py
├── data.py
├── servicios.json (se crea automáticamente)
└── README.md
```

---

## Requisitos

* Python 3.x instalado

---

## Cómo ejecutar el proyecto

1. Clonar el repositorio:

```
git clone <URL_DEL_REPOSITORIO>
```

2. Entrar a la carpeta del proyecto:

```
cd EXAMENGITHUB
```

3. Ejecutar el programa:

```
python main.py
```

---

## Sobre el archivo `servicios.json`

* Este archivo se crea automáticamente al usar el programa.
* No es necesario configurarlo manualmente.
* Se guarda en la misma carpeta del proyecto.

### Importante

No es necesario modificar rutas del sistema.
El programa funciona en cualquier computadora siempre que se ejecute dentro de la carpeta del proyecto.

---

## Notas

* El sistema valida entradas para evitar errores (números inválidos, campos vacíos, etc.).
* Si no hay servicios registrados, el programa lo indicará automáticamente.
* Se recomienda no modificar manualmente el archivo `servicios.json`.

---

## Autor

Proyecto desarrollado como práctica de gestión de versiones con Git y GitHub.

from data import *

def editar_servicio():
    servicios = cargar_servicios()

    if not servicios:
        print("No hay servicios registrados.\n")
        return

    print("=== Lista de Servicios ===")
    for i, s in enumerate(servicios):
        print(f"{i + 1}. {s['nombre']} - {s['tipo_evento']} - ${s['precio']}")

    try:
        opcion = int(input("Seleccione el número del servicio a editar: ")) - 1
        if opcion < 0 or opcion >= len(servicios):
            print("Opción inválida.\n")
            return
    except ValueError:
        print("Debe ingresar un número.\n")
        return

    servicio = servicios[opcion]

    print("\n--- Editando servicio ---")

    nuevo_nombre = input(f"Nombre ({servicio['nombre']}): ") or servicio['nombre']
    
    try:
        nuevo_precio = input(f"Precio ({servicio['precio']}): ")
        nuevo_precio = float(nuevo_precio) if nuevo_precio else servicio['precio']
    except ValueError:
        print("Precio inválido.\n")
        return

    nuevo_tipo = input(f"Tipo evento ({servicio['tipo_evento']}): ") or servicio['tipo_evento']

    try:
        nueva_duracion = input(f"Duración ({servicio['duracion']}): ")
        nueva_duracion = float(nueva_duracion) if nueva_duracion else servicio['duracion']
    except ValueError:
        print("Duración inválida.\n")
        return

    servicios[opcion] = {
        "nombre": nuevo_nombre,
        "precio": nuevo_precio,
        "tipo_evento": nuevo_tipo,
        "duracion": nueva_duracion
    }

    guardar_servicios(servicios)

    print("✔ Servicio editado correctamente.\n")
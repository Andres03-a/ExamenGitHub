from data import *

def eliminar_servicio():
    servicios = cargar_servicios()

    if not servicios:
        print("No hay servicios para eliminar.\n")
        return

    print("=== Lista de Servicios ===")
    for i, s in enumerate(servicios):
        print(f"{i + 1}. {s['nombre']} - {s['tipo_evento']}")

    try:
        opcion = int(input("Seleccione el número del servicio a eliminar: ")) - 1
        if opcion < 0 or opcion >= len(servicios):
            print("Opción inválida.\n")
            return
    except ValueError:
        print("Debe ingresar un número.\n")
        return

    confirmacion = input("¿Seguro que quieres eliminar este servicio? (Si/No): ").strip().lower()

    if confirmacion == "si":
        eliminado = servicios.pop(opcion)
        guardar_servicios(servicios)
        print(f"Servicio '{eliminado['nombre']}' eliminado.\n")
    else:
        print("Operación cancelada.\n")
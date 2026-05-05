from data import *

def registrar():
    print("=== Registro de Servicios ===")

    nombre = input("Nombre del paquete fotográfico: ").strip()
    if not nombre:
        print("Error: El nombre no puede estar vacío.\n")
        return

    try:
        precio = float(input("Precio del servicio: "))
        if precio < 0:
            print("Error: El precio no puede ser negativo.\n")
            return
    except ValueError:
        print("Error: El precio debe ser un número.\n")
        return

    tipo_evento = input("Tipo de evento (boda, retrato, producto, etc.): ").strip()
    if not tipo_evento:
        print("Error: El tipo de evento no puede estar vacío.\n")
        return

    try:
        duracion = float(input("Duración estimada (en horas): "))
        if duracion < 0:
            print("Error: La duración no puede ser negativa.\n")
            return
    except ValueError:
        print("Error: La duración debe ser un número.\n")
        return

    servicios = cargar_servicios()

    nuevo_servicio = {
        "nombre": nombre,
        "precio": precio,
        "tipo_evento": tipo_evento,
        "duracion": duracion
    }

    servicios.append(nuevo_servicio)

    guardar_servicios(servicios)

    print("✔ Servicio registrado correctamente.\n")
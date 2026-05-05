from registrar import registrar
from edit import editar_servicio
from delete import eliminar_servicio

while True:
    print("====================================================")
    print("  Bienvenido PhotoCampus Fotografia profesional")
    print("====================================================")
    print("1. Registrar servicios")
    print("2. Editar servicios")
    print("3. Eliminar servicios")
    print("4. Salir")

    opcion = input("Digite una opción: ").strip()
    print()

    if opcion == "1":
        registrar()

    elif opcion == "2":
        editar_servicio()

    elif opcion == "3":
        eliminar_servicio()

    elif opcion == "4":
        salir = input("¿Quieres salir del programa (Si/No): ").strip().lower()
        if salir == "si":
            print("Saliste del programa...\n")
            break
        elif salir == "no":
            print()
            continue
        else:
            print("Opción inválida.\n")

    else:
        print("Error: No existe la opción.\n")

    input("Presiona Enter para continuar...")
    print()
import json
import os

ARCHIVO = "servicios.json"

def cargar_servicios():
    if not os.path.exists(ARCHIVO):
        return []

    with open(ARCHIVO, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def guardar_servicios(servicios):
    with open(ARCHIVO, "w") as f:
        json.dump(servicios, f, indent=4)
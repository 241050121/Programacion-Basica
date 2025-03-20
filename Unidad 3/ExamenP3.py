import math
import random
import csv

def guardar_meseros_en_csv(nombre_archivo, lista_diccionarios):
    """Guarda una lista de diccionarios de meseros en un archivo CSV."""
    if not meseros:
        print("La lista de meseros está vacía.")
        return

    # Obtener las claves del primer diccionario de meseros como encabezados
    encabezados = ["Nombre", "Edad", "Rol", "Promedio"]

    with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo_csv:
        escritor = csv.DictWriter(archivo_csv, fieldnames=encabezados)
        escritor.writeheader()
        for nombre, detalles in meseros.items():
            fila = {"Nombre": nombre, "Edad": detalles["Edad"], "Rol": detalles["Rol"], "Promedio": detalles["Promedio"]}
        escritor.writerow(fila)  

    print(f"Datos guardados en {nombre_archivo} exitosamente.")

def leer_meseros_de_csv(nombre_archivo):
    """Lee un archivo CSV y lo convierte en una lista de diccionario de meseros."""
    meseros = {}
    try:
        with open(nombre_archivo, mode='r', encoding='utf-8') as archivo_csv:
            lector = csv.DictReader(archivo_csv)
            for fila in lector:
                meseros[fila["Nombre"]]= {
                    "Edad": fila["Edad"],
                    "Rol": fila["Rol"],
                    "Promedio": fila["Promedio"],
                }
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no existe.")
    return meseros

archivo = "ExamenP3.csv"

if __name__ == "__main__":
    meseros = {
        "Jose": {"Edad": "18", "Rol": "Capitan", "Promedio": 10.0},
        "Juan": {"Edad": "19", "Rol": "Barra", "Promedio": 9.4},
    }

    meseros_disponibles = {
        "Oswaldo": {"Edad": "24", "Rol": "Charolero", "Promedio": 80.0},
        "Roberto": {"Edad": "17", "Rol": "Charolero", "Promedio": 9.5},
        "Manuel": {"Edad": "18", "Rol": "Cocina", "Promedio": 8.7},
        "Ernesto": {"Edad": "27", "Rol": "Capitan", "Promedio": 10.0},
        "Jesus": {"Edad": "30", "Rol": "Cocina", "Promedio": 8.1},
    }

# Guardar los diccionarios en un archivo CSV
guardar_meseros_en_csv(archivo, meseros)

# Leer los diccionarios desde el archivo CSV
datos_leidos = leer_meseros_de_csv(archivo)
print("Datos leídos del archivo CSV:")
print(datos_leidos)

while True:
    print(" MENÚ ")
    print("1. Agregar mesero")
    print("2. Imprimir meseros")
    print("3. Eliminar mesero")
    print("4. Mostrar promedio de meseros")
    print("5. Seleccionar mesero aleatorio")
    print("6. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        print("Meseros disponibles para agregar:")
        for nombre, detalles in meseros_disponibles.items():
            print(f"{nombre}: {detalles}")

        nombre = input("Ingrese el nombre del mesero a agregar: ")
        if nombre in meseros_disponibles:
            meseros[nombre] = meseros_disponibles[nombre]
            del meseros_disponibles[nombre]
            print(f"Mesero '{nombre}' agregado.")
        else:
            print("❌ Mesero no disponible.")

    elif opcion == "2":
        print("Diccionario de meseros:")
        for nombre, detalles in meseros.items():
            print(f"{nombre}: {detalles}")

    elif opcion == "3":
        nombre = input("Ingrese el nombre del mesero a eliminar: ")
        if nombre in meseros:
            del meseros[nombre]
            print(f"Mesero '{nombre}' eliminado.")
        else:
            print("❌ Mesero no encontrado.")

    elif opcion == "4":
        if meseros:
            promedios = [detalles["Promedio"] for detalles in meseros.values()]
            promedio_total = sum(promedios) / len(promedios)
            print(f"Promedio total de los meseros: {math.ceil(promedio_total)}")
        else:
            print("❌ No hay meseros para calcular el promedio.")

    elif opcion == "5":
        if meseros_disponibles:
            mesero_aleatorio = random.choice(list(meseros_disponibles.keys()))
            print(f"Mesero aleatorio seleccionado: {mesero_aleatorio}")
        else:
            print("❌ No hay meseros disponibles para seleccionar.")

    elif opcion == "6":
        print("👋 Saliendo del programa. ¡Hasta luego!")
        break

    else:
        print("❌ Opción inválida. Intenta de nuevo.")
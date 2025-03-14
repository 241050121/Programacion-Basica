# Diccionario numero 3
profesores = {
    "Flores": {"Materia": "Programacion basica", "Promedio":7.9},
    "La risitas": {"Materia": "Calculo integral","promedio": 9.4},
    "La gallos": {"Materia": "Administracion", "Promedio": 100},
    "Finish class": {"Materia": "Ingles", "Promedio": 8.6},
    "El presumido": {"Materia": "Ing Materiales", "Promedio": 9.1},
    "El ASMR": {"Materia": "Algebra Lineal", "Promedio": 0},
    "Abuelo de Mamel": {"Materia": "Estadistica", "Promedio": 9.0},
}
alumnos= {
    "Aaron":18,
    "Oswaldo":18,
    "Roberto":18,
    "Adan":18,
    "Manuel":18,
    "Alejandro":18,
    "Cristian":18,
    "Juan":18,
    "Karol":18,
    "Guadalupe":18,
    "Jesus":19,
}
# Imprimir el diccionario completo
print("Diccionario de profesores:")
for nombre, detalles in profesores.items():
    print(f"{nombre}: {detalles}")

# Acceder a los valores de un estudiante específico
nombre_profesor = "Flores"
if nombre_profesor in profesores:
    detalles = profesores[nombre_profesor]
    print(f"\nDetalles de {nombre_profesor}:")
    print(f"Materia: {detalles['Materia']}")
    print(f"Promedio: {detalles['Promedio']}")


# Acceder a un valor usando una clave
print("Edad de Juan:", alumnos["Juan"])


# Iterar sobre un diccionario
print("Iterar sobre el diccionario:")
for nombre, edad in alumnos.items():
    print(f"{nombre} tiene {edad} años")


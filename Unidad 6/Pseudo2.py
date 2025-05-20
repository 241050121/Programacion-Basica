# Solicitar texto al usuario
texto = input("Introduce un texto que desea analizar: ")

# Inicializar contadores
contador_vocales = 0
contador_consonantes = 0
contador_numeros = 0
contador_otros = 0

# Definir conjuntos de caracteres
vocales = "aeiou"
consonantes = "bcdfghjklmnpqrstvwxyz"

# Recorrer el texto y analizar cada carácter
for caracter in texto.lower():
    if caracter in vocales:
        contador_vocales += 1
    elif caracter in consonantes:
        contador_consonantes += 1
    elif caracter.isdigit():
        contador_numeros += 1
    else:
        contador_otros += 1

# Mostrar resultados
print(f"Vocales: {contador_vocales}")
print(f"Consonantes: {contador_consonantes}")
print(f"Números: {contador_numeros}")
print(f"Otros caracteres: {contador_otros}")
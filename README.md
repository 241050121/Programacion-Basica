# Programacion Basica
## Jose Enrique Lara Martinez
### Unidad 2
1. ¿Que es un lenguaje de programacion?
2. ¿Que tipo de clasificaciones de software hay?
3. ¿Que es un algoritmo?
4. ¿Que es un paradigma de programacion?
5. ¿Cual es la diferencia entre un lenguaje de programacion copilado e interpretado? 
6. ¿Que es un lenguaje de alto nivel y bajo nivel?

**Operadores**
If
"if opcion == "1":
    tarea = input("📝 Escribe la nueva tarea: ")
    tareas.append(tarea)
    print(f"✅ Tarea '{tarea}' agregada.")"
Else
"else:
    print("\n📌 Lista de Tareas:")
    for i, tarea in enumerate(tareas, 1):
        print(f"{i}. {tarea}")"
Elseif
"elif opcion == "3":
    if not tareas:
        print("📭 No hay tareas para completar.")"
While
"while True:
    print("\n📋 MENÚ DE TAREAS 📋")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")"
For
"print("\n📌 Tu lista de compras es:")
for producto in lista_compras:
    print(f"- {producto}")"
Librerias
"import math
print(math.sqrt(25))"

Tipos de datos:
"entero = 5
flotante = 1.2
cadena = "Ed Flores"
booleano = True

print("Imprime los tipos de datos")
print("Entero = " , entero)
print("Cadena = ", cadena)
print("flotante =" , flotante)
print("Booleano =", booleano)"

Switch(programacion)
"def switch_example(option):
    switcher = {
        1: "Option 1 selected",
        2: "Option 2 selected",
        3: "Option 3 selected",
    }
    return switcher.get(option, "Invalid option")

Example usage
option = int(input("Enter an option (1-3): "))
print(switch_example(option))"

### Unidad 3
1. Listas
"Lista de números
numeros = [1, 2, 3, 4, 5]"

"Lista de cadenas
nombres = ["Ana", "Luis", "Pedro"]
nombres.remove("Ana")"

"Lista con diferentes tipos de datos
mixta = [10, "Python", True, 3.14]"

2. Diccionarios
" "
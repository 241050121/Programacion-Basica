# Programacion Basica
## Jose Enrique Lara Martinez
### Unidad 2
1. ¿Que es un lenguaje de programacion?
Los tipos de software se pueden clasificar en tres grandes grupos según sus intenciones:
Sistema: conjunto de componentes que trabajan juntos para realizar una tarea.
Aplicación: software diseñado para realizar una tarea.
Desarrollo: proceso de crear, diseñar y implementar.

2. ¿Que tipo de clasificaciones de software hay?
El algoritmo es la secuencia de instrucciones mediante la cual podemos resolver un problema o cuestión.

3. ¿Que es un algoritmo?
Lenguaje informático que se utiliza para crear otros programas siguiendo un lenguaje formal y una sintaxis específica. Es un lenguaje humano que se traduce a un lenguaje máquina.

4. ¿Que es un paradigma de programacion?
Es una representación visual de los pasos o procesos que un programa o algoritmo seguirá para realizar una tarea específica. Este diagrama utiliza símbolos estándar conectados por flechas para ilustrar el flujo del programa de manera secuencial y clara.

5. ¿Cual es la diferencia entre un lenguaje de programacion copilado e interpretado? 
La principal diferencia entre un compilador y un intérprete radica en cómo procesan y ejecutan el código. Un compilador convierte todo el código fuente en un programa ejecutable independiente, mientras que un intérprete procesa y ejecuta el código línea por línea en tiempo real.

6. ¿Que es un lenguaje de alto nivel y bajo nivel?
Los lenguajes de programación se dividen en dos tipos: alto nivel y bajo nivel. Los lenguajes de bajo nivel son los que están más cerca de la computadora, mientras que los de alto nivel están más lejos. Los lenguajes de alto nivel son más fáciles de leer y escribir para los humanos, mientras que los lenguajes de bajo nivel se dirigen más directamente a la computadora.

**Operadores**
1. If
"if opcion == "1":
    tarea = input("📝 Escribe la nueva tarea: ")
    tareas.append(tarea)
    print(f"✅ Tarea '{tarea}' agregada.")".
2. Else
"else:
    print("\n📌 Lista de Tareas:")
    for i, tarea in enumerate(tareas, 1):
        print(f"{i}. {tarea}")".
3. Elseif
"elif opcion == "3":
    if not tareas:
        print("📭 No hay tareas para completar.")".
4. While
"while True:
    print("\n📋 MENÚ DE TAREAS 📋")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")".
5. For
"print("\n📌 Tu lista de compras es:")
for producto in lista_compras:
    print(f"- {producto}")".
6. Librerias
"import math
print(math.sqrt(25))".

7. Tipos de datos:
"entero = 5
flotante = 1.2
cadena = "Ed Flores"
booleano = True

print("Imprime los tipos de datos")
print("Entero = " , entero)
print("Cadena = ", cadena)
print("flotante =" , flotante)
print("Booleano =", booleano)".

8. Switch(programacion)
"def switch_example(option):
    switcher = {
        1: "Option 1 selected",
        2: "Option 2 selected",
        3: "Option 3 selected",
    }
    return switcher.get(option, "Invalid option")

Example usage
option = int(input("Enter an option (1-3): "))
print(switch_example(option))".

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
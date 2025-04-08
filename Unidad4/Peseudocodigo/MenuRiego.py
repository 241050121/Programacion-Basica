import random

def menu_riego():
    while True:
        print("MENÚ")
        print("1. Medir humedad")
        print("2. Salir")
        opcion = int(input("Elige una opción: "))
        
        if opcion == 1:
            humedad = random.uniform(10, 100)  # Genera un número aleatorio entre 10 y 100
            print(f"Humedad actual: {humedad:.2f}%")
            if humedad < 40:
                print("Humedad baja. Activando riego...")
            else:
                print("Humedad suficiente. No se activa riego.")
        
        elif opcion == 2 :
            print("👋 Saliendo del programa. ¡Hasta luego!")
            break
    
    print("Fin del programa.")

# Llamar a la función para ejecutar el menú
menu_riego() 
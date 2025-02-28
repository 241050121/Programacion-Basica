
# Solicitar al usuario ingresar un número
numero = int(input("Ingresa el número de creditos obtenidos: ")) 

# Verificar si tiene los creditos academicos necesarios 
if numero >= 80 <= 119 :
    print("Puedes hacer servicio social.")
else:
    print("No puedes hacer servicio social.") 
if numero >= 120 :
    print("Puedes hacer recidencia profecional.")
else:
    print("No puedes hacer recidencia profecional.")
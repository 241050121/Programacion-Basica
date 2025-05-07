def inicializar_estado():
    estado = {
        "estado": "cerrado",  
        "temperatura_estandar": 22, 
        "detecta_temperatura": 0,  
        "numero_de_personas": 0,
    }
    return estado

def abrir(estado):
    estado['estado'] = "abierto"
    print("Persianas abiertas")
    return estado

def cerrar(estado):
    estado['estado'] = "cerrado"
    print("Persianas cerradas")
    return estado

def mostrar_temperatura(estado):
    print("Temperatura actual:", estado['detecta_temperatura'])

def recibir_datos(estado, temperatura, personas):
    estado['detecta_temperatura'] = temperatura
    estado['numero_de_personas'] = personas
    print("Datos recibidos del sensor")
    return estado

def comparar_datos(estado):
    if estado['detecta_temperatura'] > estado['temperatura_estandar']:
        print("Temperatura alta, cerrando persianas")
        estado = cerrar(estado)
    else:
        print("Temperatura baja, abriendo persianas")
        estado = abrir(estado)
    return estado

def confort_humano(estado):
    if estado['numero_de_personas'] > 0:
        print("Confort humano activado")
    else:
        print("No hay personas en la habitación")
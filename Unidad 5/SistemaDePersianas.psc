Algoritmo SistemaDePersianas
    Definir conexiones Como Entero
    Definir estado Como Cadena
    Definir temperaturaEstandar Como Real
    Definir numeroDePersonas Como Entero
    Definir detectaTemperatura Como Real
	
    estado = "cerrado" 
    temperaturaEstandar = 22.0
	
    SubProceso Abrir
        estado = "abierto"
        Escribir "Persianas abiertas"
FinSubProceso

SubProceso Cerrar
	estado = "cerrado"
	Escribir "Persianas cerradas"
FinSubProceso

SubProceso MostrarTemperatura
	Escribir "Temperatura actual: ", detectaTemperatura
FinSubProceso

SubProceso RecibirDatos
	Escribir "Datos recibidos del sensor"
FinSubProceso

SubProceso CompararDatos
	Si detectaTemperatura > temperaturaEstandar Entonces
		Escribir "Temperatura alta, cerrando persianas"
		Cerrar 
	Sino
		Escribir "Temperatura baja, abriendo persianas"
		Abrir 
	FinSi
FinSubProceso

SubProceso ConfortHumano
	Si numeroDePersonas > 0 Entonces
		Escribir "Confort humano activado"
	Sino
		Escribir "No hay personas en la habitación"
	FinSi

FinAlgoritmo 
FinSubProceso
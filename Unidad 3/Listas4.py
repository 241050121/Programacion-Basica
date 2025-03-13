# Lista de cadenas
nombres = ["Aaron", "Oswaldo", "Roberto", "Adan", "Manuel","Alejandro", "Cristian", "Juan", "Karol","Guadalupe", "Jesus"]

# Lista de números
edades = [18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18]

#Razones para jugar Videojuegos
razon = ["Te diviertes","Te desestresas","Pasas el tiempo","Convives con amigos","Realizan un hobbie","Haces enojar a gente random","Descargas tu estres en el juego","Peleas con gente","Mejores tus habilidades","Pasas el tiempo"]

# Lista de cadenas
materias = ["Programacion basica","Calculo integral","Administracion de empresas","Ingles","Ing de los materiales","Algebra lineal","Contabilidad"]

# Lista de cadenas
profesores = ["Flores","La risitas","La gallos","Finish class","El presumido","El ASMR", "Abuelo de Manuel"]

# Imprimir listas 
materias.remove("Calculo integral")
print(materias)
materias.insert(1,"Programacion Avanzada")
print(materias)
for materia in materias:
    print(materia) 
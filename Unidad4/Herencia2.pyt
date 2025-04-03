class Juego:
    def __init__(self, nombre, interactividad):
        self.nombre = nombre
        self.interactividad = interactividad

    def presentarse(self):
        return f"Bienvenido al centro de {self.nombre} donde tendras una grata {self.interactividad}."

# Clase derivada o hija
class FreeFire(Juego):
    def __init__(self, nombre, interactividad, duracion ):
        super().__init__(nombre, interactividad)  # Llamada al constructor de la clase padre
        self.duracion = duracion

    def presentarse(self):
        # Sobrescribimos el método de la clase padre
        return f"Bienvenido al juego {self.nombre} donde tendras una grata {self.interactividad} y partidas de larga {self.duracion}."

# Otra clase derivada
class Fifa(Juego):
    def __init__(self, nombre, interactividad, rejugabilidad):
        super().__init__(nombre, interactividad)
        self.rejugabilidad = rejugabilidad

    def presentarse(self):
        return f"Bienvenido al juego {self.nombre} donde tendras una grata {self.interactividad} y una grandiosa {self.rejugabilidad}."

# Programa principal
if __name__ == "__main__":
    juego = Juego("Juegos", "interactividad")
    freefire = FreeFire("FreeFire", "interactividad", "duracion")
    fifa= Fifa("Fifa", "interactividad", "rejugabilidad")

    print(juego.presentarse())
    print(freefire.presentarse())
    print(fifa.presentarse())
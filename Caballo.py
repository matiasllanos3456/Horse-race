import random
class Caballo:
    # porcentaje = Porcentaje de apuestas
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.porcentaje = 0.0
        # En que posicion quedó en cada carrera
        self.posiciones = []
        self.puntaje = 10
        self.avanzar = 0
        
    def __str__(self):
        return f"Caballo: Nombre={self.nombre}\nEdad={self.edad}\nPorcentajeDeApuestas={self.porcentaje}\nPosicion={self.posicion}\nPuntaje={self.puntaje}"
    
    def getNombre(self):
        return self.nombre
    
    def getPorcentaje(self):
        return self.porcentaje
    
    def setPorcentaje(self, porcentaje=float):
        # A la hora de cambiar el porcentaje se tomará en cuenta en puntaje del caballo
        try:
            self.porcentaje = porcentaje
        except ValueError:
            print("Valor invalido")
            
    def setPuntaje(self, puntaje=int):
        try:
            self.puntaje += puntaje
        except ValueError:
            print("Valor invalido")
    # El metodo Avanzar va a generar un numero aleatorio
    # dependiendo de ese valor se calcularan las posiciones
    # en las carreras
    def Avanzar(self):
        # Mientras mas puntaje tenga el caballo, podra
        # generar un numero mas alto
        num = random.randint(1, self.puntaje)
        self.avanzar = num
        return num
    
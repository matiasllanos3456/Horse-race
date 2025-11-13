
class Caballo:
    # porcentaje = Porcentaje de apuestas
    def __init__(self, nombre, edad, posicion, puntaje):
        self.nombre = nombre
        self.edad = edad
        self.porcentaje = 0.0
        self.posicion = posicion
        self.puntaje = puntaje
    def __str__(self):
        return f"Caballo: nombre={self.nombre}\nedad={self.edad}\nporcentajeDeApuestas={self.porcentaje}\nposicion={self.posicion}\npuntaje={self.puntaje}"
    
    def getNombre(self):
        return self.nombre
    
    def getPorcentaje(self):
        return self.porcentaje
    def setPorcentaje(self, porcentaje=float):
        try:
            self.porcentaje = porcentaje
        except ValueError:
            print("Valor invalido")
    # El metodo Avanzar va a generar un numero aleatorio
    # dependiendo de ese valor se calcularan las posiciones
    # en las carreras
    def Avanzar(self):
        pass
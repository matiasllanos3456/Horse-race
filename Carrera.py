from Caballo import Caballo
class Carrera:
    
    def __init__(self, fecha):
        self.fecha = fecha
        self.ganador = ""
        # Lista de caballos que participaran en la carrera
        self.caballos = []
        
    def __str__(self):
        return f"Carrera: {self.fecha}\nParticipantes: {self.caballos}"
    
    # ganador = Objeto de tipo caballo
    def setGanador(self, ganador=Caballo):
        if(ganador in self.caballos):
            self.ganador = ganador.getNombre()
        else:
            print("El caballo no está registrado")
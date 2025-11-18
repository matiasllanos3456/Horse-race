from Caballo import Caballo
class Carrera:
    
    def __init__(self, fecha):
        self.fecha = fecha
        self.ganador = Caballo
        # Lista de caballos que participaran en la carrera
        self.caballos = []
        self.posiciones = []
        
    def __str__(self):
        return f"Carrera: {self.fecha}\nParticipantes: {self.caballos}"
    
    def AgregarCaballo(self, caballo=Caballo):
        if caballo:
            self.caballos.append(caballo)
        else:
            print("No se pudo guardar al caballo")
            
    def AgregarVariosCaballos(self, listaC):
        # listaC = Lista con varios caballos
        # Fusionar 2 listas
        self.caballos.extend(listaC)
        
    def ListarCaballos(self):
        if self.caballos:
            for i in self.caballos:
                # Se llamará implicitamente al metodo __str__
                print(i)       
        else:
            print("No hay caballos compitiendo")

    # ganador = Objeto de tipo caballo
    def setGanador(self, ganador=Caballo):
        if(ganador in self.caballos):
            self.ganador = ganador.getNombre()
        else:
            print("El caballo no está registrado")
            
    def IniciarCarrera(self):
        if(len(self.caballos) > 2):
            # Se guardará el puntaje de cada caballo en orden
            puntajes = []
            # i = caballo
            for i in self.caballos:
                puntajes.append(i.Avanzar())
            maximo = puntajes.index(max(puntajes))
            caballo_ganador = self.caballos[maximo]
            self.ganador = caballo_ganador
            print(f"Ganador: {caballo_ganador.getNombre()}")
            return puntajes
        else:
            print("Debe haber almenos 2 caballos")
    
    # Ordenar las posiciones finales (una vez finalizada la carrera)
    def Ordenar(self):
        # Se modificará la lista de posiciones
        if(len(self.caballos) > 2):
            # Se ordenan segun el atributo avanzar de mayor a menor
            self.posiciones = sorted(self.caballos, key=lambda caballo : caballo.avanzar, reverse=True)
        else:
            print("No hay suficientes caballos")
        
    # Una vez finalizada la carrera se deben aumentar los puntajes de los caballos según la posicion en la que quedaron
    def setPuntajes(self, puntos=list):
        # ejemplo: puntos = [2,4,9,3,8,5]
        try:
            for i in range(len(puntos)):
                self.caballos[i].setPuntaje(puntos[i])
        except (IndexError):
            print("Los indices no coinciden")
            raise IndexError
        
            
    # Una vez finalizada la carrera se anotan los resultados en el archivo "RegistroCarreras.txt"
    def Registrar(self):
        try:
            with open("RegistroCarreras.txt", "w") as file:
                # Anotan las posiciones
                file.write(f"Fecha: {self.fecha}\nPosiciones: {self.posiciones}\nGanador: {self.ganador}")
        except FileNotFoundError:
            print("El archivo no se pudo encontrar")
    
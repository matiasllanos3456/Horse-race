from Caballo import Caballo
class Carrera:
    
    def __init__(self, fecha):
        self.fecha = fecha
        self.ganador = ""
        # Lista de caballos que participaran en la carrera
        self.caballos = []
        
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
            
    # Una vez finalizada la carrera se anotan los resultados en el archivo "RegistroCarreras.txt"
    
    
    # ganador = Objeto de tipo caballo
    def setGanador(self, ganador=Caballo):
        if(ganador in self.caballos):
            self.ganador = ganador.getNombre()
        else:
            print("El caballo no está registrado")
            
    # Se llamara a la funcion de setPorcentajes()
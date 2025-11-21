from Caballo import Caballo
from Usuario import Usuario
class Carrera:
    
    def __init__(self, fecha=str):
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
    
    def getCaballos(self):
        return self.caballos
            
    def AgregarVariosCaballos(self, listaC):
        # listaC = Lista con varios caballos
        # Fusionar 2 listas
        self.caballos.extend(listaC)
        
    def ListarCaballos(self):
        if self.caballos:
            for i in self.caballos:
                # Se llamará implicitamente al metodo __str__
                print(i)   
                print("----------------")    
        else:
            print("No hay caballos compitiendo")

    # ganador = Objeto de tipo caballo
    def setGanador(self, ganador=Caballo):
        if(ganador in self.caballos):
            self.ganador = ganador.getNombre()
        else:
            print("El caballo no está registrado")
            
    # Modificar los porcetajes de apuesta de cada caballo antes de empezar la carrera
    def SetPorcentajes(self):
        # Porcentaje = Puntaje / sumPuntajes
        try:
            SumPorcentajes = sum(caballo.getPuntaje() for caballo in self.caballos)
            for i in self.caballos:
                i.setPorcentaje(SumPorcentajes)
        except TypeError:
            print("Error de tipo")
            
    def IniciarCarrera(self, user=Usuario):
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
            
            # Se deben anotar las ganancias o perdidas en el archivo de transacciones
            if(self.ganador == user.GetCaballo()):
                # Dar dinero
                ganancias = user.GetDineroApostado * caballo_ganador.getPorcentaje()
                print(f"Ha ganado: {ganancias}")
                # Se anotan las ganancias
                user.SetRegistro(f"{self.fecha} | {ganancias} | Saldo: {user.GetDinero()}")
                user.SetDinero(ganancias)
            else:
                # Se registra la perdida de dinero
                print("El caballo apostado no ganó")
                user.SetRegistro(f"{self.fecha} | {-1*(user.GetDineroApostado)} | Saldo: {user.GetDinero()}")
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
                file.write(f"Fecha: {self.fecha} | Ganador: {self.ganador}\nPosiciones: {self.posiciones}")
        except FileNotFoundError:
            print("El archivo no se pudo encontrar")
    
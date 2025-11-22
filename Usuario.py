from Caballo import Caballo
class Usuario:
    
    def __init__(self, nombre=str, dinero=int):
        self.nombre = nombre
        self.dinero = dinero
        self.dineroApostado = 0
        # caballoApostado = Objeto de tipo caballo
        self.caballoApostado = None
    def __str__(self):
        return f"Nombre: {self.nombre}\nDinero: {self.dinero}\nDinero apostado: {self.dineroApostado}\n Caballo apostado: {self.caballoApostado}"
    
    # Modificar el registro de transacciones
    # Tendrá el formato: |Fecha: ........ | Ganancias: ......... |
    def SetRegistro(self, text=str):
        print("Registrando apuesta .................")
        try:
            with open("Transacciones.txt", "a") as file:
                file.write(text + "\n")
        except FileNotFoundError:
            print("Archivo no encontrado")
        except Exception as e:
            print(f"Ocurrio un error inesperado en {e}")
    
    # Realizar apuesta
    def Apostar(self):
        print(f"Saldo actual: {self.dinero}")
        apuesta = int(input("Cuanto dinero desea apostar?: "))
        if(0 < apuesta < self.dinero):
            self.dineroApostado = apuesta
            self.dinero -= apuesta
            print("Apuesta realizada")
        else:
            print("Monto invalido")
            raise ValueError
        
    def SetDinero(self, ganancias):
        # En el main se calcularan las ganancias, ya sean positivas o negativas
        self.dinero += ganancias
    
    def GetCaballo(self):
        return self.caballoApostado
    def GetDinero(self):
        return self.dinero
    def GetDineroApostado(self):
        return self.dineroApostado
    
    def ElegirCaballo(self, caballos):
        try:
            for i,j in enumerate(caballos): # i = indice; j = Caballo
                print(f"{i}) {j}")
                
            eleccion = int(input("Elija un caballo por su indice: "))
            print(f"Haz elegido a {caballos[eleccion].getNombre()}")
            self.caballoApostado = caballos[eleccion]
        except IndexError:
            print("Indice inexistente")
from Caballo import Caballo
class Usuario:
    
    def __init__(self, nombre=str, dinero=int):
        self.__nombre = nombre
        self.__dinero = dinero
        self.__dineroApostado = 0
        # caballoApostado = Objeto de tipo caballo
        self.__caballoApostado = None
    def __str__(self):
        return f"Nombre: {self.__nombre}\nDinero: {self.__dinero}\nDinero apostado: {self.__dineroApostado}\n Caballo apostado: {self.__caballoApostado}"
    
    def GetNombre(self):
        return self.__nombre
    
    def SetNombre(self, nombre=str):
        if not isinstance(nombre, str):
            raise ValueError("Nombre inválido")
        self.__nombre = nombre
    
    def SetDinero(self, ganancias):
        # En el main se calcularan las ganancias, ya sean positivas o negativas
        self.__dinero += ganancias*10

    # Cambiar el caballo apostado
    def SetCaballo(self, caballo):
        if caballo is not None and not isinstance(caballo, Caballo):
            raise TypeError("Debe ser un objeto Caballo o None")
        self.__caballoApostado = caballo

    def GetCaballo(self):
        return self.__caballoApostado
    def GetDinero(self):
        return round(self.__dinero)
    def GetDineroApostado(self):
        return round(self.__dineroApostado)
    
    # Modificar el registro de transacciones
    # Tendrá el formato: |Fecha: ........ | Ganancias: ......... |
    def SetRegistro(self, text=str):
        try:
            with open("Transacciones.txt", "a") as file:
                file.write(text + "\n")
        except FileNotFoundError:
            print("Archivo no encontrado")
        except Exception as e:
            print(f"Ocurrio un error inesperado en {e}")
    
    # Realizar apuesta
    def Apostar(self):
        print(f"Saldo actual: {self.__dinero}")
        apuesta = int(input("Cuanto dinero desea apostar?: "))
        if(5 <= apuesta <= self.__dinero):
            self.__dineroApostado = apuesta
            self.__dinero -= apuesta
            print("Apuesta realizada")
        else:
            print("Monto invalido")
            raise ValueError
        
    def ElegirCaballo(self, caballos):
        try:
            for i,j in enumerate(caballos): # i = indice; j = Caballo
                print(f"{i}) {j}")
                
            eleccion = int(input("Elija un caballo por su indice: "))
            print(f"Haz elegido a {caballos[eleccion].getNombre()}")
            print("------------------------------------")
            self.__caballoApostado = caballos[eleccion]
        except IndexError:
            print("Indice inexistente")
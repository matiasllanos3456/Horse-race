
class Usuario:
    
    def __init__(self, nombre=str, dinero=int):
        self.nombre = nombre
        self.dinero = dinero
        self.dineroApostado = 0
        # caballoApostado = Objeto de tipo caballo
        self.caballoApostado = None
    def __str__(self):
        return f"Nombre: {self.nombre}\nDinero: {self.dinero}\nDinero apostado: {self.dineroApostado}\n Caballo apostado: {self.caballoApostado}"
    
    # Ver registro de las transacciones
    def VerRegistro(self):
        pass
    
    # Modificar el registro
    def SetRegistro(self, text):
        pass
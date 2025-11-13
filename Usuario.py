
class Usuario:
    
    def __init__(self, nombre=str, dinero=int):
        self.nombre = nombre
        self.dinero = dinero
        self.dineroApostado = 0
        # caballoApostado = Objeto de tipo caballo
        self.caballoApostado = None
    def __str__(self):
        return f"Nombre: {self.nombre}\nDinero: {self.dinero}\nDinero apostado: {self.dineroApostado}\n Caballo apostado: {self.caballoApostado}"
    
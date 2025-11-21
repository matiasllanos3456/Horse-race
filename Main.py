from Caballo import Caballo
from Carrera import Carrera
from Usuario import Usuario

caballos = []
caballos.append(Caballo("Tormenta China", 15))
caballos.append(Caballo("Martin", 18))
caballos.append(Caballo("Cristobal", 19))
caballos.append(Caballo("Nube", 21))
caballos.append(Caballo("Tornado", 13))
caballos.append(Caballo("Leon", 16))
caballos.append(Caballo("Pegaso", 19))
caballos.append(Caballo("Lucky", 23))
caballos.append(Caballo("Esmeralda", 24))
caballos.append(Caballo("Mensajero de Dios", 20))

# Se debe implementar una funcion para simular la carrera
# Una vez que se cree una carrera se abrirá un menú con 3 opciones: 1) Realizar apuesta; 2) Ver caballos; 3) Retirarse
# Se necesita una funcion para realizar la apuesta. Se podran ver los caballos a travez de un metodo de la clase "Carrera"
# Funcion mostrar posiciones
# Otra funcion debe mostrar el historial de las carreras
# Otra funcion debe mostrar el historial de transacciones del usuario
# Se accederan a los archivos de texto desde el menú
# El usuario debe poder inscribir un caballo

# Creacion del usuario
nombre = input("Ingrese su nombre: ")
user1 = Usuario(nombre, 50)


def SimularCarrera(caballos, user=Usuario):
    try:
        # Aquí se crean las carreras
        fecha = input("Ingrese la fecha en formato DD/MM/YYYY: ")
        carrera1 = Carrera(fecha)
        carrera1.AgregarVariosCaballos(caballos)
        # Cambiar los porcentajes de apuesta antes de empezar la carrera
        carrera1.SetPorcentajes()
        # Antes de iniciar la carrera se debe realizar la apuesta
        opcion1 = 0
        while(opcion1 != 3):
            print("1) Ver caballos\n2) Empezar apuesta\n3) Salir")
            opcion1 = int(input("> "))
            if(opcion1 == 1):
                carrera1.ListarCaballos()
            elif(opcion1 == 2):
                # IniciarCarrera() se utilizara aquí
                user.Apostar()
                
                user1.ElegirCaballo(caballos)
                
                puntajes = carrera1.IniciarCarrera(user)
                
                # Se ordenan las posiciones finales
                carrera1.Ordenar()
                
                # Cambiar los puntajes de los caballos al finalizar la carrera
                carrera1.setPuntajes(puntajes)
                
                break
            elif(opcion1 == 3):
                print("Saliendo...")
                break
            else:
                print("Opcion invalida")

        print("Carrera finalizada")
    except IndexError:
        pass
    except TypeError:
        pass
    except ZeroDivisionError:
        pass
    except ValueError:
        pass
    
def MostrarCarreras():
    try:
        with open("RegistroCarreras.txt", "r") as file:
            contenido = file.read()
            print(contenido)
    except FileNotFoundError:
        print("No se encontró el archivo")
        
def MostrarTransacciones():
    try:
        with open("Transacciones.txt", "r") as file:
            contenido = file.read()
            print(contenido)
    except FileNotFoundError:
        print("No se encontró el archivo")

def InscripcionCaballo(caballos):
    try:
        nombre = input("Nombre: ")
        edad = int(input("Edad: "))
        c = Caballo(nombre, edad)
        caballos.append(c)
        print("Caballo creado exitosamente")
        print(c)
    except ValueError:
        print("Valor invalido")
        
opcion = 0

while(opcion != 5):
    print("MENU:\n1) Inscribir caballo\n2) Iniciar carrera\n3) Ver historial de carreras\n4) Ver transacciones\n5) Salir")
    opcion = int(input("> "))
    if(opcion == 1):
        InscripcionCaballo(caballos)
    elif(opcion == 2):
        SimularCarrera(caballos, user1)
    elif(opcion == 3):
        print("Historial de carreras")
        MostrarCarreras()
    elif(opcion == 4):
        print("Historial de transacciones")
        MostrarTransacciones()
    elif(opcion == 5):
        print("Saliendo... ")
    else:
        print("Opcion invalida")
    

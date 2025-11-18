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
# El usuario debe poder inscribir un caballo

opcion = 0

while(opcion != 5):
    print("MENU:\n1) Inscribir caballo\n2) Iniciar carrera\n3) Ver historial de carreras\n4)Ver transacciones\n5) Salir")
    opcion = int(input("> "))
    if(opcion == 1):
        pass
    elif(opcion == 2):
        pass
    elif(opcion == 3):
        pass
    elif(opcion == 4):
        pass
    elif(opcion == 5):
        print("Saliendo... ")
    else:
        print("Opcion invalida")
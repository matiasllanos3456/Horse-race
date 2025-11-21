# Horse-race
El juego consistirá en apostar por un caballo, el cual competirá con al menos 2 caballos mas. La apuesta mínima es de $5. Cada jugador comienza $50 y puede acumular dinero infinito, luego de cada carrera el jugador puede elegir si retirarse o continuar apostando. No se puede apostar por más de un caballo a la vez. Los puntos de cada caballo aumentaran en relación a su posicion en una carrera. El juego finalizará cuando el jugador se retire o cuando se quede sin dinero para seguir apostando.

Requerimientos: 
Funcionales: 
1) Los usuarios y caballos interactúan con la clase Carrera.
2) Desde el main se debe poder acceder al historial de las transacciones.
3) El usuario podrá interactuar con el juego a través de un menú en el archivo main
4) El tiempo de juego es hasta que el usuario se quede sin dinero o hasta que          él decida retirarse.
5) El usuario debe elegir un único caballo.
6) El usuario puede ver la información de los caballos.
7) El usuario puede acceder al historial de carreras.
8) Cada carrera contará con al menos 2 caballos.
9) La apuesta mínima para participar debe ser de al menos $5.
10) Las posiciones de los caballos en las carreras debe ser aleatoria.
11) No se sabrá nada de las apuestas hasta que el tiempo termine.
12) Los caballos obtendrán puntos en función de la posición en que terminen.

No funcionales: 
1) Las transacciones y datos de los usuarios deben ser privados.
2) El juego debe ser fácil de entender.
3) El juego no debe detenerse al ingresar valores inválidos.
4) El juego debe ejecutarse de forma fluida.
5) El menú podrá manejar entradas invalidas
6) Los archivos de texto presentarán la información de forma clara y ordenada

Clases: 
Caballo(Apuesta=int; Nombre=String; Edad=int; Posicion=int; Puntaje=int); 
Carrera(Posiciones=[]; Fecha=String; Caballos= [Caballo]; Ganador = Caballo);
Usuario(Nombre=String; Dinero=int; DineroApostado=int; CaballoActual = Caballo);

Funciones externas: Empezar carrera; Inscribir caballos; Ver caballos; Ver historial de las carreras.

Archivo de texto: Puntajes.txt; Transacciones.txt

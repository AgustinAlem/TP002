# apostar par impar
# paridad = max*2
# no paridad = - min
#puntaje a ser obtenido
#se juega hasta obtener el puntaje elegido
#mostrar nombre y puntaje de cada jugador
#si tienen mismo puntaje gana el jugador con más turnos ganados
#q jugadas realizadas
#si hubo empate en el puntaje en algún turno
#puntaje promedio obtenido por cada jugador
#porcentaje de aciertos para c jugador
#si el ganador es quién tuvo mayor porcentaje de aciertos
#Si algún jugador ganó en 3 turnos seguidos

import random
jugador1 = input("Ingrese el nombre del primer jugador: ")
jugador2 = input("Ingrese el nombre del segundo jugador: ")

puntajeAlcanzar = int(input("Ingrese el puntaje a ser alcanzado: "))

puntajej1 = 0
puntajej2 = 0

while puntajeAlcanzar != puntajej1 or puntajeAlcanzar != puntajej2:

#JUGADOR 1
    opcion = int(input("Ingrese el número de la opción elegida: "))
    print("Opciones:")
    print("         1: par.")
    print("         2: impar.")

    if opcion != 1 or opcion != 2:
       print("Opción no válida")

    else:
        dado1j1 = random.randint(1,6)
        dado2j1 = random.randint(1,6)
        dado3j1 = random.randint(1,6)

        if ((dado1j1 + dado2j1 + dado3j1) % 2) == 0 and opcion == 1:
            puntajej1 += max(dado1j1, dado2j1, dado3j1) * 2

        elif((dado1j1 + dado2j1 + dado3j1) % 2) == 0 and opcion == 2:
            puntajej1 = puntajej1 - min(dado1j1, dado2j1, dado3j1)

        elif((dado1j1 + dado2j1 + dado3j1) % 2) == 1 and opcion == 2:
            puntajej1 += max(dado1j1, dado2j1, dado3j1) * 2

        elif((dado1j1 + dado2j1 + dado3j1) % 2) == 1 and opcion == 1:
            puntajej1 = puntajej1 - min(dado1j1, dado2j1, dado3j1)


#JUGADOR 2

    opcionj2 = int(input("Ingrese el número de la opción elegida: "))
    print("Opciones:")
    print("         1: par.")
    print("         2: impar.")

    if opcionj2 != 1 or opcionj2 != 2:
        print("Opción no válida")

    else:
        dado1j2 = random.randint(1, 6)
        dado2j2 = random.randint(1, 6)
        dado3j2 = random.randint(1, 6)

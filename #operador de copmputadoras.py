e1=int(input("ingrese edad 1: "))
e2=int(input("ingrese edad 2: "))
e3=int(input("ingrese edad 3: "))
e4=int(input("ingrese edad 4: "))
e5=int(input("ingrese edad 5: "))
e6=int(input("ingrese edad 6: "))
e7=int(input("ingrese edad 7: "))
e8=int(input("ingrese edad 8: "))
pre=0 #contador de edades de 4 años
kin=0 #contador de edades de 5 años
pri=0 #contador de edades de 6 años





import random
option = ("piedra or papel or tijeras: ")
res = int(1)
jugadas = ["piedra","papel","tijeras"]

while (res==1):

    jugadaU = int(input("jugador, favor ingresar jugad: [1:piedra; 2:papel; 3:tijeras]: "))
    jugada =jugadas[jugadaU - 1]
    jugadaM = jugadas[ rsndom.randit(0, 2)]

    if( (jugada == "piedra") and (jugadaM == "tijeras" ) ):
        print ""






    resultado = jugar_piedra_papel_tijera(jugador, computadora)
    print(f"Jugador elige {jugador}")
    print(f"Computadora elige {computadora}")
    print(resultado)



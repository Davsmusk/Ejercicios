
import random

def jugar_piedra_papel_tijera(jugador1, jugador2):
    opciones = ["piedra", "papel", "tijera"]

    if jugador1 == jugador2:
        return "Empate"

    if jugador1 == "piedra":
        if jugador2 == "papel":
            return "jugador2 gana"
        else:
            return "Jugador1 gana"

    if jugador1 == "papel":
        if jugador2 == "tijera":
            return "jugador2 gana"
        else:
            return "Jugador1 gana"

    if jugador1 == "tijera":
        if jugador2 == "piedra":
            return "jugador2 gana"
        else:
            return "Jugador1 gana"

def main():
    print("Bienvenido a Piedra, Papel o Tijera!")
    jugador1 = input("Elige: piedra, papel o tijera: ").lower()
    jugador2 = random.choice(["piedra", "papel", "tijera"])
    resultado = jugar_piedra_papel_tijera(jugador1, jugador2)
    print(f"Jugador1 elige {jugador1}")
    print(f"jugador2 elige {jugador2}")
    print(resultado)

if __name__ == '__main__':
    main()

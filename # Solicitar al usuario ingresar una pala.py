# Solicitar al usuario ingresar una palabra
palabra = input("Ingrese una palabra: ")

#contador de vocales
contador_a = 0
contador_e = 0
contador_i = 0
contador_o = 0
contador_u = 0

# Contar el número de veces que aparece cada vocal en la palabra
for letra in palabra:
    if letra.lower() == 'a':
        contador_a += 1
    elif letra.lower() == 'e':
        contador_e += 1
    elif letra.lower() == 'i':
        contador_i += 1
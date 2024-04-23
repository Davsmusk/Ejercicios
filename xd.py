def contar_vocales(palabra):
    # Inicializar un diccionario para almacenar el recuento de cada vocal
    recuento_vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    # Iterar sobre cada letra en la palabra
    for letra in palabra:
        # Verificar si la letra es una vocal y actualizar el contador correspondiente
        if letra.lower() in recuento_vocales:
            recuento_vocales[letra.lower()] += 1
    return recuento_vocales

# Solicitar al usuario ingresar una palabra
palabra = input("Ingrese una palabra: ")
# Obtener el recuento de cada vocal en la palabra ingresada
recuento = contar_vocales(palabra)
# Mostrar el recuento de cada vocal
for vocal, cantidad in recuento.items():
    print(f"Número de veces que aparece la vocal '{vocal}': {cantidad}")
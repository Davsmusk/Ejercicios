def calcular_billetes(cantidad):
    denominaciones = [200, 100, 50, 20, 10, 5, 1, 0.50, 0.25, 0.10, 0.05, 0.01]
    billetes = {}

    for denominacion in denominaciones:
        if cantidad >= denominacion:
            billetes[denominacion] = cantidad // denominacion
            cantidad = round(cantidad % denominacion, 2)

    return billetes

cantidad = float(input("ingrese la cantidad:"))
resultado = calcular_billetes(cantidad)

for denominacion, cantidad in resultado.items():
    print(f"Se deben dar {cantidad} billetes de {denominacion} quetzales.")
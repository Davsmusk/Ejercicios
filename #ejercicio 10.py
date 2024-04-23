#ejercicio 10
while True:
    try:
        numero1 = int(input("Ingrese el primer número entero positivo: "))
        numero2 = int(input("Ingrese el segundo número entero positivo: "))
        if numero1 > 0 and numero2 > 0:
            break
        else:
            print("Por favor, ingrese dos números enteros positivos.")
    except ValueError:
        print("Por favor, ingrese dos números enteros.")

# Realizar la división si ambos números son positivos
if numero1 > 0 and numero2 > 0:
    resultado = numero1 / numero2
    print("El resultado de la división es:", resultado)
else:
    print("No se puede realizar la división porque al menos uno de los números ingresados no es positivo.")
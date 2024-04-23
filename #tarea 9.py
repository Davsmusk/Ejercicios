#tarea 9
suma_negativo=0
indice=-1
suma_positivo=0
num_positivos=0
for a in range (6):
    num=int(input("Ingresa numero:"))
    if num<0:
        suma_negativo+=1
    elif num>0:
        num_positivos+=1
        suma_positivo+=num

promedio=suma_positivo/num_positivos

print("los numeros negativos son:",suma_negativo,"el promedio de los positivos es:", promedio)

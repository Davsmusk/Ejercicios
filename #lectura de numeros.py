#lectura de numeros
num1=int(input("ingrese un mumero"))
num2=int(input("ingrese un mumero"))
num3=int(input("ingrese un mumero"))

if num1>num2:
 numero_mayor=num1
elif num2>num3:
 numero_mayor=num2
else:
 numero_mayor=num3
 
print("el numero mayor es",numero_mayor)


if num3<num2:
 numero_menor=num1
elif num2<num1:
 numero_menor=num2
else:
 numero_menor=num3
print("el numero menor es",numero_menor)


if num1==num2:
 numero_igual=num1
elif num2==num3:
 numero_igual=num2
else:
 numero_igual=num3
print("hay numeros iguales8",numero_igual)

 
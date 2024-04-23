#tarea 6
x=0
contraseña="chunchumaru"


while x<100000:
    ing=input("ingrese contraseña:")
    if ing==contraseña:
       print("contraseña correcta.")
       break

    else  : 
        print("contraseña incorrecta intente de nuevo")
        x +=1
         

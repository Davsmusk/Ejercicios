#año bisiesto
year= int(input("ingrese año:"))
mes= int(input("ingrese un mes:"))
dia= int(input("ingrese un dia:"))

if year%4==0:
    if mes==1:
       if 1<=dia<31:
         print("fecha valida")
    if mes==2:
        if 1<=dia<30:
         print("fecha valida")
    if mes==3:
        if 1<=dia<28:
         print("fecha valida")
    if mes==4:
        if 1<=dia<30:
         print("fecha valida")
    if mes==5:
        if 1<=dia<31:
         print("fecha valida")
    if mes==6:
        if 1<=dia<30:
         print("fecha valida")
    if mes==7:
        if 1<=dia<31:
         print("fecha valida")
    if mes==8:
        if 1<=dia<31:
         print("fecha valida")
    if mes==9:
        if 1<=dia<30:
         print("fecha valida")
    if mes==10:
        if 1<=dia<31:
         print("fecha valida")
    if mes==11:
        if 1<=dia<30:
         print("fecha valida")
    if mes==12:
        if 1<=dia<31:
         print("fecha valida")


    elif year%4 !=0:
        if mes==1:
          if 1<=dia<31:
             print("fecha valida")
          if mes==2:
              if 1<=dia<28:
                print("fecha valida")
        if mes==3:
            if 1<=dia<28:
                print("fecha valida")
        if mes==4:
            if 1<=dia<30:
                    print("fecha valida")
        if mes==5:
            if 1<=dia<31:
                  print("fecha valida")
        if mes==6:
             if 1<=dia<30:
                print("fecha valida")
        if mes==7:
                if 1<=dia<31:
                    print("fecha valida")
        if mes==8:
             if 1<=dia<31:
                     print("fecha valida")
        if mes==9:
             if 1<=dia<30:
                     print("fecha valida")
             if mes==10:
                if 1<=dia<31:
                         print("fecha valida")
        if mes==11:
                if 1<=dia<30:
                      print("fecha valida")
        if mes==12:
                 if 1<=dia<31:
                  print("fecha valida")
   
else:
   print("fecha no valida")

         
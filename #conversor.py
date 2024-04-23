#conversor
med= int(input("ingrese la medida:"))
tipo= str(input("ingrese el tipo de medida:"))

def pie (med):
    metro1= med/3.281
    yarda1= med/3
    pulgada1= med*12
    cm1= med*30.48
    print("las medidas son:","de metro",metro1,"de yarda", yarda1,"de pulgada",pulgada1,"de cm",cm1,)



    return metro1

def yarda (med):
    metro2= med/1.094
    pie1= med*3
    pulgada2= med*36
    cm2= med*91.44
    print("las medidas son:","de metro",metro2,"de pie", pie1,"de pulgada",pulgada2,"de cm",cm2)
    return metro2

def metro (med):
    yarda2= med*1.094
    pie2= med*3.281
    pulgada3= med*39.37
    cm3= med*100
    print("las medidas son:","de yarda",yarda2, "de pie",pie2,"de pulgada",pulgada3,"de cm",cm3)
    return yarda2

def pulgada(med):
    yarda3= med/36
    pie3= med/12
    metro3= med/39.37
    cm4= med*2.53
    print("las medidas son:","de yarda",yarda3,"de pie", pie3,"de metro",metro3,"de cm",cm4)
    return yarda3   

def cm(med):
    yarda4= med/91.44
    pie4= med/30.48
    metro4= med/100
    pulgada4= med/2.54
    print("las medidas son:","de yarda",yarda4,"de pie", pie4,"de metro",metro4,"de pulgada",pulgada4)
    return yarda4   

if tipo=="f":
    pie(med)

if tipo=="p":
    pulgada(med)

if tipo=="y":
    yarda(med)

if tipo=="c":
    cm(med)

if tipo=="m":
    metro(med)
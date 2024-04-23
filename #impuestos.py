#impuestos
ingreso=float(input("ingrese el monto:"))
if ingreso<85528.0:
    impuesto= ingreso*0.18-556.2
else:
    impuesto= ingreso*0.32+14839.2
    print("total a pagar de impuesto es:",round(impuesto))


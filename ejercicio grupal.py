def convertir_a_romano(numero):
  
    valores = {
        1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL',
        50: 'L', 90: 'XC', 100: 'C'
    }
    resultado = ''
 
    for valor_romano, valor_numerico in sorted(valores.items(), reverse=True):
        
        while numero >= valor_romano:
            
            resultado += valor_numerico
            
            numero -= valor_romano
    return resultado
def main():
    
    numero = int(input("Ingrese un número entre 1 y 100: "))
    
    if 1 <= numero <= 100:
             
        numeral_romano = convertir_a_romano(numero)
        print(f"El número {numero} en numeral romano es: {numeral_romano}")
    else:
        print("El número ingresado está fuera del rango permitido.")
        

main()


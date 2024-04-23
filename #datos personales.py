# Solicitar al usuario que ingrese su información personal
nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
direccion = input("Ingrese su dirección: ")
telefono = input("Ingrese su teléfono: ")

# Crear un diccionario para almacenar la información personal
informacion_personal = {
    "Nombre": nombre,
    "Edad": edad,
    "Dirección": direccion,
    "Teléfono": telefono
}

print(informacion_personal)
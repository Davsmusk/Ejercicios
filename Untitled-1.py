def ingreso():
    
    x= 3
    contraseña=["davs","peps"]


    while x >0:
        ing=input("ingrese contraseña:")
        if ing in contraseña:
            print("contraseña correcta.")
            break

        else  : 
            print("contraseña incorrecta intente de nuevo")
        x -=1
    if x==0:
        print("se han agotado sus intentos, intente en otro momento")
        


class Libro:
    def __init__(self, titulo, autor, categoria):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria

libros= []

def agregar_libros():
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")
    categoria = input("Ingrese la categoría del libro: ")
    libro = Libro(titulo, autor, categoria)
    libros.append(libro)
    print("Libro agregado con éxito.")

def eliminar_libros():
    titulo = input("Ingrese el título del libro que desee eliminar: ")
    autor = input("Ingrese el autor del libro para confirmar: ")
    
    libro = Libro(titulo, autor)
    libros.remove(libro)
    print("Libro agregado con éxito.")

def buscar_libros_por_titulo():
    titulo = input("Ingrese el título del libro: ")
    
    for libro in libros:
        if libro.titulo==titulo:
            print("Libro encontrado  con éxito.")
            print("libro",libro.titulo)
            print("autor",libro.autor)
            print("categoria",libro.categoria)
            return
        print("libro no encontrado")

def buscar_libros_por_autor():
    autor = input("Ingrese el título del libro: ")
    
    for libro in libros:
        if libro.autor==autor:
            print("Libro encontrado  con éxito.")
            print("libro",libro.titulo)
            print("autor",libro.autor)
            print("categoria",libro.categoria)
            return
        print("libro no encontrado")

def buscar_libros_por_categoria():
    categoria = input("Ingrese el título del libro: ")
    
    for libro in libros:
        if libro.categoria==categoria:
            print("Libro encontrado  con éxito.")
            print("libro",libro.titulo)
            print("autor",libro.autor)
            print("categoria",libro.categoria)
            return
        print("libro no encontrado")



def mostrar_menu():
    print("1. Agregar libro")
    print("2. Buscar libro por titulo")
    print("3. Eliminar libro")
    print("4. buscar por autor")
    print("5. buscar por categoria")
    print("6. Salir")

def main():
    ingreso()
    while True:
        mostrar_menu()
        opcion= input("seleccione una opcion")
        if opcion=="1":
            agregar_libros()
        elif opcion=="2":
            buscar_libros_por_titulo()
        elif opcion =="3":
            eliminar_libros()
            
        elif opcion=="4":
            buscar_libros_por_autor()
        elif opcion=="5":
            buscar_libros_por_categoria()
        elif opcion=="6":
            print("hasta luego:")
            break
        else:
            print("opcion invalida, ingrese una opcion valida")
            
main()
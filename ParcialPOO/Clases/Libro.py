import os
from Clases.Registro import registro
class Libro:
    def __init__(self, titulo, autor, categoria):
        self.titulo = titulo
        self.autor = autor
        self.category = categoria

    def titulolibro(self):
        self.titulo = input("Ingrese el titulo del libro: ")
    
    def autorlibro(self):
        self.autor = input("Ingrese el nombre del autor del libro: ")

    def categoria(self):
        
        print("Categorias\n1. Drama\n2. Ficción\n3. Científico\n4. Infantil\n5. Idiomas")
        opcion = int(input("Seleccione una opcion: "))
        match opcion:
            case 1:
                print("Ha seleccionado Drama")
                self.category = "Drama"
            case 2:
                print("Ha seleccionado Ficción")
                self.category = "Ficción"
            case 3:
                print("Ha seleccionado Científico")
                self.category = "Científico"
            case 4:
                print("Ha seleccionado Infantil")
                self.category = "Infantil"
            case 5:
                print("Ha selecionado Idiomas")
                self.category = "Idiomas"
            case _:
                print("No es una opción valida")
            


def menuLibro():
    libro = Libro("", "", "")
    while True:
        os.system("cls")
        print("Menu Principal\n1. Titulo del libro\n2. Autor del libro\n3. Categoría del libro\n4. Guardar Libro\n5. Salir del Menu")
        opcion = int(input("Seleccione una opcion: "))
        match opcion:
            case 1:
                libro.titulolibro()
            case 2:
                libro.autorlibro()
            case 3:
                libro.categoria()
            case 4:
                registro.agregarLibro(libro)
            case 5:
                break
            case _:
                print("No es una opción valida")
        input("Presione Enter para continuar . . .")
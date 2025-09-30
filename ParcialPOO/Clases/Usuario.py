import os

class Usuario:
    def __init__(self, nombre, numerotel):
        self.nombre = nombre
        self.__numb = numerotel
    
    def registro(self):
        self.nombre = input("Ingrese su nombre: ")
        self.__numb = int(input("Ingrese su numero de telefono: "))
    
user = Usuario("", 0)
def menuUsuario():
    while True:
        os.system("cls")
        print("Menu Principal\n1. Informacion de Usuario\n2. Salir del Menu")
        opcion = int(input("Seleccione una opcion: "))
        match opcion:
            case 1:
                user.registro()
                print(user.nombre, user._Usuario__numb)
            case 2:
                break
            case _:
                print("No es una opción valida")
        input("Presione Enter para continuar . . .")
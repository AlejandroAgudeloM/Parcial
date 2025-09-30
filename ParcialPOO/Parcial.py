#Autor: Alejandro Agudelo Marentes
import os
import Clases.Usuario as User
import Clases.Libro as Libro
import Clases.Registro as Registro


def main():
    while True:
        os.system("cls")
        print(f"Hola {User.user.nombre}")
        print("Menu Principal\n1. Registrar Usuario\n2. Registrar Libro\n3. Mostrar libros registrados\n4. Cerrar Sesión")
        opcion = int(input("Seleccione una opcion: "))
        match opcion:
            case 1:
                User.menuUsuario()
            case 2:
                Libro.menuLibro()
            case 3:
                Registro.registro.mostrarLibros()
            case 4:
                break
            case _:
                print("No es una opción valida")
        input("Presione Enter para continuar . . .")

if __name__ == "__main__":
    main()
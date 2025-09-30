
class Registro:
    def __init__(self):
        self.libros = []
    
    def agregarLibro(self, libro):
        self.libros.append(libro)

    def mostrarLibros(self):
        if not self.libros:
            print("No hay libros registrados.")
        else:
            print("Libros registrados:")
            for i, libro in enumerate(self.libros, start=1):
                print(f"{i}. {libro.titulo} - {libro.autor} ({libro.category})")

# Objeto global para registrar
registro = Registro()
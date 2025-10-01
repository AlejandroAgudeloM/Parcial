# 📚 Proyecto de Registro de Libros y Usuarios

Este proyecto implementa un sistema sencillo de registro de usuarios y libros en Python, utilizando un menú interactivo en consola. El programa permite:  
- Registrar usuarios con su nombre y teléfono.  
- Registrar libros con título, autor y categoría.  
- Almacenar los libros en una lista centralizada.  
- Mostrar en cualquier momento todos los libros registrados.  

---

## ✅ Tabla de Requerimientos

| Requerimiento            | Cumplimiento |
|--------------------------|--------------|
| Registrar nuevo usuario  | ✔️ |
| Registrar nuevo libro    | ✔️ |
| Mínimo 3 categorías      | ✔️ |

---

## 📸 Capturas de Funcionamiento

- **Registro de Libro**  
  ![Registro Libro](https://i.ibb.co/WNFDgySN/image-2025-09-30-230506208.png)

- **Listado de Libros Registrados**  
  ![Listado Libros](https://i.ibb.co/TqtWM5QZ/image.png)

---

## 🏗️ Descripción de las Clases y Métodos

### `Usuario.py`
- **Clase `Usuario`**
  - `__init__(nombre, numerotel)`: Constructor con nombre y teléfono.  
  - `registro()`: Permite al usuario ingresar su información desde consola.  

- **Objeto global `user`**: Instancia única que representa al usuario actual.  
- **`menuUsuario()`**: Menú para registrar y mostrar la información del usuario.  

---

### `Libro.py`
- **Clase `Libro`**
  - `__init__(titulo, autor, categoria)`: Constructor con título, autor y categoría.  
  - `titulolibro()`: Solicita al usuario el título del libro.  
  - `autorlibro()`: Solicita al usuario el nombre del autor.  
  - `categoria()`: Menú interactivo para seleccionar una categoría predefinida.  

- **`menuLibro()`**: Crea un libro, permite llenarlo paso a paso y finalmente lo guarda en el registro central.  

---

### `Registro.py`
- **Clase `Registro`**
  - `__init__()`: Inicializa la lista de libros (`libros = []`).  
  - `agregar_libro(libro)`: Agrega un objeto `Libro` a la lista.  
  - `mostrar_libros()`: Muestra todos los libros registrados.  

- **Objeto global `registro`**: Contenedor centralizado de libros.  

---

### `Parcial.py`
- Función principal `main()` que coordina los menús:
  - **Opción 1:** Registrar usuario.  
  - **Opción 2:** Registrar libro.  
  - **Opción 3:** Mostrar libros registrados.  
  - **Opción 4:** Cerrar sesión.  

---

## ⚙️ Justificación Técnica de las Decisiones de Diseño

1. **Modularización por clases**  
   - Se creó una clase `Usuario`, una clase `Libro` y una clase `Registro`. Esto facilita el mantenimiento, la escalabilidad y la reutilización del código.  

2. **Objeto global `registro`**  
   - Permite centralizar el almacenamiento de todos los libros en memoria, accesible desde cualquier parte del proyecto sin necesidad de pasar referencias constantemente.  

3. **Menús interactivos**  
   - Cada módulo tiene su propio menú (`menuUsuario` y `menuLibro`) para mantener una interfaz clara y evitar que el archivo principal `Parcial.py` se sobrecargue de lógica.  

4. **Uso de listas en `Registro`**  
   - Se eligió una lista para almacenar libros por ser una estructura flexible, que permite añadir, recorrer y mostrar elementos fácilmente.  

5. **Separación entre lógica de usuario y lógica de negocio**  
   - `Usuario` y `Libro` manejan la captura de datos, mientras que `Registro` gestiona el almacenamiento. Esto sigue un diseño más cercano al patrón **MVC simplificado**.  
- Implementar persistencia con archivos (guardar y cargar usuarios/libros desde un archivo `.json` o `.txt`).  
- Validaciones adicionales (evitar títulos vacíos o teléfonos no válidos).  
- Añadir más categorías dinámicamente.  

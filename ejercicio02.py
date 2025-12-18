class Biblioteca:
    def __init__(self):
        self.libros = []
            
    def agregar_libro(self, libro):
        self.libros.append(libro)

    def listar_libros(self):
        if not self.libros:
            print(f"No hay libros registrados en la biblioteca.")
            return

        for libro in self.libros:
            estado = "Disponible" if libro.disponible else "Prestado"
            print(f"Título: {libro.titulo} | Autor: {libro.autor} | Año: {libro.año} | Estado: {estado}")
    
    def buscar_por_autor(self, autor):
        encontrados = False

        for libro in self.libros:
            if libro.autor.lower() == autor.lower():
                estado = "Disponible" if libro.disponible else "Prestado"
                print(f"Título: {libro.titulo} | Año: {libro.año} | Estado: {estado}")
                encontrados = True

        if not encontrados:
            print(f"No se encontraron libros de ese autor.")
    
    def prestar_por_titulo(self, titulo):
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                libro.prestar()   
                return
        print(f"No se encontró un libro con ese título.")

class Libro:
    def __init__(self, titulo, autor, año, disponible = True):
        self.titulo = titulo
        self.autor = autor
        self.año = año
        self.disponible = disponible
    
    def prestar(self):
        if (self.disponible != False):
            print(f"Libro prestado: ", self.titulo)
            self.disponible = False
        else:
            print(f"El libro ya ha sido prestado.")
    
    def devolver(self):
        if (self.disponible == False):
            print(f"Gracias por devolver: ", self.titulo)
            self.disponible = True
        else:
            print(f"El libro no ha sido prestado.")
            
class LibroDigital(Libro):
    def __init__(self, titulo, autor, año, formato, tamañoMB):
        super().__init__(titulo, autor, año, disponible=True)
        self.formato = formato
        self.tamañoMB = tamañoMB
    
    def prestar(self):
        print(f"Libro digital descargado: {self.titulo} ({self.formato}, {self.tamañoMB}MB)")
        
biblioteca = Biblioteca()
libro1 = Libro("1984", "George Orwell", 1949)
libro2 = Libro("El Principito", "Antoine de Saint-Exupéry", 1943)
libro3 = Libro("Cien años de soledad", "Gabriel García Márquez", 1967)
libro4 = LibroDigital("Python para Todos", "Guido van Rossum", 2023, "PDF", 5)
libro5 = LibroDigital("Aprendiendo Java", "James Gosling", 2022, "EPUB", 8)

biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)
biblioteca.agregar_libro(libro4)
biblioteca.agregar_libro(libro5)

biblioteca.listar_libros()

biblioteca.prestar_por_titulo("1984")

for i in range(5):
    print(f"Intento {i+1}: ", end="")
    biblioteca.prestar_por_titulo("Python para Todos")

biblioteca.prestar_por_titulo("1984")

biblioteca.buscar_por_autor("George Orwell")
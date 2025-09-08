# ==============================
# Sistema de Gestión de Biblioteca Digital
# ==============================

# Clase Libro
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # Tupla inmutable (titulo, autor)
        self.info = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.info[0]} por {self.info[1]} | Categoría: {self.categoria} | ISBN: {self.isbn}"


# Clase Usuario
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista de objetos Libro

    def __str__(self):
        return f"Usuario: {self.nombre} | ID: {self.id_usuario}"


# Clase Biblioteca
class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario {isbn: Libro}
        self.usuarios = {}  # Diccionario {id_usuario: Usuario}
        self.ids_usuarios = set()  # Conjunto para IDs únicos

    # ------- Gestión de Libros -------
    def agregar_libro(self, libro):
        if libro.isbn in self.libros:
            print("❌ El libro con este ISBN ya existe en la biblioteca.")
        else:
            self.libros[libro.isbn] = libro
            print(f"✅ Libro agregado: {libro}")

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            eliminado = self.libros.pop(isbn)
            print(f"🗑️ Libro eliminado: {eliminado}")
        else:
            print("❌ No se encontró un libro con ese ISBN.")

    # ------- Gestión de Usuarios -------
    def registrar_usuario(self, usuario):
        if usuario.id_usuario in self.ids_usuarios:
            print("❌ El ID de usuario ya existe.")
        else:
            self.usuarios[usuario.id_usuario] = usuario
            self.ids_usuarios.add(usuario.id_usuario)
            print(f"✅ Usuario registrado: {usuario}")

    def dar_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            eliminado = self.usuarios.pop(id_usuario)
            self.ids_usuarios.remove(id_usuario)
            print(f"🗑️ Usuario eliminado: {eliminado}")
        else:
            print("❌ Usuario no encontrado.")

    # ------- Préstamos -------
    def prestar_libro(self, id_usuario, isbn):
        if id_usuario not in self.usuarios:
            print("❌ Usuario no registrado.")
            return
        if isbn not in self.libros:
            print("❌ Libro no disponible en la biblioteca.")
            return

        usuario = self.usuarios[id_usuario]
        libro = self.libros.pop(isbn)  # Quita el libro del diccionario
        usuario.libros_prestados.append(libro)
        print(f"📚 Libro prestado: {libro} -> {usuario.nombre}")

    def devolver_libro(self, id_usuario, isbn):
        if id_usuario not in self.usuarios:
            print("❌ Usuario no registrado.")
            return

        usuario = self.usuarios[id_usuario]
        for libro in usuario.libros_prestados:
            if libro.isbn == isbn:
                usuario.libros_prestados.remove(libro)
                self.libros[isbn] = libro
                print(f"🔄 Libro devuelto: {libro} <- {usuario.nombre}")
                return
        print("❌ El usuario no tiene prestado este libro.")

    # ------- Búsquedas -------
    def buscar_libros(self, criterio, valor):
        resultados = []
        for libro in self.libros.values():
            if criterio == "titulo" and libro.info[0].lower() == valor.lower():
                resultados.append(libro)
            elif criterio == "autor" and libro.info[1].lower() == valor.lower():
                resultados.append(libro)
            elif criterio == "categoria" and libro.categoria.lower() == valor.lower():
                resultados.append(libro)

        if resultados:
            print(f"🔎 Resultados de búsqueda por {criterio}='{valor}':")
            for r in resultados:
                print(" -", r)
        else:
            print(f"❌ No se encontraron libros con {criterio}='{valor}'.")

    # ------- Listar Libros Prestados -------
    def listar_libros_prestados(self, id_usuario):
        if id_usuario not in self.usuarios:
            print("❌ Usuario no registrado.")
            return
        usuario = self.usuarios[id_usuario]
        if usuario.libros_prestados:
            print(f"📚 Libros prestados a {usuario.nombre}:")
            for libro in usuario.libros_prestados:
                print(" -", libro)
        else:
            print(f"{usuario.nombre} no tiene libros prestados.")


# ==============================
# PRUEBA DEL SISTEMA
# ==============================

# Crear la biblioteca
biblioteca = Biblioteca()

# Crear libros
libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "Novela", "12345")
libro2 = Libro("Python para Todos", "Raúl González", "Programación", "67890")
libro3 = Libro("El Principito", "Antoine de Saint-Exupéry", "Infantil", "54321")

# Agregar libros
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)

# Crear usuarios
usuario1 = Usuario("Ana López", "U001")
usuario2 = Usuario("Carlos Pérez", "U002")

# Registrar usuarios
biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

# Préstamo de libros
biblioteca.prestar_libro("U001", "12345")
biblioteca.prestar_libro("U002", "67890")

# Listar libros prestados
biblioteca.listar_libros_prestados("U001")
biblioteca.listar_libros_prestados("U002")

# Devolución de libro
biblioteca.devolver_libro("U001", "12345")

# Buscar libros por categoría
biblioteca.buscar_libros("categoria", "Infantil")

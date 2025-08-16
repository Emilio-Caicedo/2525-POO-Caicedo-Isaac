    # Sistema de Gestión de Inventario Tecnológico
    # Autor: Emilio Caicedo
    # Descripción:
    # Este programa permite gestionar un inventario de productos
    # con opciones para añadir, eliminar, actualizar, buscar y mostrar.

# Clase Producto
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        """
        Constructor de la clase Producto.
        :param id_producto: ID único del producto
        :param nombre: Nombre del producto
        :param cantidad: Cantidad disponible
        :param precio: Precio unitario
        """
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Métodos getters
    def get_id(self):
        return self.id_producto

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    # Métodos setters
    def set_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def set_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad

    def set_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    def __str__(self):
        """
        Representación en texto del producto (para imprimir fácilmente)
        """
        return f"ID: {self.id_producto} | Nombre: {self.nombre} | Cantidad: {self.cantidad} | Precio: ${self.precio:.2f}"

# Clase Inventario
class Inventario:
    def __init__(self):
        """
        Constructor: crea una lista vacía para almacenar los productos.
        """
        self.productos = []

    def agregar_producto(self, producto):
        """
        Añade un nuevo producto al inventario si el ID es único.
        """
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("Error: Ya existe un producto con ese ID.")
                return
        self.productos.append(producto)
        print("Producto añadido con éxito.")

    def eliminar_producto(self, id_producto):
        """
        Elimina un producto por su ID.
        """
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                print("Producto eliminado.")
                return
        print("Producto no encontrado.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        """
        Actualiza la cantidad y/o el precio de un producto.
        """
        for p in self.productos:
            if p.get_id() == id_producto:
                if nueva_cantidad is not None:
                    p.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)
                print("Producto actualizado.")
                return
        print("Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
        """
        Busca productos cuyo nombre contenga la palabra indicada (no es sensible a mayúsculas).
        """
        resultados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        if resultados:
            print("Resultados de búsqueda:")
            for r in resultados:
                print(r)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_todos(self):
        """
        Muestra todos los productos del inventario.
        """
        if not self.productos:
            print("El inventario está vacío.")
        else:
            print("Inventario:")
            for p in self.productos:
                print(p)

# Interfaz de Usuario (Menú en Consola)
def mostrar_menu():
    print("\n===== Sistema de Gestión Inventario Tecnológico =====")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto por nombre")
    print("5. Mostrar todos los productos")
    print("6. Salir")
    print("============================================")

# Función principal
def main():
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("Ingrese ID del producto: ")
            nombre = input("Ingrese nombre del producto: ")
            cantidad = int(input("Ingrese cantidad: "))
            precio = float(input("Ingrese precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == "2":
            id_producto = input("Ingrese ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("Ingrese ID del producto a actualizar: ")
            nueva_cantidad = input("Ingrese nueva cantidad (o deje vacío): ")
            nuevo_precio = input("Ingrese nuevo precio (o deje vacío): ")

            nueva_cantidad = int(nueva_cantidad) if nueva_cantidad else None
            nuevo_precio = float(nuevo_precio) if nuevo_precio else None

            inventario.actualizar_producto(id_producto, nueva_cantidad, nuevo_precio)

        elif opcion == "4":
            nombre_buscar = input("Ingrese el nombre o parte del nombre: ")
            inventario.buscar_por_nombre(nombre_buscar)

        elif opcion == "5":
            inventario.mostrar_todos()

        elif opcion == "6":
            print("Saliendo del sistema. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
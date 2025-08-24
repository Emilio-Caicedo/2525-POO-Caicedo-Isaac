    # Sistema de Gestión de Inventario Tecnológico con Archivos
    # Autor: Emilio Caicedo
    # Descripción:
    # Este programa permite gestionar un inventario de productos
    # con opciones para añadir, eliminar, actualizar, buscar y mostrar.
    # Ahora con persistencia en archivo JSON y manejo de excepciones.

import json
import os

# ================== Clase Producto ==================
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_id(self):
        return self.id_producto

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    def set_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def set_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad

    def set_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    def __str__(self):
        return f"ID: {self.id_producto} | Nombre: {self.nombre} | Cantidad: {self.cantidad} | Precio: ${self.precio:.2f}"

    def to_dict(self):
        """Convierte el objeto en un diccionario (para JSON)."""
        return {
            "id": self.id_producto,
            "nombre": self.nombre,
            "cantidad": self.cantidad,
            "precio": self.precio
        }

    @staticmethod
    def from_dict(data):
        """Crea un objeto Producto desde un diccionario."""
        return Producto(data["id"], data["nombre"], data["cantidad"], data["precio"])

# ================== Clase Inventario ==================
class Inventario:
    def __init__(self, archivo="Inventario.json"):
        self.archivo = archivo
        self.productos = []
        self.cargar_desde_archivo()

    def guardar_en_archivo(self):
        """Guarda el inventario en un archivo JSON con manejo de excepciones."""
        try:
            with open(self.archivo, "w", encoding="utf-8") as f:
                json.dump([p.to_dict() for p in self.productos], f, indent=4, ensure_ascii=False)
            print("Inventario guardado correctamente en archivo.")
        except PermissionError:
            print("Error: No tienes permisos para escribir en el archivo.")
        except Exception as e:
            print(f"Error al guardar el inventario: {e}")

    def cargar_desde_archivo(self):
        """Carga los productos desde el archivo JSON si existe."""
        if not os.path.exists(self.archivo):
            print("Archivo de inventario no encontrado. Se creará uno nuevo al guardar.")
            return
        try:
            with open(self.archivo, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.productos = [Producto.from_dict(p) for p in data]
            print("Inventario cargado desde archivo.")
        except FileNotFoundError:
            print("Archivo no encontrado. Se iniciará un inventario vacío.")
        except json.JSONDecodeError:
            print("Error: El archivo está corrupto. Se iniciará un inventario vacío.")
        except Exception as e:
            print(f"Error al cargar inventario: {e}")

    def agregar_producto(self, producto):
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("Error: Ya existe un producto con ese ID.")
                return
        self.productos.append(producto)
        self.guardar_en_archivo()
        print("Producto añadido con éxito.")

    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                self.guardar_en_archivo()
                print("Producto eliminado.")
                return
        print("Producto no encontrado.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        for p in self.productos:
            if p.get_id() == id_producto:
                if nueva_cantidad is not None:
                    p.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)
                self.guardar_en_archivo()
                print("Producto actualizado.")
                return
        print("Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
        resultados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        if resultados:
            print("Resultados de búsqueda:")
            for r in resultados:
                print(r)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_todos(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            print("Inventario:")
            for p in self.productos:
                print(p)

# ================== Interfaz de Usuario ==================
def mostrar_menu():
    print("\n===== Sistema de Gestión Inventario Tecnológico =====")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto por nombre")
    print("5. Mostrar todos los productos")
    print("6. Salir")
    print("====================================================")

def main():
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("Ingrese ID del producto: ")
            nombre = input("Ingrese nombre del producto: ")
            try:
                cantidad = int(input("Ingrese cantidad: "))
                precio = float(input("Ingrese precio: "))
                producto = Producto(id_producto, nombre, cantidad, precio)
                inventario.agregar_producto(producto)
            except ValueError:
                print("Error: La cantidad y el precio deben ser valores numéricos.")

        elif opcion == "2":
            id_producto = input("Ingrese ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("Ingrese ID del producto a actualizar: ")
            nueva_cantidad = input("Ingrese nueva cantidad (o deje vacío): ")
            nuevo_precio = input("Ingrese nuevo precio (o deje vacío): ")

            try:
                nueva_cantidad = int(nueva_cantidad) if nueva_cantidad else None
                nuevo_precio = float(nuevo_precio) if nuevo_precio else None
                inventario.actualizar_producto(id_producto, nueva_cantidad, nuevo_precio)
            except ValueError:
                print("Error: Los valores de cantidad y precio deben ser numéricos.")

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

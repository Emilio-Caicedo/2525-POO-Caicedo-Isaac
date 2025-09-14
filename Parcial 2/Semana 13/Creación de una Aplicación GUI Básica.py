    #Creación de una Aplicación GUI Básica
    #Sistema de Gestión de Inventario Tecnológico con Tkinter
    #Descripción:
    #            - Implementa una interfaz gráfica para gestionar un inventario.
    #            - Incluye tabla (Treeview) para mostrar productos con ID, nombre, cantidad y precio.
    #            - Funcionalidades: agregar producto, borrar seleccionado, limpiar tabla.
    #            - Manejo de eventos: Enter agrega, Supr borra selección.
#Autor: Emilio Caicedo

import tkinter as tk
from tkinter import ttk, messagebox

class InventarioGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gestión de Inventario Tecnológico")
        self.root.geometry("700x450")
        self.root.resizable(False, False)

        # --- Inventario inicial ---
        self.inventario = [
            (1, "Laptop Dell XPS 13", 5, 1200),
            (2, "Monitor LG 24''", 10, 200),
            (3, "Teclado Mecánico HyperX", 15, 80),
            (4, "Mouse Logitech MX Master 3", 7, 100),
            (5, "Disco Duro Externo 1TB", 20, 60)
        ]
        self._next_id = len(self.inventario) + 1

        # --- Encabezado ---
        encabezado = ttk.Label(self.root, text="Gestión de Inventario", font=("Segoe UI", 14))
        encabezado.pack(pady=10)

        # --- Frame superior ---
        frame_top = ttk.Frame(self.root)
        frame_top.pack(fill=tk.X, padx=12)

        ttk.Label(frame_top, text="Nombre:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_nombre = ttk.Entry(frame_top)
        self.entry_nombre.grid(row=0, column=1, padx=5)

        ttk.Label(frame_top, text="Cantidad:").grid(row=0, column=2, padx=5, pady=5)
        self.entry_cantidad = ttk.Entry(frame_top)
        self.entry_cantidad.grid(row=0, column=3, padx=5)

        ttk.Label(frame_top, text="Precio:").grid(row=0, column=4, padx=5, pady=5)
        self.entry_precio = ttk.Entry(frame_top)
        self.entry_precio.grid(row=0, column=5, padx=5)

        ttk.Button(frame_top, text="Agregar", command=self.agregar_producto).grid(row=0, column=6, padx=5)
        ttk.Button(frame_top, text="Borrar seleccionado", command=self.borrar_seleccion).grid(row=0, column=7, padx=5)
        ttk.Button(frame_top, text="Limpiar tabla", command=self.limpiar_tabla).grid(row=0, column=8, padx=5)

        # --- Tabla ---
        columnas = ("id", "nombre", "cantidad", "precio")
        self.tree = ttk.Treeview(self.root, columns=columnas, show="headings", height=12)
        self.tree.heading("id", text="ID")
        self.tree.column("id", width=50, anchor=tk.CENTER)
        self.tree.heading("nombre", text="Nombre")
        self.tree.column("nombre", width=300, anchor=tk.W)
        self.tree.heading("cantidad", text="Cantidad")
        self.tree.column("cantidad", width=100, anchor=tk.CENTER)
        self.tree.heading("precio", text="Precio ($)")
        self.tree.column("precio", width=100, anchor=tk.CENTER)
        self.tree.pack(fill=tk.BOTH, expand=True, padx=12, pady=12)

        # --- Barra de estado ---
        self.status_var = tk.StringVar(value="Inventario listo")
        status = ttk.Label(self.root, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W)
        status.pack(fill=tk.X, side=tk.BOTTOM)

        # --- Eventos ---
        self.root.bind("<Return>", lambda ev: self.agregar_producto())
        self.root.bind("<Delete>", lambda ev: self.borrar_seleccion())

        # --- Cargar inventario inicial ---
        for producto in self.inventario:
            self.tree.insert("", tk.END, iid=str(producto[0]), values=producto)

    def agregar_producto(self):
        nombre = self.entry_nombre.get().strip()
        cantidad = self.entry_cantidad.get().strip()
        precio = self.entry_precio.get().strip()

        if not nombre or not cantidad.isdigit() or not precio.replace(".", "", 1).isdigit():
            messagebox.showwarning("Advertencia", "Ingrese valores válidos: Nombre, Cantidad (número), Precio (número).")
            return

        producto = (self._next_id, nombre, int(cantidad), float(precio))
        self.tree.insert("", tk.END, iid=str(self._next_id), values=producto)
        self._next_id += 1

        self.entry_nombre.delete(0, tk.END)
        self.entry_cantidad.delete(0, tk.END)
        self.entry_precio.delete(0, tk.END)

        self.status_var.set(f"Producto agregado: {nombre}")

    def borrar_seleccion(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showinfo("Información", "No hay elementos seleccionados.")
            return
        for iid in seleccion:
            self.tree.delete(iid)
        self.status_var.set("Producto(s) eliminado(s)")

    def limpiar_tabla(self):
        confirmar = messagebox.askyesno("Confirmar", "¿Desea borrar todos los productos?")
        if confirmar:
            for child in self.tree.get_children():
                self.tree.delete(child)
            self._next_id = 1
            self.status_var.set("Inventario limpiado")

def main():
    root = tk.Tk()
    app = InventarioGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
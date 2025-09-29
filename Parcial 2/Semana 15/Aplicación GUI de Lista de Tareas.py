#   Agenda Personal - Emilio Caicedo
#   Descripción: Aplicación de escritorio que permite agregar, ver, modificar, marcar como completados
#   y eliminar eventos o tareas.
#   Requisitos:
#   - Interfaz con Tkinter
#   - Entrada de fecha
#   - Entrada de hora y descripción
#   - Botones: Agregar, Modificar, Marcar, Eliminar, Salir
#   - Guardado automático en JSON

import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import uuid
import json
import os

try:
    from tkcalendar import DateEntry
    HAS_TKCALENDAR = True
except Exception:
    HAS_TKCALENDAR = False


class AgendaApp(tk.Tk):
    FILE_NAME = "eventos.json"

    def __init__(self):
        super().__init__()
        self.title("Agenda Personal de Emilio Caicedo")
        self.geometry("750x520")
        self.resizable(False, False)

        self.eventos = {}

        self._crear_frames()
        self._crear_treeview()
        self._crear_campos_entrada()
        self._crear_botones()

        # Atajo: Enter para agregar evento
        self.bind("<Return>", lambda e: self.agregar_evento())

        # Cargar eventos desde JSON
        self._cargar_eventos()

        # Guardar automáticamente al cerrar
        self.protocol("WM_DELETE_WINDOW", self._on_close)

    def _crear_frames(self):
        self.frame_lista = ttk.Frame(self, padding=(10, 10))
        self.frame_lista.pack(side=tk.TOP, fill=tk.BOTH, expand=False)

        self.frame_entradas = ttk.Frame(self, padding=(10, 5))
        self.frame_entradas.pack(side=tk.TOP, fill=tk.X)

        self.frame_acciones = ttk.Frame(self, padding=(10, 10))
        self.frame_acciones.pack(side=tk.TOP, fill=tk.X)

    def _crear_treeview(self):
        columns = ("fecha", "hora", "descripcion")
        self.tree = ttk.Treeview(self.frame_lista, columns=columns, show="headings", height=12)
        self.tree.heading("fecha", text="Fecha")
        self.tree.heading("hora", text="Hora")
        self.tree.heading("descripcion", text="Descripción")
        self.tree.column("fecha", width=120, anchor=tk.CENTER)
        self.tree.column("hora", width=80, anchor=tk.CENTER)
        self.tree.column("descripcion", width=500, anchor=tk.W)

        vsb = ttk.Scrollbar(self.frame_lista, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=vsb.set)
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        vsb.pack(side=tk.LEFT, fill=tk.Y)

        # Doble clic → marcar como completado
        self.tree.bind("<Double-1>", lambda e: self.marcar_completado())

    def _crear_campos_entrada(self):
        ttk.Label(self.frame_entradas, text="Fecha:").grid(row=0, column=0, padx=5, pady=6, sticky=tk.W)
        ttk.Label(self.frame_entradas, text="Hora:").grid(row=0, column=2, padx=5, pady=6, sticky=tk.W)
        ttk.Label(self.frame_entradas, text="Descripción:").grid(row=1, column=0, padx=5, pady=6, sticky=tk.W)

        if HAS_TKCALENDAR:
            self.entry_fecha = DateEntry(self.frame_entradas, date_pattern='yyyy-mm-dd')
        else:
            self.entry_fecha = ttk.Entry(self.frame_entradas)
            self.entry_fecha.insert(0, datetime.now().strftime('%Y-%m-%d'))

        self.entry_fecha.grid(row=0, column=1, padx=5, pady=6, sticky=tk.W)

        horas = [f"{h:02d}" for h in range(0, 24)]
        minutos = [f"{m:02d}" for m in range(0, 60, 5)]
        self.combo_hora = ttk.Combobox(self.frame_entradas, values=horas, width=3, state="readonly")
        self.combo_hora.set("09")
        self.combo_hora.grid(row=0, column=3, padx=2, pady=6, sticky=tk.W)

        self.combo_min = ttk.Combobox(self.frame_entradas, values=minutos, width=3, state="readonly")
        self.combo_min.set("00")
        self.combo_min.grid(row=0, column=4, padx=2, pady=6, sticky=tk.W)

        self.entry_desc = ttk.Entry(self.frame_entradas, width=70)
        self.entry_desc.grid(row=1, column=1, columnspan=4, padx=5, pady=6, sticky=tk.W)

    def _crear_botones(self):
        ttk.Button(self.frame_acciones, text="Agregar Evento", command=self.agregar_evento).pack(side=tk.LEFT, padx=6)
        ttk.Button(self.frame_acciones, text="Modificar Evento", command=self.modificar_evento).pack(side=tk.LEFT, padx=6)
        ttk.Button(self.frame_acciones, text="Marcar como Completado", command=self.marcar_completado).pack(side=tk.LEFT, padx=6)
        ttk.Button(self.frame_acciones, text="Eliminar Evento Seleccionado", command=self.eliminar_evento).pack(side=tk.LEFT, padx=6)
        ttk.Button(self.frame_acciones, text="Salir", command=self._on_close).pack(side=tk.RIGHT, padx=6)

    def agregar_evento(self):
        fecha = self.entry_fecha.get().strip()
        hora = f"{self.combo_hora.get()}:{self.combo_min.get()}"
        desc = self.entry_desc.get().strip()

        if not fecha or not self._validar_fecha(fecha):
            messagebox.showwarning("Validación", "Ingrese una fecha válida (AAAA-MM-DD).")
            return
        if not self._validar_hora(hora):
            messagebox.showwarning("Validación", "Seleccione una hora válida.")
            return
        if not desc:
            messagebox.showwarning("Validación", "La descripción no puede estar vacía.")
            return

        evento_id = str(uuid.uuid4())
        self.eventos[evento_id] = {"fecha": fecha, "hora": hora, "descripcion": desc}
        self.tree.insert('', tk.END, iid=evento_id, values=(fecha, hora, desc))

        self.entry_desc.delete(0, tk.END)
        self._guardar_eventos()

    def modificar_evento(self):
        seleccionado = self.tree.selection()
        if not seleccionado:
            messagebox.showinfo("Modificar", "No hay ningún evento seleccionado.")
            return

        item_id = seleccionado[0]

        fecha = self.entry_fecha.get().strip()
        hora = f"{self.combo_hora.get()}:{self.combo_min.get()}"
        desc = self.entry_desc.get().strip()

        if not fecha or not self._validar_fecha(fecha):
            messagebox.showwarning("Validación", "Ingrese una fecha válida (AAAA-MM-DD).")
            return
        if not self._validar_hora(hora):
            messagebox.showwarning("Validación", "Seleccione una hora válida.")
            return
        if not desc:
            messagebox.showwarning("Validación", "La descripción no puede estar vacía.")
            return

        self.eventos[item_id] = {"fecha": fecha, "hora": hora, "descripcion": desc}
        self.tree.item(item_id, values=(fecha, hora, desc))
        self._guardar_eventos()

        messagebox.showinfo("Modificar", "Evento actualizado correctamente.")

    def marcar_completado(self):
        seleccionado = self.tree.selection()
        if not seleccionado:
            messagebox.showinfo("Completar", "No hay ningún evento seleccionado.")
            return

        item_id = seleccionado[0]
        evento = self.eventos.get(item_id)

        if evento:
            desc = evento["descripcion"]
            if desc.startswith("✔ "):
                desc = desc[2:]
            else:
                desc = "✔ " + desc

            evento["descripcion"] = desc
            self.tree.item(item_id, values=(evento["fecha"], evento["hora"], desc))
            self._guardar_eventos()

    def eliminar_evento(self):
        seleccionado = self.tree.selection()
        if not seleccionado:
            messagebox.showinfo("Eliminar", "No hay ningún evento seleccionado.")
            return

        item_id = seleccionado[0]
        evento = self.eventos.get(item_id)
        if evento and messagebox.askyesno("Confirmar eliminación",
                                          f"¿Eliminar el evento del {evento['fecha']} a las {evento['hora']}?\n\n{evento['descripcion']}"):
            self.tree.delete(item_id)
            del self.eventos[item_id]
            self._guardar_eventos()

    def _guardar_eventos(self):
        with open(self.FILE_NAME, "w", encoding="utf-8") as f:
            json.dump(self.eventos, f, indent=4, ensure_ascii=False)

    def _cargar_eventos(self):
        if os.path.exists(self.FILE_NAME):
            try:
                with open(self.FILE_NAME, "r", encoding="utf-8") as f:
                    self.eventos = json.load(f)
                for eid, ev in self.eventos.items():
                    self.tree.insert('', tk.END, iid=eid, values=(ev["fecha"], ev["hora"], ev["descripcion"]))
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo cargar el archivo de eventos.\n{e}")

    def _on_close(self):
        self._guardar_eventos()
        self.destroy()

    def _validar_hora(self, hora_texto: str) -> bool:
        try:
            datetime.strptime(hora_texto, "%H:%M")
            return True
        except ValueError:
            return False

    def _validar_fecha(self, fecha_texto: str) -> bool:
        try:
            datetime.strptime(fecha_texto, "%Y-%m-%d")
            return True
        except ValueError:
            return False


if __name__ == '__main__':
    app = AgendaApp()
    app.mainloop()

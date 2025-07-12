class Mascota:
    def __init__(self, nombre, especie, edad):
        """
        Constructor de la clase Mascota.
        Este metodo se ejecuta automáticamente al crear una nueva mascota.
        Inicializa los atributos de nombre, especie y edad.
        """
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        print(f"Mascota creada: {self.nombre}, especie: {self.especie}, edad: {self.edad} años.")

    def mostrar_info(self):
        """
        Metodo que imprime la información de la mascota.
        """
        print(f"Nombre: {self.nombre}")
        print(f"Especie: {self.especie}")
        print(f"Edad: {self.edad} años")

    def __del__(self):
        """
        Destructor de la clase Mascota.
        Este metodo se ejecuta automáticamente cuando se elimina el objeto.
        Simula liberar recursos (por ejemplo, cerrar conexión a una base de datos).
        """
        print(f"La mascota {self.nombre} ha sido eliminada de la memoria.")
# Crear una instancia de la clase Mascota
mi_mascota = Mascota("Manchas", "Perro (Pitbull)", 5)

# Mostrar la información de la mascota
mi_mascota.mostrar_info()

# Eliminar el objeto manualmente (opcional, para ver el destructor)
del mi_mascota

# Si no se elimina manualmente, el destructor se llamará automáticamente al finalizar el programa

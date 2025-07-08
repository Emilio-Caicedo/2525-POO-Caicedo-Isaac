# Clase base: Mascota
class Mascota:
    def __init__(self, nombre, edad_meses, color):
        self.__nombre = nombre  # Encapsulación
        self.__edad_meses = edad_meses  # Encapsulación
        self.__color = color  # Encapsulación

    # Getters y setters
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    def get_edad_meses(self):
        return self.__edad_meses

    def set_edad_meses(self, nueva_edad):
        if nueva_edad >= 0:
            self.__edad_meses = nueva_edad
        else:
            print("La edad no puede ser negativa.")

    def get_color(self):
        return self.__color

    def set_color(self, nuevo_color):
        self.__color = nuevo_color

    # Método común (será sobrescrito por subclases)
    def hacer_sonido(self):
        return "La mascota hace un sonido."


# Clase derivada: Perro
class Perro(Mascota):
    def __init__(self, nombre, edad_meses, color, raza):
        super().__init__(nombre, edad_meses, color)  # Herencia
        self.raza = raza

    # Polimorfismo: redefinimos el método
    def hacer_sonido(self):
        return "¡Guau guau!"

    def descripcion(self):
        return (f"{self.get_nombre()} es un perro de raza {self.raza}, "
                f"color {self.get_color()}, con {self.get_edad_meses()} meses de edad.")


# -------------------------------
# Crear instancia de Manchas
manchas = Perro("Manchas", 5, "blanco con manchas negras", "Pitbull")

# Mostrar descripción y comportamiento
print(manchas.descripcion())  # Información de Manchas
print("Sonido:", manchas.hacer_sonido())  # Polimorfismo

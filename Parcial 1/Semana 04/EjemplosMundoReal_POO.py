# Isaac va a comprar un boleto de avión para viajar de Quito a Guayaquil.

# Programa: Sistema de Compra de Boletos de Avión.

# Clase que representa un vuelo

class Vuelo:
    def __init__(self, origen, destino, precio):
        self.origen = origen  # Ciudad de origen
        self.destino = destino  # Ciudad de destino
        self.precio = precio  # Precio del boleto
        self.boletos_disponibles = 10  # Cantidad de boletos disponibles

    def vender_boleto(self):
        if self.boletos_disponibles > 0:
            self.boletos_disponibles -= 1
            return True
        return False

    def __str__(self):
        return f"Vuelo de {self.origen} a {self.destino} - ${self.precio} - Boletos disponibles: {self.boletos_disponibles}"


# Clase que representa a un pasajero
class Pasajero:
    def __init__(self, nombre):
        self.nombre = nombre
        self.boleto = None  # Almacena el vuelo si compra un boleto

    def comprar_boleto(self, vuelo):
        if vuelo.vender_boleto():
            self.boleto = vuelo
            print(f"\n{self.nombre} ha comprado un boleto para el vuelo de {vuelo.origen} a {vuelo.destino}.")
        else:
            print(f"\nNo hay boletos disponibles para el vuelo de {vuelo.origen} a {vuelo.destino}.")


# Simulación de compra de boleto
vuelo_quito_guayaquil = Vuelo("Quito", "Guayaquil", 75)

# Mostrar detalles del vuelo
print(vuelo_quito_guayaquil)

# Crear pasajero Isaac
isaac = Pasajero("Isaac")

# Isaac compra el boleto
isaac.comprar_boleto(vuelo_quito_guayaquil)

# Mostrar detalles del vuelo después de la compra
print(vuelo_quito_guayaquil)

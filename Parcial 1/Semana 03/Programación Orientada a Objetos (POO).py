#Diseña una solución utilizando el paradigma de POO.
#Crea una clase que represente la información diaria del clima.
#Utiliza métodos de la clase para ingresar datos y calcular el promedio semanal.
#Asegúrate de aplicar conceptos como encapsulamiento, herencia o polimorfismo según sea apropiado.

# Clase que representa la información climática de un solo día
class DiaClima:
    def __init__(self, dia, temperatura=0.0):
        self.dia = dia  # Día del registro (1 al 7)
        self.__temperatura = temperatura  # Temperatura (privada - encapsulada)

    # Método para establecer la temperatura
    def set_temperatura(self, temperatura):
        self.__temperatura = temperatura

    # Método para obtener la temperatura
    def get_temperatura(self):
        return self.__temperatura

# Clase que gestiona la información climática de una semana
class SemanaClima:
    def __init__(self):
        # Crea una lista de objetos DiaClima para los 7 días
        self.dias = [DiaClima(dia) for dia in range(1, 8)]

    # Método para ingresar las temperaturas de cada día
    def ingresar_temperaturas(self):
        for dia in self.dias:
            temp = float(input(f"Ingrese la temperatura de su día {dia.dia}: "))
            dia.set_temperatura(temp)

    # Método para calcular el promedio semanal de temperaturas
    def calcular_promedio(self):
        total = sum(dia.get_temperatura() for dia in self.dias)
        return total / len(self.dias)

# Clase hija que extiende SemanaClima y añade funcionalidad adicional
class SemanaClimaExtendida(SemanaClima):
    # Método adicional para mostrar las temperaturas ingresadas
    def mostrar_temperaturas(self):
        print("Temperaturas registradas:")
        for dia in self.dias:
            print(f"Día {dia.dia}: {dia.get_temperatura()}°C")

# Función principal que controla la ejecución del programa
def main():
    print("=== PROMEDIO SEMANAL DEL CLIMA (POO) ===")
    semana = SemanaClimaExtendida()  # Crea una instancia de la clase extendida
    semana.ingresar_temperaturas()   # Llama al método para ingresar los datos
    semana.mostrar_temperaturas()    # Muestra las temperaturas registradas
    promedio = semana.calcular_promedio()  # Calcula el promedio semanal
    print(f"Su promedio semanal de temperatura es: {promedio:.2f}°C")  # Muestra el resultado

# Punto de entrada del programa
if __name__ == "__main__":
    main()

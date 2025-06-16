# Implementa una solución utilizando estructuras de funciones.
# Define funciones para la entrada de datos diarios (temperaturas) y el cálculo del promedio semanal.
# Organiza el código de manera lógica y funcional utilizando la programación tradicional.

# Función para ingresar las temperaturas de cada día de la semana por el usuario.
def ingresar_temperaturas():
    # [] Lista para almacenar las temperaturas
    temperaturas = []
    # Debe ingresar 7 veces (una por cada día de la semana)
    for dia in range(7):
        # Solicita al usuario la temperatura
        temp = float(input(f"Ingrese la temperatura de su día {dia + 1}: "))
        # Agrega la temperatura incertada de cada dia a la lista
        temperaturas.append(temp)
        # Devuelve la lista completa
    return temperaturas

# Función para calcular el promedio de las temperaturas ingresadas.
def calcular_promedio(temperaturas):
    # Para calcular el promedio realiza la suma total dividida por cantidad de n
    return sum(temperaturas) / len(temperaturas)

# Función principal que coordina la ejecución del programa
def main():
    print("=== PROMEDIO SEMANAL DEL CLIMA (TRADICIONAL) ===")
    # Llama a la función para ingresar las temperaturas
    temps = ingresar_temperaturas()
    # Calcula el promedio
    promedio = calcular_promedio(temps)
    # Muestra el promedio obtenido durante los 7 días
    print(f"Su promedio semanal de temperatura es: {promedio:.2f}°C")

# Punto de entrada del programa
if __name__ == "__main__":
    main()

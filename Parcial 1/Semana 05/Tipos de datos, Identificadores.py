# Programa: Conversor de Kilogramos a Gramos
# Descripción: Este programa solicita al usuario una cantidad en kilogramos, la convierte a gramos y muestra el resultado.
# Utiliza diferentes tipos de datos y sigue buenas prácticas de programación.

def convertir_kg_a_g(kg):
    """
    Convierte una cantidad de kilogramos a gramos.
    1 kilogramo = 1000 gramos
    :param kg: cantidad en kilogramos (float)
    :return: cantidad en gramos (float)
    """
    gramos = kg * 1000
    return gramos

# Solicita al usuario que ingrese una cantidad en kilogramos
entrada_usuario = input("Ingresa la cantidad en kilogramos: ")
es_valido = entrada_usuario.replace('.', '', 1).isdigit()  # Validación simple para flotantes positivos

if es_valido:
    kilogramos = float(entrada_usuario)  # Tipo de dato float
    gramos = convertir_kg_a_g(kilogramos)
    print(f"{kilogramos} kilogramos equivalen a {gramos} gramos.")  # Tipo string con interpolación
else:
    print("Entrada inválida. Por favor, ingresa un número válido.")  # Manejo de errores con string

# Variable boolean para indicar si la conversión fue exitosa
conversion_exitosa = es_valido
print("¿La conversión fue exitosa?", conversion_exitosa)  # Tipo boolean

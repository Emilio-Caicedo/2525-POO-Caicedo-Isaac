import os


def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    print(f"Intentando Abrir: {ruta_script_absoluta}")
    try:
        with open(ruta_script_absoluta, 'r', encoding="utf-8") as archivo:
            codigo = archivo.read()
            print(f"\n--- Código de {ruta_script} ---\n")
            print (codigo)
            print("\n--- Resultado de la ejecución ---\n")
            exec(codigo, globals())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")


def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

    opciones = {
        '1': 'Parcial 1/Semana 02/Desarrollo de Ejemplos de Técnicas de Programación.py ',
        '2': 'Parcial 1/Semana 03/Programación Orientada a Objetos (POO).py ',
        '3': 'Parcial 1/Semana 03/Programación Tradicional.py ',
        '4': 'Parcial 1/Semana 04/EjemplosMundoReal_POO.py ',
        '5': 'Parcial 1/Semana 05/Tipos de datos, Identificadores.py ',
        '6': 'Parcial 1/Semana 06/Clases, Objetos, Herencia, Encapsulamiento y Polimorfismo..py ',
        '7': 'Parcial 1/Semana 07/Implementación de Constructores y Destructores en Python..py '
    }

    while True:
        print("\nMenu Principal - Dashboard")
        # Imprime las opciones del menú
        for key in opciones:
            print(f"{key} - {opciones[key]}")
        print("0 - Salir")

        eleccion = input("Elige un script para ver su código o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            # Asegura que el path sea absoluto
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
            input("\nPresione Enter para regresar al menú...")
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()
# bucles.py

"""
Este programa muestra ejemplos de uso de bucles en Python.
"""

def main():
    """
    Función principal del programa.
    """
    # Ejemplo de bucle while
    contador = 0

    while contador < 5:
        print("El contador es:", contador)
        contador += 1

    # Ejemplo de bucle for
    nombres = ["Juan", "María", "Carlos"]

    for nombre in nombres:
        print("Hola,", nombre)

    # Ejemplo de bucle for con rango
    for i in range(5):
        print("El valor de i es:", i)

if __name__ == "__main__":
    main()

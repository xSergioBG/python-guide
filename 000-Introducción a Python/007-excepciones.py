# 007-excepciones.py

"""
Este programa muestra ejemplos de manejo de excepciones en Python.
"""

def main():
    """
    Función principal del programa.
    """
    # Ejemplo de manejo de excepciones
    try:
        # División de dos números
        numero1 = int(input("Ingrese el primer número: "))
        numero2 = int(input("Ingrese el segundo número: "))
        resultado = numero1 / numero2
        print("El resultado de la división es:", resultado)
    except ValueError:
        print("Error: Ingrese solo números enteros.")
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")
    except Exception as exception:
        print("Error:", exception)

    # Ejemplo de excepción personalizada
    try:
        nombre = input("Ingrese su nombre: ")
        if len(nombre) < 3:
            raise ValueError("El nombre debe tener al menos 3 caracteres.")
        print("Hola,", nombre + "!")
    except ValueError as value_exception:
        print("Error:", value_exception)

if __name__ == "__main__":
    main()

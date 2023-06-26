# funciones.py

"""
Este programa muestra ejemplos de declaración y uso de funciones en Python.
"""

def saludar(nombre):
    """
    Esta función muestra un saludo con el nombre proporcionado.
    """
    print("¡Hola,", nombre, "! Bienvenido.")

def sumar(numero1, numero2):
    """
    Esta función suma dos números y devuelve el resultado.
    """
    resultado = numero1 + numero2
    return resultado

def main():
    """
    Función principal del programa.
    """
    # Ejemplo de llamada a una función de saludo
    nombre = "Juan"
    saludar(nombre)

    # Ejemplo de llamada a una función de suma
    numero1 = 10
    numero2 = 5
    resultado = sumar(numero1, numero2)
    print("El resultado de la suma es:", resultado)

if __name__ == "__main__":
    main()

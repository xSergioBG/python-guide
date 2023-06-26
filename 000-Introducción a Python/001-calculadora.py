# calculadora.py

"""
Este programa implementa una calculadora básica en la consola.
Permite realizar operaciones de suma, resta, multiplicación y división.
"""

def sumar(num1, num2):
    """
    Suma dos números y devuelve el resultado.
    """
    return num1 + num2

def restar(num1, num2):
    """
    Resta dos números y devuelve el resultado.
    """
    return num1 - num2

def multiplicar(num1, num2):
    """
    Multiplica dos números y devuelve el resultado.
    """
    return num1 * num2

def dividir(num1, num2):
    """
    Divide dos números y devuelve el resultado.
    Si se intenta dividir por cero, muestra un mensaje de error y devuelve None.
    """
    if num2 != 0:
        return num1 / num2
    else:
        print("¡Error! No se puede dividir por cero.")
        return None

def main():
    """
    Función principal del programa.
    Solicita al usuario ingresar dos números y muestra el resultado de las operaciones.
    """
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    print("Suma:", sumar(num1, num2))
    print("Resta:", restar(num1, num2))
    print("Multiplicación:", multiplicar(num1, num2))
    resultado_division = dividir(num1, num2)
    if resultado_division is not None:
        print("División:", resultado_division)

if __name__ == "__main__":
    main()

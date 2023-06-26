# 003-condicionales.py

"""
Este programa muestra ejemplos de uso de condicionales en Python.
"""

def main():
    """
    Función principal del programa.
    """
    # Ejemplo de condicional if
    numero = 10

    if numero > 0:
        print("El número es positivo.")
    elif numero < 0:
        print("El número es negativo.")
    else:
        print("El número es cero.")

    # Ejemplo de condicional if anidado
    edad = 18
    tiene_licencia = True

    if edad >= 18:
        if tiene_licencia:
            print("Puede conducir.")
        else:
            print("No puede conducir sin licencia.")
    else:
        print("No puede conducir.")

    # Ejemplo de condicional if-else en una línea (operador ternario)
    es_mayor_edad = True if edad >= 18 else False

    print("Es mayor de edad:", es_mayor_edad)

if __name__ == "__main__":
    main()

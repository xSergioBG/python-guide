# entrada_salida.py

"""
Este programa muestra ejemplos de entrada y salida en Python.
"""

def main():
    """
    Función principal del programa.
    """
    # Ejemplo de entrada de datos
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))

    # Ejemplo de salida de datos
    print(f"¡Hola, {nombre}! Usted tiene {edad} años.")

    # Ejemplo de formateo de salida
    promedio = 7.5
    print(f"Su promedio es: {promedio:.2f}")

    # Ejemplo de escritura en un archivo
    with open("datos.txt", "w", encoding="utf-8") as archivo:
        archivo.write(f"Nombre: {nombre}\n")
        archivo.write(f"Edad: {edad}\n")

if __name__ == "__main__":
    main()

# ordenamiento_burbuja.py

"""
Este es un ejemplo de implementación del algoritmo de ordenamiento burbuja en Python.
"""

def bubble_sort(arr):
    """
    Ordena una lista utilizando el algoritmo de ordenamiento burbuja.
    """
    numero_de_elementos = len(arr)
    for i in range(numero_de_elementos - 1):
        for j in range(numero_de_elementos - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

if __name__ == "__main__":
    # Ejemplo de uso
    lista = [5, 2, 9, 1, 3]
    bubble_sort(lista)
    print(lista)

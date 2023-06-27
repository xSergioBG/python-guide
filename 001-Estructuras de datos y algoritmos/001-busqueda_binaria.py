# busqueda_binaria.py

"""
Este es un ejemplo de implementación del algoritmo de búsqueda binaria en Python.
"""

def binary_search(arr, target):
    """
    Realiza una búsqueda binaria en una lista ordenada para encontrar un elemento objetivo.
    Devuelve el índice del elemento si se encuentra, o -1 si no está presente.
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

if __name__ == "__main__":
    # Ejemplo de uso
    lista = [1, 3, 5, 7, 9]
    elemento = 5
    resultado = binary_search(lista, elemento)

    if resultado != -1:
        print(f"El elemento {elemento} se encuentra en el índice {resultado}.")
    else:
        print(f"El elemento {elemento} no está presente en la lista.")

from random import randint
max_rows = 5
max_columns = 5

def generar_matriz() -> list:
    """
    Genera una matriz de 5x5 con numero enteros del 1 al 10.

    Returns:
        list: matriz de 5x5
    """
    
    matrix = list()

    for row in range(max_rows):
        matrix.append([randint(0, 10) for col in range(max_columns)])
    
    return matrix
    
def buscar_secuencia(matrix: list=generar_matriz()) -> None:
    """
    Busca secuencias de 4 numeros consecutivos en filas primero
    y despues columnas. Muestra la primer posicion, y la ultima en caso de encontrar.
    Tambien muestra la matriz

    >>> matrix = [[1, 2, 3, 4, 6], [6, 4, 7, 5, 9], [7, 5, 6, 6, 1], [8, 3, 1, 7, 5], [9, 5, 6, 7, 8]]
    >>> buscar_secuencia(matrix)
    Hay una secuencia de 4 numeros consecutivos en:
    Primer numero fila 1 columna 1, ultimo numero fila 1 columna 4
    Primer numero fila 5 columna 2, ultimo numero fila 5 columna 5
    Primer numero fila 2 columna 1, ultimo numero fila 5 columna 1
    Primer numero fila 1 columna 4, ultimo numero fila 4 columna 4
    <BLANKLINE>
    La matriz es:
    [1, 2, 3, 4, 6]
    [6, 4, 7, 5, 9]
    [7, 5, 6, 6, 1]
    [8, 3, 1, 7, 5]
    [9, 5, 6, 7, 8]
    <BLANKLINE>

    >>> matrix = [[4, 4, 0, 6, 10], [2, 8, 3, 10, 5], [8, 10, 6, 7, 6], [0, 1, 4, 2, 6], [4, 9, 5, 2, 1]]
    >>> buscar_secuencia(matrix)
    No hay secuencias consecutivas en la matriz
    <BLANKLINE>
    La matriz es:
    [4, 4, 0, 6, 10]
    [2, 8, 3, 10, 5]
    [8, 10, 6, 7, 6]
    [0, 1, 4, 2, 6]
    [4, 9, 5, 2, 1]
    <BLANKLINE>


    Args:
        matrix (list): Matriz donde buscar la secuencia
    """

    match_sequence = 4
    matches = list()

    for number_row, row in enumerate(matrix):
        for col in range(max_columns - (match_sequence - 1)):
            if all(row[i + 1] == row[i] + 1 for i in range(col, col + (match_sequence - 1))):
                # guardo en una tupla de tuplas, primero la fila y columna de la posicion incial, y en la segunda tupla la fila y columna de la posicion final
                matches.append(((number_row, col), (number_row, col + (match_sequence - 1))))
    
    for col in range(max_columns):
        for row in range(max_rows - (match_sequence - 1)):
            if all(matrix[i + 1][col] == matrix[i][col] + 1 for i in range(row, row + (match_sequence - 1))):
                # guardo en una tupla de tuplas, primero la fila y columna de la posicion incial, y en la segunda tupla la fila y columna de la posicion final
                matches.append(((row, col), (row + (match_sequence - 1), col)))

    if matches:
        print(f"Hay una secuencia de {match_sequence} numeros consecutivos en:")
        for item in matches:
            print(f"Primer numero fila {item[0][0] + 1} columna {item[0][1] + 1}, ultimo numero fila {item[1][0] + 1} columna {item[1][1] + 1}")
    else:
        print("No hay secuencias consecutivas en la matriz")

    print()
    print("La matriz es:")
    for row in matrix:
        print(row)
    print()
    

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
    buscar_secuencia()
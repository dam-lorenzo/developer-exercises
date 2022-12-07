from random import randint

def generar_matriz():
    max_rows = 5
    max_columns = 5
    match_sequence = 4

    matrix = list()
    for row in range(max_rows):
        matrix.append([randint(0, 10) for col in range(max_columns)])
    
    row = 0
    col = 0

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
            print(f"Primer numero fila {item[0][0]} columna {item[0][1]}, segundo numero fila {item[1][0]} columna {item[1][1]}")
    else:
        print("No hay secuencias consecutivas en la matriz")

    print()
    print("La matriz es:")
    for row in matrix:
        print(row)
    print()
    
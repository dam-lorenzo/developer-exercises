from random import randint

def generar_lista() -> list:
    """
    Genera una lista de 10 elementos de diccionarios con un "Id" y una "Edad" entre 1 y 100

    >>> all(item["Edad"] >= 1 and item["Edad"] <= 100 for item in generar_lista())
    True

    >>> all(count + 1 == item["Id"] for count, item in enumerate(generar_lista()))
    True

    >>> len(generar_lista())
    10

    Returns:
        list: lisa de dict
    """
    min_age = 1
    max_age = 100
    len_list = 10
    ages = list()

    for pos in range(len_list):
        ages.append( {
            "Id": pos + 1,
            "Edad": randint(min_age, max_age)
        } )
    
    return ages

def ordenar_lista(unordered_list: list) -> list:
    """
    Ordena de menor a mayor, segun la edad una lista. 

    Args:
        unordered_list (list): Lista de diccionarios con la key "Edad" para indicar la edad

    >>> ordenar_lista([{'Id': 1, 'Edad': 69}, {'Id': 2, 'Edad': 28}, {'Id': 3, 'Edad': 75}, {'Id': 4, 'Edad': 89}, {'Id': 5, 'Edad': 16}, {'Id': 6, 'Edad': 21}, {'Id': 7, 'Edad': 90}, {'Id': 8, 'Edad': 87}, {'Id': 9, 'Edad': 78}, {'Id': 10, 'Edad': 38}])
    [{'Id': 5, 'Edad': 16}, {'Id': 6, 'Edad': 21}, {'Id': 2, 'Edad': 28}, {'Id': 10, 'Edad': 38}, {'Id': 1, 'Edad': 69}, {'Id': 3, 'Edad': 75}, {'Id': 9, 'Edad': 78}, {'Id': 8, 'Edad': 87}, {'Id': 4, 'Edad': 89}, {'Id': 7, 'Edad': 90}]

    Returns:
        list: Copia de la lista pasada como argumento
    """
    ordered_list = unordered_list.copy()
    for i in range(len(ordered_list) - 1):
        for pos in range(len(ordered_list) - (i + 1)):
            if ordered_list[pos]["Edad"] > ordered_list[pos + 1]["Edad"]:
                aux = ordered_list[pos]
                ordered_list[pos] = ordered_list[pos + 1]
                ordered_list[pos + 1] = aux
    return ordered_list

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    ordenar_lista(generar_lista())
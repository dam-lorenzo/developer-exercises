from random import randint

def generar_lista() -> list:
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
    ordered_list = unordered_list.copy()
    for i in range(len(ordered_list) - 1):
        for pos in range(len(ordered_list) - (i + 1)):
            if ordered_list[pos]["Edad"] > ordered_list[pos + 1]["Edad"]:
                aux = ordered_list[pos]
                ordered_list[pos] = ordered_list[pos + 1]
                ordered_list[pos + 1] = aux
    return ordered_list
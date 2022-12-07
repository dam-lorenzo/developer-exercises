from Simple.simple import generar_lista, ordenar_lista
from Matriz.matriz import generar_matriz

if __name__ == '__main__':
    print(f'\n\t\t\t{"="*22}')
    print('\t\t\tDeveloper Exercises')
    print('\t\t\tDamian Lorenzo Cupeiro')
    print(f'\t\t\t{"="*22}\n')
    op = -1
    while op != '0':
        print(f'{"-"*120}')
        print('Menu:')
        print('\t1) Simple: se genera una lista con 10 elementos y se la ordena')
        print('\t2) Matriz: se genera una matriz de 5x5 con numeros aleatoreos y se busca una secuencia de 4 numeros consecutivos')
        print('\t3) Clases: accede a una clase con sus propias opciones')
        print('\t0) Con esta opcion se termina el programa')
        op = input('Ingrese su opcion: ')
        print(f'{"-"*120}\n')
        if op == '1':
            ages = generar_lista()
            ordered_ages = ordenar_lista(ages)
            print(f'Lista sin ordenar {ages}\n')
            print(f'Lista ordenada {ordered_ages}\n')
        elif op == '2':
            generar_matriz()
        elif op == '3':
            print('WIP')
        elif op == '0':
            print('Hasta luego\n')
        else:
            print('Opcion incorrecta\n')
    
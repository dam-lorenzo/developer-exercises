from Simple.simple import generar_lista, ordenar_lista
from Matriz.matriz import buscar_secuencia
from Clases.clases import Circulo

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
            buscar_secuencia()
        elif op == '3':
            op2 = -1
            rad = int(input('Ingrese el radio del circulo: '))
            try:
                circulo = Circulo(rad)
            except Exception:
                break
            while op2 != '0':
                print('Opciones')
                print('\t1) Mostrar area del circulo')
                print('\t2) Mostrar perimetro del circulo')
                print('\t3) Dibujar el circulo')
                print('\t4) Multiplicar el circulo')
                print('\t0) Para volver al menu principal')
                op2 = input('Elija una opcion: ')
                if op2 == '1':
                    area = circulo.area()
                    print(f'El area es {area}\n')
                elif op2 == '2':
                    perimetro = circulo.perimetro()
                    print(f'El perimetro es {perimetro}\n')
                elif op2 == '3':
                    circulo.dibujar_circulo()
                elif op2 == '4':
                    number = int(input('Ingrese el numero a multiplicar: '))
                    circulo2 = circulo.multiplicar(number)
                elif op2 == '0':
                    pass
                else:
                    print('Opcion incorrecta\n')
        elif op == '0':
            print('Hasta luego\n')
        else:
            print('Opcion incorrecta\n')
    
import math
import turtle

class Circulo:
    def __init__(self, radius: int) -> None:
        if radius > 0:
            self.__radius = radius
        else:
            raise(f'El radio debe ser mayor a 0, se ingreso {radius}')
    
    def area(self) -> float:
        area = math.pi * self.__radius * self.__radius
        return area

    def perimetro(self) -> float:
        perimeter = 2 * math.pi * self.__radius
        return perimeter

    def modificar_radio(self, radius: int) -> None:
        if radius > 0:
            self.__radius = radius
        else:
            print(f'El radio debe ser mayor a 0, se ingreso {radius}.')
            print('No se modifico el radio')
    
    def dibujar_circulo(self) -> None:
        turtle.circle(self.__radius)

    def multiplicar(self, number: int):
        if number > 0:
            return Circulo(self.__radius * number)
        else:
            print(f'El numero para multiplicar debe ser mayor a 0, se ingreso {number}.')
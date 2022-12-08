import math
import turtle

class Circulo:
    def __init__(self, radius: int) -> None:
        """Instancia la clase circulo siempre y cuando el radio sea mayo

        >>> Circulo(-3)
        Traceback (most recent call last):
            ...
        ValueError: El radio debe ser mayor a 0, se ingreso -3

        >>> Circulo(0)
        Traceback (most recent call last):
            ...
        ValueError: El radio debe ser mayor a 0, se ingreso 0

        Args:
            radius (int): Debe ser mayor a 0
        """
        if radius > 0:
            self.__radius = radius
        else:
            raise ValueError(f'El radio debe ser mayor a 0, se ingreso {radius}')
    
    def get_radio(self) -> int:
        return self.__radius

    def area(self) -> float:
        """
        Calcula el area del circulo, toma como valor de pi el definido en la libreria de math.

        >>> Circulo(3).area()
        28.274333882308138

        Returns:
            float: area del circulo
        """
        area = math.pi * self.__radius * self.__radius
        return area

    def perimetro(self) -> float:
        """
        Calcula el perimetro del circulo, toma como valor de pi el definido en la libreria de math.

        >>> Circulo(3).perimetro()
        18.84955592153876

        Returns:
            float: perimetro del circulo
        """
        perimeter = 2 * math.pi * self.__radius
        return perimeter

    def modificar_radio(self, radius: int) -> None:
        """
        Modifica el valor de radio del circulo

        >>> Circulo(4).modificar_radio(0)
        El radio debe ser mayor a 0, se ingreso 0.
        No se modifico el radio

        >>> Circulo(4).modificar_radio(-1)
        El radio debe ser mayor a 0, se ingreso -1.
        No se modifico el radio

        Args:
            radius (int): nuevo radio, deber ser mayor a 0
        """
        if radius > 0:
            self.__radius = radius
        else:
            print(f'El radio debe ser mayor a 0, se ingreso {radius}.')
            print('No se modifico el radio')
    
    def dibujar_circulo(self) -> None:
        """
        Dibuja el circulo usando el modulo turtle.
        """
        turtle.circle(self.__radius)

    def multiplicar(self, number: int):
        """
        genera una nueva clase circulo con el restultado de multiplicar el radio actual por numero pasado
        por argumento

        >>> Circulo(3).multiplicar(0)
        El numero para multiplicar debe ser mayor a 0, se ingreso 0.

        >>> Circulo(3).multiplicar(-1)
        El numero para multiplicar debe ser mayor a 0, se ingreso -1.

        Args:
            number (int): debe ser mayor a 0

        Returns:
            Circulo: nueva instancia de la clase circulo
        """
        if number > 0:
            return Circulo(self.__radius * number)
        else:
            print(f'El numero para multiplicar debe ser mayor a 0, se ingreso {number}.')



if __name__ == "__main__":
    import doctest
    doctest.testmod()

    circulo = Circulo(3)
    print(f'Radio del circulo {circulo.get_radio()}')
    print(f'Area del circulo {circulo.area()}')
    print(f'Perimetro del circulo {circulo.perimetro()}')
    circulo.dibujar_circulo()
    circulo.modificar_radio(5)
    print(f'Nuevo radio del circulo {circulo.get_radio()}')
    circulo2 = circulo.multiplicar(6)
    print(f'Radio del circulo 2 {circulo2.get_radio()}')
    
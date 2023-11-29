from HW.geometry.circle import Circle
from HW.geometry.rectangle import Rectangle
from HW.geometry.square import Square
from HW.geometry.triangle import Triangle

if __name__ == '__main__':

    figures = [Circle(10), Square(17), Triangle(9, 8, 3), Rectangle(80, 654)]

    for figure in figures:
        print(figure.calculator())

from src.geometry.circle import Circle
from src.geometry.rectangle import Rectangle
from src.geometry.square import Square
from src.geometry.triangle import Triangle

if __name__ == '__main__':

    figures = [Circle(10), Square(17), Triangle(9, 8, 3), Rectangle(80, 654)]

    for figure in figures:
        print(figure.calculator())

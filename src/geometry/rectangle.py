import math

from src.geometry.base_figure import BaseFigure


class Rectangle(BaseFigure):
    def __init__(self, side_a, side_b):
        self.sides = (side_a, side_b)
        self.check_args(*self.sides)

    def area(self):
        return math.prod(self.sides)

    def perimeter(self):
        return "Perimeter", 2 * sum(self.sides)

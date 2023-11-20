import math

from src.geometry.base_figure import BaseFigure


class Rectangle(BaseFigure):

    def __init__(self, side_a, side_b):
        self.sides = (side_a, side_b)
        self.check_args(*self.sides)
        self.name = f"Rectangle {side_a} and {side_b}"

    def area(self):
        return math.prod(self.sides)

    def perimeter(self):
        return 2 * sum(self.sides)

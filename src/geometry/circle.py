import math

from src.geometry.base_figure import BaseFigure


class Circle(BaseFigure):
    def __init__(self, radius):
        self.radius = radius
        self.check_args(self.radius)

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return "Circuit", 2 * math.pi * self.radius

import math

from HW.geometry.base_figure import BaseFigure


class Circle(BaseFigure):
    def __init__(self, radius):
        self.radius = radius
        self.check_args(self.radius)
        if radius < 0:
            raise ValueError(f"Невозможно создать Circle "
                             f"{self.__class__.__name__}!")
        self.name = f"Circle: radius {radius}"

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

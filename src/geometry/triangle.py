import math

from src.geometry.base_figure import BaseFigure


class Triangle(BaseFigure):
    def __init__(self, side_a, side_b, side_c):
        self.sides = (side_a, side_b, side_c)
        self.check_args(*self.sides)
        if side_a + side_b < side_c or side_a + side_c < side_b or side_c + side_b < side_a:
            raise ValueError(f"Невозможно создать триангл "
                             f"{self.__class__.__name__}!")

    def area(self):
        half_perimeter = sum(self.sides) / 2
        area = math.prod([half_perimeter] +
                         [half_perimeter - s for s in self.sides])
        return area

    def perimeter(self):
        return "Perimeter", sum(self.sides)

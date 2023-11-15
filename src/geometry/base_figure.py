import abc


class BaseFigure(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def area(self):
        pass

    @abc.abstractmethod
    def perimeter(self):
        pass

    def calculator(self):
        result = self.perimeter()
        return f"{result[0]} is: {round(result[1], 3)}" \
               f"\nArea is: {round(self.area(), 3)}"

    def add_area(self, other_figure):
        if not isinstance(other_figure, BaseFigure):
            raise ValueError
        return self.area() + other_figure.area()

    def check_args(self, *args):
        for side in args:
            if type(side) not in (int, float):
                raise ValueError(f"Неправильный тип данных для "
                                 f"{self.__class__.__name__}!")

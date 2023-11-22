from src.geometry.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, side_a, side_b=None):
        if side_b is None:
            side_b = side_a
        self.check_args(side_a, side_b)
        if side_a != side_b:
            raise ValueError(f"Это не квадрат"
                             f"{self.__class__.__name__}!")
        side = min(side_a, side_b)
        super().__init__(side, side)
        self.name = f"Square {side}"

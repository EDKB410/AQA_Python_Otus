from src.geometry.rectangle import Rectangle
from src.geometry.circle import Circle
from src.geometry.square import Square
from src.geometry.triangle import Triangle

import pytest


@pytest.mark.parametrize(("side_a", "side_b", "area"),
                         [(5, 10, 50)])
def test_sum_fiure(side_a, side_b, area):
    rec = Rectangle(side_a, side_b)
    cir = Circle(radius=side_a)
    assert rec.add_area(cir) == rec.area() + cir.area()


@pytest.mark.parametrize(("side_a", "side_b", "area", "perimeter"),
                         [(-4, -6, 24, -20),
                          (0, 0, 0, 0),
                          (4, 6, 24, 20),
                          (5, 10, 50, 30)])
def test_rectangle(side_a, side_b, area, perimeter):
    r = Rectangle(side_a, side_b)
    assert r.name == f"Rectangle {side_a} and {side_b}"
    assert r.area() == area
    assert r.perimeter() == perimeter


@pytest.mark.parametrize(("side_a", "side_b"),
                         [(15, False),
                          ("15", 16)])
def test_rectangle_negative(side_a, side_b):
    with pytest.raises(ValueError):
        Rectangle(side_a, side_b)

@pytest.mark.parametrize(("side_a", "area", "perimeter"),
                         [(4, 16, 16),
                          (5, 25, 20)])
def test_square(side_a, area, perimeter):
    sqr = Square(side_a)
    assert sqr.name == f"Square {side_a}"
    assert sqr.area() == area
    assert sqr.perimeter() == perimeter


@pytest.mark.parametrize(("side_a", "side_b"),
                         [(10, 1),
                          (15, False),
                          (15, "15")])
def test_square_negative(side_a, side_b):
    with pytest.raises(ValueError):
        Square(side_a, side_b)

@pytest.mark.parametrize(("side_a", "side_b", "side_c", "area", "perimeter"),
                         [(4, 6, 8, 135, 18),
                          (5, 10, 10, 585.9375, 25)])
def test_triangle(side_a, side_b, side_c, area, perimeter):
    tri = Triangle(side_a, side_b, side_c)
    assert tri.name == f"Triangle {side_a} X {side_b} X {side_c}"
    assert tri.area() == area
    assert tri.perimeter() == perimeter


@pytest.mark.parametrize(("side_a", "side_b", "side_c"),
                         [(4, 6, 11),
                          (5, 16, 10),
                          (15, 6, 8),
                          (15, 1, False),
                          (15, "10", 8)])
def test_triangle_negtive(side_a, side_b, side_c):
    with pytest.raises(ValueError):
        Triangle(side_a, side_b, side_c)


@pytest.mark.parametrize(("radius", "area", "perimeter"),
                         [(1, 3.141592653589793, 6.283185307179586)])
def test_circle(radius, area, perimeter):
    cir = Circle(radius)
    assert cir.name == f"Circle: radius {radius}"
    assert cir.area() == area
    assert cir.perimeter() == perimeter


@pytest.mark.parametrize("radius",
                         [(-1), "1", True])
def test_circle_negative(radius):
    with pytest.raises(ValueError):
        Circle(radius)

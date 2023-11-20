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


@pytest.mark.parametrize(("side_a", "side_b", "area", "perimeter"),
                         [(5, 5, 5, 5),
                          (2, 2, -2, -2)])
def test_rectangle_negative(side_a, side_b, area, perimeter):
    rec = Rectangle(side_a, side_b)
    assert rec.area() != area
    assert rec.perimeter() != perimeter


@pytest.mark.parametrize(("side_a", "area", "perimeter"),
                         [(4, 16, 16),
                          (5, 25, 20)])
def test_square(side_a, area, perimeter):
    sqr = Square(side_a)
    assert sqr.name == f"Square {side_a}"
    assert sqr.area() == area
    assert sqr.perimeter() == perimeter

@pytest.mark.parametrize(("side_a", "area", "perimeter"),
                         [(10, 10, 10),
                          (-5, -5, -5)])
def test_square_negtive(side_a, area, perimeter):
    sqr = Square(side_a)
    assert sqr.name == f"Square {side_a}"
    assert sqr.area() != area
    assert sqr.perimeter() != perimeter

@pytest.mark.parametrize(("side_a", "side_b", "side_c", "area", "perimeter"),
                         [(4, 6, 8, 135, 18),
                          (5, 10, 10, 585.9375, 25)])
def test_triangle(side_a, side_b, side_c, area, perimeter):
    tri = Triangle(side_a, side_b, side_c)
    assert tri.name == f"Triangle {side_a} X {side_b} X {side_c}"
    assert tri.area() == area
    assert tri.perimeter() == perimeter

@pytest.mark.parametrize(("side_a", "side_b", "side_c", "area", "perimeter"),
                         [(4, 6, 8, 130, 1),
                          (5, 10, 10, 586, 20)])
def test_triangle_negtive(side_a, side_b, side_c, area, perimeter):
    tri = Triangle(side_a, side_b, side_c)
    assert tri.area() != area
    assert tri.perimeter() != perimeter


@pytest.mark.parametrize(("radius", "area", "perimeter"),
                         [(1, 3.141592653589793, 6.283185307179586)])
def test_circle(radius, area, perimeter):

    cir = Circle(radius)
    assert cir.name == f"Circle: radius {radius}"
    assert cir.area() == area
    assert cir.perimeter() == perimeter

@pytest.mark.parametrize(("radius", "area", "perimeter"),
                         [(1, 1, 1)])
def test_circle_negative(radius, area, perimeter):

    cir = Circle(radius)
    assert cir.area() != area
    assert cir.perimeter() != perimeter
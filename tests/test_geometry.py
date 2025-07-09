import pytest
import numbers
from geometry import Square, Circle
from geometry.utils import area_stats
import math
def test_area_zero_and_positive():
    test_square = Square(1.5493)
    test_zero = Square(0)
    test_circle = Circle(4013.38293)
    test_circle_zero = Circle(0)
    assert test_square.area() == pytest.approx(2.40033049)
    assert test_zero.area() == pytest.approx(0)
    assert test_circle.area() == pytest.approx(math.pi * 4013.38293**2)
    assert test_circle_zero.area() == pytest.approx(0)

def test_stats_keys_and_values():
    s1 = Square(41309)
    s2 = Square(0.24)
    s3 = Square(1)
    c1 = Circle(134089)
    c2 = Circle(0.241389)
    c3 = Circle(0)
    d = area_stats(s1, s2, s3, c1, c2, c3)
    assert isinstance(d, dict)
    for i in d.keys():
        assert i in ["n", "total", "mean", "min","max"]
    for i in d.values():
        assert isinstance(i, numbers.Number)

def test_stats_empty_list():
    with pytest.raises(ValueError):
        area_stats()
        
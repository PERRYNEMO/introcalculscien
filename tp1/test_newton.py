import math

from tp1.newton import bisection, newton


def test_newton():
    square = lambda x: x ** 2 - 2
    dsquare = lambda x: 2 * x
    assert newton(square, dsquare, 1) - math.sqrt(2) < 1e-16
    assert -math.sqrt(2) - newton(square, dsquare, -1) < 1e-16
    assert bisection(square, 0, 4) - math.sqrt(2) < 1e-16
    assert bisection(square, 4, 0) - math.sqrt(2) < 1e-16

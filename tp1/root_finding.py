"""

"""
import math

from tp1.newton import bisection, find_root_best, Function


def get_gb(b):
    return lambda a: (b ** 2) * (math.exp(a) + a ** 3) - a ** 2 - 4 * a


def get_derivative_gb(b):
    return lambda a: (b ** 2) * (math.exp(a) + 3 * a ** 2) - 2 * a - 4


def get_second_derivative_gb(b):
    return lambda a: (b ** 2) * (math.exp(a) + 6 * a) - 2


def get_third_derivative_gb(b):
    return lambda a: (b ** 2) * (math.exp(a) + 6)


def h(b):
    if abs(b) > 0.5:
        return find_root_best(get_derivative_gb(b), get_second_derivative_gb(b),
                              0, 4)
    second_derivative_root = find_last_root(b, 0, get_second_derivative_gb(b),
                                            get_third_derivative_gb(b))
    return find_last_root(b, second_derivative_root, get_derivative_gb(b),
                          get_second_derivative_gb(b))




def find_last_root(b, x0, f, df, max_iter=100):
    n = 0
    k = math.log(1 / b) * 0.1
    fx0 = f(x0)
    tk = 100
    ftk = f(tk)
    while ftk * fx0 > 0 and n <= max_iter:
        try:
            tk = x0 + k - f(k + x0) / df(k + x0)
        except:
            k /= 1.05
        try:
            ftk = f(tk)
        except:
            k *= 1.1
        n = n + 1
        k /= 1.05
    if n > max_iter:
        raise ValueError("x0 too high")
    return find_root_best(f, df, x0, tk)


def find_b_star():
    return bisection(lambda b: get_gb(b)(h(b)), 1, 1.5)


b_star = find_b_star()


def continu(b):
    if b == 0:
        return -4, 0

    a1 = find_root_best(get_gb(b), get_derivative_gb(b), -6, 0)

    if abs(b) > b_star:
        return a1
    if abs(b) == b_star:
        return a1, h(b)
    hb = h(b)
    a2 = find_root_best(get_gb(b), get_derivative_gb(b), -0.5, hb)
    a3 = find_last_root(b, hb, get_gb(b), get_derivative_gb(b))
    return a1,a2,a3

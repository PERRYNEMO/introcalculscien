"""

"""
import math
from tp1.newton import newton, bisection

def good_for_newton_condition(f, df):
    def tang_are_good(a, b):
        if a == b:
            raise ValueError()
        if a > b:
            a, b = b, a
        if df(a)==0 or df(b)==0:
            return False
        ta = a - f(a) / df(a)
        tb = b - f(b) / df(b)
        if a < ta < b and a < tb < b:
            return True
        return False
    return tang_are_good

def get_gb(b):
    return lambda a: (b ** 2) * (math.exp(a) + a ** 3) - a ** 2 - 4 * a


def get_derivative_gb(b):
    return lambda a: (b ** 2) * (math.exp(a) + 3 * a ** 2) - 2 * a - 4


def get_second_derivative_gb(b):
    return lambda a: (b ** 2) * (math.exp(a) + 6 * a) - 2

def get_third_derivative_gb(b):
    return lambda a: (b ** 2) * (math.exp(a) + 6 )


def h(b):
    if b>0.5:
        return find_root_best(get_derivative_gb(b), get_second_derivative_gb(b), 0, 4)
    second_derivative_root = find_last_root(b, 0, get_second_derivative_gb(b), get_third_derivative_gb(b))
    return find_last_root(b, second_derivative_root, get_derivative_gb(b), get_second_derivative_gb(b))

def find_root_best(f, df, a, b):
    x = bisection(f, a, b, good_for_newton_condition(f, df))
    return newton(f, df, x)

def find_last_root(b,x0,f, df, max_iter=10000):
    n = 0
    k = 0.1
    fx0 = f(x0)
    while f(x0+k)*fx0>0 and n <= max_iter:
        n = n + 1
        k+=0.1
    if n>max_iter:
        raise ValueError("x0 too high")
    return find_root_best(f, df, x0, x0+k)

def find_b_star():
    return bisection(lambda b: get_gb(b)(h(b)), 1, 1.5)
b_star = find_b_star()
def continu(b):
    if b == 0:
        return -4,0

    a1 = find_root_best(get_gb(b), get_derivative_gb(b), -6, 0)

    if b>b_star:
        return a1
    if b==b_star:
        return a1, h(b)
    a2 = find_root_best(get_gb(b), get_derivative_gb(b), -0.5, h(b))
    a3 = find_last_root(b, h(b), get_gb(b), get_derivative_gb(b))
    return a1, a2, a3
print(continu(0.00000000000000000000000000000000000000000000000000000000001))

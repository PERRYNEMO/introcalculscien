"""
Calculate the value of a and b for which the function is continuous
"""
import math

from tp1.newton import bisection, find_root_best, Function


def get_gb(b: float) -> Function:
    """get gb

    :param b:  parameter
    :return: the function gb
    """
    return lambda a: (b ** 2) * (math.exp(a) + a ** 3) - a ** 2 - 4 * a


def get_derivative_gb(b: float) -> Function:
    """get derivative of gb

    :param b:  parameter
    :return: the derivative of gb
    """
    return lambda a: (b ** 2) * (math.exp(a) + 3 * a ** 2) - 2 * a - 4


def get_second_derivative_gb(b: float) -> Function:
    """get second derivative of gb

    :param b:  parameter
    :return: the second derivative of gb
    """
    return lambda a: (b ** 2) * (math.exp(a) + 6 * a) - 2


def get_third_derivative_gb(b: float) -> Function:
    """get third derivative of gb

    :param b:  parameter
    :return: the third derivative of gb
    """
    return lambda a: (b ** 2) * (math.exp(a) + 6)


def h(b: float) -> float:
    """it is the function that at each b reel associate the min of the function
    gb in the positif

    :param b:  parameter
    :return: the minimum of gb in positif

    :raise ValueError: if the function is not defined
    """
    if abs(b) > 2:
        raise ValueError('b there is no minimum, the function is not defined')
    if abs(b) > 0.5:
        return find_root_best(get_derivative_gb(b), get_second_derivative_gb(b),
                              0, 4)
    second_derivative_root = find_last_root(b, 0, get_second_derivative_gb(b),
                                            get_third_derivative_gb(b))
    return find_last_root(b, second_derivative_root, get_derivative_gb(b),
                          get_second_derivative_gb(b))


def find_last_root(b: float, x0: float, f: Function, df: Function,
                   max_iter: int = 100) -> float:
    """calculate the root of the function, the only thing we know is
    the derivative is croissant, the derivative of x0 is positive, and there is
    one root between x0 and + infinity

    :param b: parameter
    :param x0: the starting value
    :param f: the function that we want to find the root
    :param df: the derivative of f
    :param max_iter: maximum iterations
    :return: the root of the function

    :raise ValueError: if the function gb do an overflow at the root
    """
    n: int = 0
    k: float = math.log(1 / b) * 0.1
    fx0: float = f(x0)
    tk: float = 100
    ftk: float = f(tk)
    while ftk * fx0 > 0 and n <= max_iter:
        try:
            tk = x0 + k - f(k + x0) / df(k + x0)
        except OverflowError:
            k /= 1.05
        try:
            ftk = f(tk)
        except OverflowError:
            k *= 1.1
        n = n + 1
        k /= 1.05
    if n > max_iter:
        raise ValueError("we can not find the interval, probably "
                         "the root is to high, the limit for the exp is 710")
    return find_root_best(f, df, x0, tk)


def find_b_star():
    """ find when there is only one root of gb on positif

    :return: the value of b when the root of gb and his derivative are the same
    """
    return bisection(lambda b: get_gb(b)(h(b)), 1, 1.5)


b_star = find_b_star()


def continu(b: float) -> list[float]:
    """calculate the value of a for a b for which the function is continuous
    so the root of gb

    :param b: parameter
    :return: the list of the roots
    """
    if b == 0:
        return [-4, 0]

    a1: float = find_root_best(get_gb(b), get_derivative_gb(b), -6, 0)

    if abs(b) > b_star:
        return [a1]
    if abs(b) == b_star:
        return [a1, h(b)]
    hb: float = h(b)
    a2: float = find_root_best(get_gb(b), get_derivative_gb(b), -0.5, hb)
    a3: float = find_last_root(b, hb, get_gb(b), get_derivative_gb(b))
    return [a1, a2, a3]

""" implementing the newton and bisection algorithm"""
import math
from typing import Callable


def relative_error_condition(eps: float = 1e-16, delta: float = 1e-16) \
        -> Callable[[float, float], bool]:
    """create relative error function

    :param eps: relative precision (if a and b are big)
    :param delta: absolute precision (if a and b are close to 0)
    :return: lamda function that tells if a and b are close enough
    """
    return lambda a,b:abs(b-a)<eps*(abs(a)+abs(b))+delta

def absolute_error_condition(eps: float= 1e-16) \
        -> Callable[[float, float], bool]:
    """create absolute error condition function

    :param eps: precision
    :return: lamda function that tells if a and b are close enough
    """
    return lambda a,b:abs(b-a)<eps



def newton(
        f: Callable[[float], float],
        df: Callable[[float], float], x0: float,
        stop_condition : Callable[[float, float], bool] = relative_error_condition(),
        max_iter: int=100
) -> float:
    """find the root of a function using Newton's method

    :param f: The function for which the root is sought
    :param df: The derivative of the function f
    :param x0: Initial guess for the root.
    :param stop_condition: a function that tells if we can stop with a good precision
    :param max_iter: Maximum number of iterations (default is 100)
    :return: The computed root

    :raises ValueError: if x0 is finite, if f(x) or f/'(x) is not defined ,
    If the derivative is too close to zero, indicating a
    risk of divergence.
    :raises RuntimeError: If the maximum number of iterations is reached
    without convergence.
    """
    if not math.isfinite(x0):
        raise ValueError("x0 is not finite")
    x=x0
    n = 0
    while not stop_condition(x, x0) and n <= max_iter:
        n +=1
        fx=f(x)
        dfx=df(x)
        if not math.isfinite(fx):
            raise ValueError('f is not defined at '+x)
        if not math.isfinite(dfx):
            raise ValueError('f derivative is not defined at '+x)
        if abs(dfx)<1e-12:
            raise ValueError("f derivative to small at "+x+" newton did not converge")
        x0 = x
        x = x - fx/dfx
    if n <= max_iter:
        return x
    raise RuntimeError("Newton did not converge")


def bisection(
        f: Callable[[float], float],
        a: float, b: float, stop_condition=relative_error_condition(), max_iter=100
) -> float:
    """find the root of a function using Bisection method

    :param f: The function for which the root is sought
    :param a: first bound of interval
    :param b: second bound of interval
    :param stop_condition: a function that tells if we can stop with a good precision
    :param max_iter: maximum number of iterations (default is 100)
    :return: computed root

    :raises ValueError: if a and b are not finite, if the sign of a and b are not different,
    if f(x) is not defined
    :raises RuntimeError: If the maximum number of iterations is reached
    """
    if not math.isfinite(a):
        raise ValueError("a is not finite")
    if not math.isfinite(b):
        raise ValueError("b is not finite")
    fa= f(a)
    if fa*f(b)>0:
        raise ValueError('sign of f(a) and f(b) are not different')
    if fa<0:
        a, b = b, a
    n = 0
    while not stop_condition(a, b) and n<=max_iter:
        n+=1
        x = (a+b)/2
        fx = f(x)
        if not math.isfinite(fx):
            raise ValueError('f is not defined at '+x)
        if fx>0:
            a = x
        elif fx<0:
            b = x
        else:
            return x
    if n<=max_iter:
        return (a + b) / 2
    raise RuntimeError('bisection takes too long')

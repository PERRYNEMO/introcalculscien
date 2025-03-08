""""""
import math
from typing import Callable


def relative_error(eps: float = 1e-16, delta: float = 1e-16) \
        -> Callable[[float, float], bool]:
    """create relative error function

    :param eps: relative precision (if a and b are big)
    :param delta: absolute precision (if a and b are close to 0)
    :return: lamda function that tells if a and b are close enough
    """
    return lambda a,b:abs(b-a)<eps*(abs(a)+abs(b))+delta

def absolute_error(eps: float= 1e-16) \
        -> Callable[[float, float], bool]:
    """create absolute error function

    :param eps: precision
    :return: lamda function that tells if a and b are close enough
    """
    return lambda a,b:abs(b-a)<eps



def newton(
        f: Callable[[float], float],
        df: Callable[[float], float], x0: float,
        stop_condition : Callable[[float, float], bool] = relative_error(),
        max_iter: int=100
) -> float:
    """find the root of a function using Newton's method

    :param f: The function for which the root is sought
    :param df: The derivative of the function f
    :param x0: Initial guess for the root.
    :param stop_condition: a function that tells if a and b are close enough
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


def bisection(f, a, b, stop_condition=relative_error(), max_iter=100):
    if not math.isfinite(a):
        raise AssertionError("a is not finite")
    if not math.isfinite(b):
        raise AssertionError("b is not finite")
    fa= f(a)
    if fa*f(b)>0:
        raise Exception('bisection failed')
    if fa<0:
        a, b = b, a
    n = 0
    while not stop_condition(a, b) and n<=max_iter:
        n+=1
        x = (a+b)/2
        fx = f(x)
        if not math.isfinite(fx):
            raise Exception('f is not defined at '+x)
        if fx>0:
            a = x
        elif fx<0:
            b = x
        else:
            return x
    if n<=max_iter:
        return (a + b) / 2
    raise Exception('bisection failed')

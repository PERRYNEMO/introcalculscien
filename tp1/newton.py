""""""
import math
from typing import *


def relative_error(eps=1e-16, delta=1e-16):
    return lambda a,b:abs(b-a)<eps*(abs(a)+abs(b))+delta

def absolute_error(eps=1e-16):
    return lambda a,b:abs(b-a)<eps

def newton(f, df, x0, stop_condition=relative_error(), max_iter=100):
    if not math.isfinite(x0):
        raise AssertionError("x0 is not finite")
    x=x0
    n = 0
    while not stop_condition(x, x0) and n <= max_iter:
        n +=1
        fx=f(x)
        dfx=df(x)
        if not math.isfinite(fx):
            raise AssertionError('f is not defined at '+x)
        if not math.isfinite(dfx):
            raise AssertionError('f derivative is not defined at '+x)
        if abs(dfx)<1e-12:
            raise AssertionError("f derivative to small at "+x+" newton did not converge")
        x0 = x
        x = x - fx/dfx
    if n <= max_iter:
        return x
    raise Exception("Newton did not converge")


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

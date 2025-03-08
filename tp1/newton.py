""""""

def relative_error(eps=1e-16, delta=1e-16):
    return lambda a,b:abs(b-a)<eps*(abs(a)+abs(b))+delta

def absolute_error(eps=1e-16):
    return lambda a,b:abs(b-a)<eps

def newton(f, df, x0, stop_condition=relative_error(), max_iter=100):
    x=x0
    for i in range(max_iter):
        fx=f(x)
        dfx=df(x)
        x0 = x
        x = x - fx/dfx
        if stop_condition(x, x0):
            return x
    return x


def bisection(f, a, b, stop_condition=relative_error(), max_iter=100):
    fa= f(a)
    if fa*f(b)>0:
        raise Exception('bisection failed')
    if fa<0:
        a, b = b, a
    n = 0
    while not stop_condition(a, b) and n<max_iter:
        n+=1
        x = (a+b)/2
        fx = f(x)
        if fx>0:
            a = x
        elif fx<0:
            b = x
        else:
            return x
    return (a+b)/2

def newton(f, df, x0, eps=1e-16, delta=1e-16, max_iter=100):
    x=x0
    for i in range(max_iter):
        fx=f(x)
        dfx=df(x)
        x0 = x
        x = x - fx/dfx
        if abs(x0-x)<eps*(abs(x)+abs(x0))+delta:
            return x
    return x


def bisection(f, a, b, eps=1e-16, delta=1e-16, max_iter=100):
    fa =f(a)
    n = 0
    while abs(b-a)>eps*(abs(a)+abs(b))+delta and n<max_iter:
        n+=1
        x = (a+b)/2
        fx = f(x)
        if fx*fa>0:
            a = x
        elif fx*fa<0:
            b = x
        else:
            return x
    return (a+b)/2

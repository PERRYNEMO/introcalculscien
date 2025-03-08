
def newton(f, df, x0, eps=1e-16, delta=1e-16, max_iter=100):
    x=x0
    for i in range(max_iter):
        fx=f(x)
        dfx=df(x)
        x0 = x
        x = x - fx*dfx/dfx
        if abs(x0-x)<eps*(abs(x)+abs(x0))+delta:
            return x
    return x

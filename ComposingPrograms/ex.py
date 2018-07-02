def improve(close, update, guess=1):
    while not close(guess):
        guess = update(guess)
    return guess
def approx_eq(x, y, tolerance=0.0001):
    return abs(x-y)<tolerance

def newton(f, df):
    def update(x):
        return x - f(x)/df(x)

    def close(x):
        return approx_eq(f(x),0);

    return improve(close, update)


def square_root_newton():
    def f(x):
        return x * x - 2;
    def df(x):
        return 2 * x;
    return newton(f,df)

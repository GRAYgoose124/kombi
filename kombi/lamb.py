def alpha_convert(f, x, y):
    if x == y:
        return f
    else:
        return lambda z: f(z) if z != x else y


def beta_reduce(f, x, y):
    return f(x) if x == y else f

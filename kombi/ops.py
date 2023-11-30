import inspect, sys
import operator
from typing import Optional


def identity(x):
    return x


def reduce[T](f: callable, xs: list[callable], init: Optional[callable] = None):
    """educational reduce impl"""
    if init is None:
        init = xs[0]
        xs = xs[1:]
    for x in xs:
        init = f(init, x)

    return init


def compose(*functions):
    return reduce(lambda f, g: lambda *args: f(g(*args)), functions, identity)


def pipe(*functions):
    return compose(*reversed(functions))


def split(f, g):
    return lambda *args: (f(*args), g(*args))


def duplicate(f):
    return split(f, f)


def map1(f):
    return lambda xs: [f(x) for x in xs]


def map2(f):
    return lambda xs: map(f, xs)


def starmap1(f):
    return lambda xs: [f(*x) for x in xs]


def chain(*xs):
    return [x for x in xs]


def interleave(*iterables):
    chain(*zip(*iterables))


__all__ = [
    t[0]
    for t in inspect.getmembers(
        sys.modules[__name__], lambda x: inspect.isfunction(x) or inspect.isclass(x)
    )
]

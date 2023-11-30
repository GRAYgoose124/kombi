import functools
import itertools
import operator


__all__ = ["compose", "pipe"]


def identity(x):
    return x


def compose(*functions):
    return functools.reduce(lambda f, g: lambda x: f(g(x)), functions, identity)


def pipe(*functions):
    return compose(*reversed(functions))

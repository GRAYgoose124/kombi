import inspect
import itertools

from typing import List, Type


def check_annotations(a, b):
    if a == b:
        return True
    if a == inspect._empty or b == inspect._empty:
        return True


def get_methods(cls):
    methods = {
        name: method
        for name, method in inspect.getmembers(cls, predicate=inspect.ismethod)
    }
    return methods


def compare_argument_signature_to_return(f, g):
    f_sig = inspect.signature(f)
    g_sig = inspect.signature(g)

    if len(g_sig.parameters) == 1:
        return check_annotations(
            f_sig.return_annotation, next(iter(g_sig.parameters.values())).annotation
        )
    elif len(g_sig.parameters) > 1:
        return check_annotations(
            f_sig.return_annotation,
            tuple(p.annotation for p in g_sig.parameters.values()),
        )


def is_sublist(a, b):
    if len(a) > len(b):
        return False
    return any(b[i : i + len(a)] == a for i in range(len(b) - len(a) + 1))


def compatible_functions(functions: List[Type]) -> List[str]:
    chains = []

    for f, g in itertools.combinations(functions, 2):
        if compare_argument_signature_to_return(f, g):
            chains.append([f, g])

    for chain in chains:
        while True:
            extended = False
            for h in functions:
                if compare_argument_signature_to_return(chain[-1], h):
                    chain.append(h)
                    extended = True
            if not extended:
                break

    chains.sort(key=len, reverse=True)
    i = 0
    while i < len(chains):
        chain = chains[i]
        chains = [c for c in chains if c == chain or not is_sublist(c, chain)]
        i += 1

    return chains


def to_strs(chains, delims=(" -> ", "\n")):
    return delims[1].join(delims[0].join(f.__name__ for f in chain) for chain in chains)


def compatible_methods(classes: List[Type], display=False) -> List[str]:
    all_methods = []
    for cls in classes:
        all_methods.extend(get_methods(cls()).values())

    chains = compatible_functions(all_methods)

    if display:
        print(to_strs(chains))

    return chains

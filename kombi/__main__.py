from .compat import *
from .infer import *
from .ops import *


class A:
    def method1(self) -> int:
        pass

    def method2(self, arg: int) -> (str, int):
        return "a", 1


class B:
    def method3(self, arg: int) -> str:
        pass

    def method4(self, a: str, b: int) -> str:
        return a * b


def main():
    """ """
    compose(
        print,
        pipe(
            lambda x: x + 1,
            lambda x: x * 2,
            lambda x: x**2,
        ),
    )(1)

    compatible_methods([A, B], display=True)


if __name__ == "__main__":
    main()

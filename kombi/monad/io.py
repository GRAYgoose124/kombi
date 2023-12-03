from .base import Monad


class IO(Monad):
    def __init__(self, action):
        super().__init__(action)

    def __str__(self):
        return f"IO({self.value})"


@IO.wrap
def get_line():
    return input("Enter something: ")


@IO.wrap
def to_uppercase(text):
    return text.upper()

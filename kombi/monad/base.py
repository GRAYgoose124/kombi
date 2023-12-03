from functools import wraps


class MonadicFunction:
    def __init__(self, monad, function):
        self.monad = monad
        self.function = function

    def __rshift__(self, other):
        if self.monad == other.monad:

            def composed_function(*args, **kwargs):
                # First, execute the function and ensure it returns a monad
                first_result = self.function(*args, **kwargs)
                if not isinstance(first_result, Monad):
                    first_result = self.monad.unit(first_result)
                # Then bind the second function to the result
                return first_result >> other.function

            return MonadicFunction(monad=self.monad, function=composed_function)
        else:
            raise TypeError("Cannot compose functions of different monads.")

    def __call__(self, *args, **kwargs):
        # Call the function and ensure it returns a monad
        result = self.function(*args, **kwargs)
        if not isinstance(result, Monad):
            return self.monad.unit(result)
        return result


class Monad:
    def __init__(self, value):
        self.value = value

    @classmethod
    def unit(cls, value):
        return cls(value)

    def __rshift__(self, bind_function):
        return bind_function(self.value)

    def __call__(self):
        # Execute the action and return its result
        if callable(self.value):
            return self.value()
        return self.value

    @classmethod
    def wrap(cls, func):
        return wraps(func)(MonadicFunction(monad=cls, function=func))

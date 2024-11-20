from typing import Callable, Any


def strict(func) -> Callable:
    def wrapper(*args, **kwargs):
        annotations_types = func.__annotations__
        for name, value in zip(annotations_types, args):
            if not isinstance(value, annotations_types[name]):
                raise TypeError
        return func(*args, **kwargs)
    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


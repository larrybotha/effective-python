import random
from collections import defaultdict
from functools import wraps
from itertools import repeat
from random import shuffle


def _print_fn(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        fn_name = fn.__name__.replace("_", " ")
        indent = 2
        div = "".join(repeat("=", len(fn_name) + indent * 2))
        title = "\n".join([div, f"{''.join(repeat(' ', indent))}{fn_name}", div])
        print(title)
        fn(*args, **kwargs)
        print("\n")

    return wrapper


@_print_fn
def _sort_by_length():
    def repeated_string(value: str, n: int, /) -> str:
        return "".join(repeat(value, n))

    xs = [
        repeated_string("a", random.randint(0, x))
        for x in range(0, random.randint(0, 12))
    ]
    shuffle(xs)

    print(f"xs: {xs}\n")

    print("sort using key=len")
    xs.sort(key=len)
    print(f"xs: {xs}")


@_print_fn
def _defaultdict_with_side_effect():
    def side_effect_default():
        print("dict is missing value!")
        return 0

    my_base_object = {"a": 1, "b": 2}
    my_object = defaultdict(side_effect_default, my_base_object)

    print(f"my_object: {repr(my_object)}")
    xs = ["a", "b", "c", "d"]

    for name in xs:
        print(f"my_object[{name}]: {my_object[name]}")


@_print_fn
def _defaultdict_side_effect_in_closure():
    count = 0

    def my_side_effect_closure():
        nonlocal count
        count = count + 1

        return 0

    my_base_object = {"a": 1, "b": 2}
    my_object = defaultdict(my_side_effect_closure, my_base_object)
    xs = ["a", "b", "c", "d"]

    print(f"my_object: {my_object}")
    print(f"xs: {xs}")

    for name in xs:
        print(f"my_object[{name}]: {my_object[name]}")

    print(f"number of missing keys: {count}")


@_print_fn
def _defaultdict_side_effect_in_class():
    class DefaultDictMissing:
        def __init__(self):
            self.count = 0

        def missing(self):
            self.count = self.count + 1
            return 0

    default_dict_missing_thing = DefaultDictMissing()
    my_base_object = {"a": 1, "b": 2}
    my_object = defaultdict(default_dict_missing_thing.missing, my_base_object)
    xs = ["a", "b", "c", "d"]

    print(f"my_object: {my_object}")
    print(f"xs: {xs}")

    for name in xs:
        print(f"my_object[{name}]: {my_object[name]}")

    print(f"number of missing keys: {default_dict_missing_thing.count}")


@_print_fn
def _defaultdict_side_effect_in_callable_class():
    class MissingCounter:
        def __init__(self):
            self.count = 0

        def __call__(self):
            self.count = self.count + 1

            return 0

    missing_counter = MissingCounter()
    my_base_object = {"a": 1, "b": 2}
    my_object = defaultdict(missing_counter, my_base_object)
    xs = ["a", "b", "c", "d"]

    print(f"my_object: {my_object}")
    print(f"xs: {xs}")

    for name in xs:
        print(f"my_object[{name}]: {my_object[name]}")

    print(f"number of missing keys: {missing_counter.count}")


@_print_fn
def _callable_builtin():
    def my_func():
        pass

    class MyCallable:
        def __call__():
            pass

    my_callable = MyCallable()
    string_1 = "callable(my_func)"
    string_2 = "callable(my_callable)"

    xs = [string_1, string_2]

    for x in xs:
        print(f"{x}: {eval(x)}\n")


if __name__ == "__main__":
    _sort_by_length()
    _defaultdict_with_side_effect()
    _defaultdict_side_effect_in_closure()
    _defaultdict_side_effect_in_class()
    _defaultdict_side_effect_in_callable_class()
    _callable_builtin()

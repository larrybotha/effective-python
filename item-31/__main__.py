import os
from collections.abc import Iterator
from inspect import stack
from typing import Callable, Iterable, Optional


def _cr():
    print("")


def _div(text: Optional[str] = "", print_caller: bool = True):
    fn_name = stack()[1][3] if print_caller else None

    print("================")

    if text or fn_name:
        print(text or fn_name)
        _div(print_caller=False)


def _get_path(filename: str):
    return f"{os.path.dirname(__file__)}/{filename}"


class _MyFileIterable:
    def __init__(self, path: str):
        self.path = path

    def __iter__(self):
        with open(self.path, "r") as file_handle:
            for line in file_handle:
                yield line

        file_handle.close()


def _beware_of_consuming_an_iterator_twice():
    _div()

    def my_gen(length: int = 3):
        for i in range(length):
            yield i

    def do_something(xs: Iterable):
        # sum will consume the iterator, leaving us with no more values
        total = sum(xs)
        percentages = []

        for x in xs:
            percentages.append(x / xs * 100)

        return total, percentages

    iterator = my_gen(5)
    total, percentages = do_something(iterator)
    print(f"total: {total}")
    print(f"percentages: {percentages}\n ^ empty because iterator was consumed in sum")

    _cr()


def _pass_generator_in_as_lambda():
    _div()

    def my_gen(length: int = 3):
        for x in range(length):
            yield x

    def do_something(gen: Callable):
        total = sum(gen())
        percentages = []

        for x in gen():
            percentages.append(x / total * 100)

        return total, percentages

    string = "do_something(lambda: my_gen(5))"
    print(f"using lambda: {string}")
    total, percentages = do_something(lambda: my_gen(5))
    print(f"total: {total}")
    print(f"percentages: {percentages}")

    _cr()


def _use_class_to_iterate():
    _div()

    def do_something(iter: Iterable):
        xs = [int(x) for x in iter]
        total = sum(xs)
        percentages = []

        for x in iter:
            normalized = int(x)
            percentages.append(normalized / total * 100)

        return total, percentages

    path = _get_path("example.txt")
    my_iterable = _MyFileIterable(path)

    string = "do_something(my_iterable)"
    print(f"using iterable class: {string}")
    total, percentages = do_something(my_iterable)
    print(f"total: {total}")
    print(f"percentages: {percentages}")
    print("this new iterable will result in a file being read twice, however")

    _cr()


def _raise_if_iterator_with_comparison():
    _div()

    def my_gen(length: int = 3):
        for x in range(length):
            yield x

    def do_something_defensively(xs, /):
        if iter(xs) == xs:
            raise TypeError("Iterator not allowed as argument")
        total = sum(xs)
        percentages = []

        for x in xs:
            percentages.append(x / total * 100)

        return total, percentages

    it = my_gen(5)
    try:
        total, percentages = do_something_defensively(it)
    except TypeError:
        print("rejects iterator\n")

    xs = list(range(5))
    print(f"accepts list: {xs}")
    total, percentages = do_something_defensively(xs)
    print(f"total: {total}")
    print(f"percentages: {percentages}")

    _cr()


def _raise_if_iterator_with_isinstance():
    _div()

    def my_gen(length: int = 3):
        for x in range(length):
            yield x

    def do_something_defensively(xs, /):
        if isinstance(xs, Iterator):
            raise TypeError("Iterator not allowed as argument")
        xs_normalized = [int(x) for x in xs]
        total = sum(xs_normalized)
        percentages = []

        for x in xs:
            x_normalized = int(x)
            percentages.append(x_normalized / total * 100)

        return total, percentages

    it = my_gen(5)
    try:
        total, percentages = do_something_defensively(it)
    except TypeError:
        print("rejects iterator\n")

    xs = list(range(5))
    print(f"accepts list: {xs}")
    total, percentages = do_something_defensively(xs)
    print(f"total: {total}")
    print(f"percentages: {percentages}")

    _cr()

    path = _get_path("example.txt")
    my_iterable = _MyFileIterable(path)
    print(f"accepts container:")
    total, percentages = do_something_defensively(my_iterable)
    print(f"total: {total}")
    print(f"percentages: {percentages}")

    _cr()


if __name__ == "__main__":
    _beware_of_consuming_an_iterator_twice()
    _pass_generator_in_as_lambda()
    _use_class_to_iterate()
    _raise_if_iterator_with_comparison()
    _raise_if_iterator_with_isinstance()

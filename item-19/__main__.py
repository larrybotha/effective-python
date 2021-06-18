from inspect import stack
from typing import Optional


def _cr():
    print("")


def _div(text: Optional[str] = "", print_caller: bool = True):
    fn_name = stack()[1][3] if print_caller else None

    print("================")

    if text or fn_name:
        print(text or fn_name)
        _div(print_caller=False)


def _unpacking_from_assignment():
    _div()
    first, second = 1, 2
    xs = [(first, 1), (second, 2)]

    for (var, value) in xs:
        try:
            assert var == value
        except AssertionError:
            print("failed!")
            raise
        else:
            print("succeeded!")

    _cr()


def _unpacking_from_function():
    _div()

    def get_tuple():
        return 1, 2

    first, second = get_tuple()
    xs = [(first, 1), (second, 2)]

    for (var, value) in xs:
        try:
            assert var == value
        except AssertionError:
            print("failed!")
            raise
        else:
            print("succeeded!")

    _cr()


def _unpacking_incredibly_long_function_return():
    _div()

    """
    Don't write functions that return more than 3 values in the 1st place - use a
    named tuple, or a small class
    """

    def _too_man_return_values():
        mean = 1
        mode = 2
        median = 3
        standard_deviation = 4
        variance = 5

        return mean, mode, median, standard_deviation, variance

    # AAHHHHH!!!
    a, b, c, d, e = _too_man_return_values()

    # better
    print("get first, second, and rest")
    first, second, *rest = _too_man_return_values()
    print("get first, middle, and last")
    first, *middle, last = _too_man_return_values()
    print("get rest, second last, and last")
    *rest, second_last, last = _too_man_return_values()

    _cr()


if __name__ == "__main__":
    _unpacking_from_assignment()
    _unpacking_from_function()
    _unpacking_incredibly_long_function_return()

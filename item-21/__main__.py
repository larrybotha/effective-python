import random
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


def _sort_priority_closure(xs: list, group: set):
    """_sort_priority_closure.

    Sort a list by first evaluating each value against the values in the
    provided set

    :param xs:
    :type xs: list
    :param group:
    :type group: set
    """

    # the equivalent in Javascript for sorting is the following:
    # (a, b) => a > b ? -1 : 1
    def helper(x):
        if x in group:
            return (0, x)
        else:
            return (1, x)

    return sorted(xs, key=helper)


def _sort_using_closure():
    _div()
    xs = [random.randint(0, 10) for _ in range(10)]
    group = set(xs[-3:])

    ys = _sort_priority_closure(xs, group)
    print(f"{'list: ':>10} {xs}")
    print(f"{'group: ':>10} {group}")
    print(f"{'sorted list: ':>10} {ys}")

    _cr()


def _python_prevents_shadowing():
    _div()
    outer_var = "foo"

    print(f"outer_var before: {outer_var}")

    def assign_outer_var():
        # this is instantiation, not assignment
        outer_var = "bar"
        print(f"outer_var inside: {outer_var}")

    assign_outer_var()

    print(f"outer_var after: {outer_var}")
    print("outer_var unchanged by function scope!")
    _cr()


def _python_has_nonlocal_keyword():
    _div()
    outer_var = "foo"

    print(f"outer_var before: {outer_var}")

    def assign_outer_var():
        # make this value assignable
        nonlocal outer_var
        outer_var = "bar"
        print(f"outer_var inside: {outer_var}")

    assign_outer_var()

    print(f"outer_var after: {outer_var}")
    print("outer_var changed by function scope thanks to nonlocal keyword!")
    _cr()


def _avoid_nonlocal_with_a_class():
    _div()

    class Sorter:
        def __init__(self, group_values: set):
            self.found = False
            self.group = group_values

        # __call__ will be executed if the instance is used as a function
        def __call__(self, x):
            if x in self.group:
                self.found = True
                return (0, x)
            else:
                return (1, x)

    xs = [random.randint(0, 10) for _ in range(10)]
    group = set([random.randint(0, 2) for _ in range(3)])
    my_sorter = Sorter(group)

    ys = sorted(xs, key=my_sorter)
    print(f"{'list: ':>14} {xs}")
    print(f"{'group: ':>14} {group}")
    print(f"{'sorted list: ':>14} {ys}")
    print(f"{'value found?: ':>14} {my_sorter.found}")


if __name__ == "__main__":
    _sort_using_closure()
    _python_prevents_shadowing()
    _python_has_nonlocal_keyword()
    _avoid_nonlocal_with_a_class()

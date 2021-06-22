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


def _verbose_list_comprehension_without_assignment_expression():
    _div()
    ord_a = ord("a")
    xs = [random.randint(0, 25) for _ in range(5)]

    # chr(ord_a + v) is repeated here
    my_dict = {chr(ord_a + v): v for v in xs if chr(ord_a + v) > "m"}

    print(my_dict)
    _cr()


def _avoid_repetition_with_assignment_expression():
    _div()
    ord_a = ord("a")
    xs = [random.randint(0, 25) for _ in range(5)]

    # chr(ord_a + v) is evaluated once per iteration
    my_dict = {k: v for v in xs if (k := chr(ord_a + v)) and k > "m"}

    print(my_dict)
    _cr()


def _assignment_expressions_in_the_value_part_leak():
    _div()

    xs = [1, 2, 3]

    # the last value assigned to x will be leaked as x to the rest of this function's
    # scope
    ys = [(x := v) for v in xs]

    print(f"xs: {xs}")
    print(f"ys: {ys}")
    print(f"x: {x} (leaked variable)")


def _assignment_expressions_in_generator_expressions():
    _div()

    xs = [1, 2, 3]
    gen = ((x, x_squared) for x in xs if (x_squared := x ** 2))

    print(f"xs: {xs}")

    print(f"gen:")
    print(f"\t: {next(gen)}")
    print(f"\t: {next(gen)}")
    print(f"\t: {next(gen)}")


if __name__ == "__main__":
    _verbose_list_comprehension_without_assignment_expression()
    _avoid_repetition_with_assignment_expression()
    _assignment_expressions_in_the_value_part_leak()
    _assignment_expressions_in_generator_expressions()

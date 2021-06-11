from inspect import stack
from random import randint
from typing import Optional


def _cr():
    print("")


def _div(text: Optional[str] = "", print_caller: bool = True):
    fn_name = stack()[1][3] if print_caller else None

    print("================")

    if text or fn_name:
        print(text or fn_name)
        _div(print_caller=False)


def _get_truthy_value():
    return 1


def _if_simple():
    _div()

    # expression assignment assigns in if statement
    if count := _get_truthy_value():
        print(f"condition is valid - count is assigned {count}")

    _cr()


def _if_comparative():
    _div()

    # expression assignment assigns in if statement
    if (count := _get_truthy_value()) > 0:
        print(f"condition is valid - count is assigned {count}")

    _cr()


def _almost_a_switch():
    _div()

    some_dict = {
        "a": randint(0, 10),
        "b": randint(0, 10),
        "c": randint(0, 10),
    }

    # Python doesn't have a switch statement, but the walrus operator can be
    # used to create a similar construct
    if (x := some_dict.get("a", 0)) >= 5:
        print(f"using a: {x}")
    elif (x := some_dict.get("b", 0)) >= 5:
        print(f"using b: {x}")
    elif (x := some_dict.get("c", 0)) >= 5:
        print(f"using c: {x}")
    else:
        print("no match!")

    _cr()


def _almost_a_do_while():
    _div()

    def _get_last(ys: list):
        last = None

        if len(ys) > 0:
            *_, last = ys

        return last

    xs = list(range(1, 4))

    while last := _get_last(xs):
        xs = xs[:-1]

        print(f"removed {last}")

    _cr()


if __name__ == "__main__":
    _if_simple()
    _if_comparative()
    _almost_a_switch()
    _almost_a_do_while()

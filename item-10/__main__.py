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


if __name__ == "__main__":
    _if_simple()
    _if_comparative()

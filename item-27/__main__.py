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


def _verbose_map_and_filter():
    _div()

    xs = list(range(10))
    string = "map(\n\tlambda x: x ** 2,\n\t filter(lambda x: x % 2 == 0, xs)\n)"
    print(f"xs: {xs}")
    print(f"{string}\n\t\n => {list(eval(string))}")


def _terse_list_comprehension():
    _div()

    xs = list(range(10))
    string = "[x**2 for x in xs if x % 2 == 0]"
    print(f"xs: {xs}")
    print(f"{string}\n\t\n => {list(eval(string))}")


if __name__ == "__main__":
    _verbose_map_and_filter()
    _terse_list_comprehension()

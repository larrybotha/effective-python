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


def _comprehensions_can_be_nested():
    _div()

    xxs = [[1, 2, 3], [4, 5, 6]]
    string = "[x for xrow in xxs for x in xrow]"

    print(f"xxs: {xxs}\n")
    print(f"{string} =\n\t{eval(string)}")

    _cr()


if __name__ == "__main__":
    _comprehensions_can_be_nested()

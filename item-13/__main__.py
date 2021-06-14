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


def _catch_all_unpacking():
    _div()
    xs = list(range(10))
    first, *middle, last = xs
    print(f'{"original":>10} {xs}\n')
    print(f'{"first":>10} {first}')
    print(f'{"middle":>10} {middle}')
    print(f'{"last":>10} {last}')
    _cr()


if __name__ == "__main__":
    _catch_all_unpacking()

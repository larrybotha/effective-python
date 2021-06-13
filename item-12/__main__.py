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


def _mixing_slicing_and_stepping_is_difficult_to_read():
    _div()
    xs = list(range(10))
    command = f"xs[-2::-2]"

    print(f"{'original:':>10} {xs}")
    print(f"{'slice:':>10} {command}")
    print(f"{'outcome:':>10} {eval(command)}")

    _cr()


if __name__ == "__main__":
    _mixing_slicing_and_stepping_is_difficult_to_read()

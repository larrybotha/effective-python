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


def _for_else():
    _div()

    for i in range(10):
        print(f"printing in for: {i}")
    else:
        print("printing in else: 10")

    _cr()


def _for_else_skipped():
    _div()

    for i in range(10):
        print("else will not be printed")
        break
    else:
        print("not printed!")

    _cr()


def _empty_iterable_fires():
    _div()

    for _ in []:
        print("nothing to see here")
    else:
        print("empty iterable results in else being executed")

    _cr()


def _while_else():
    _div()
    done = False
    count = 0

    while not done:
        count = count + 1
        print(f"count in while: {count}")

        done = True if count >= 5 else done
    else:
        print("printed from 'else'")

    _cr()


def _while_else_skipped():
    _div()
    count = 0

    while True:
        count = count + 1
        print(f"count in while: {count}")

        if count >= 5:
            break
    else:
        print("never printed")

    _cr()


def _false_while_executes():
    _div()

    while False:
        print("nothing to see here")
    else:
        print("executed from False while")

    _cr()


if __name__ == "__main__":
    _for_else()
    _for_else_skipped()
    _empty_iterable_fires()
    _while_else()
    _while_else_skipped()
    _false_while_executes()

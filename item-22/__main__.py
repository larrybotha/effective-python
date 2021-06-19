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


def _fixed_arity():
    _div()

    def my_func(msg, xs):
        print(f"message: {msg} - required")
        print(f"xs: {xs} - required")

    my_func("a message", list(range(3)))
    _cr()


def _variable_arity():
    _div()

    def my_func(msg, *args):
        print(f"message: {msg} - required")
        print(f"*args: {args} - optional")

    xs = list(range(3))

    my_func("one value", xs)

    _cr()

    my_func("no values")

    _cr()

    my_func("many values", *xs)

    _cr()


def _positional_arguments_consume_entire_iterable():
    _div()

    def my_gen():
        for i in range(10):
            yield i

    def my_fn(*args):
        print(*args)

    iterator = my_gen()
    my_fn(*iterator)
    _cr()


if __name__ == "__main__":
    _fixed_arity()
    _variable_arity()
    _positional_arguments_consume_entire_iterable()

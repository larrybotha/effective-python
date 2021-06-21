from functools import wraps
from inspect import stack
from typing import Callable, Optional


def _cr():
    print("")


def _div(text: Optional[str] = "", print_caller: bool = True):
    fn_name = stack()[1][3] if print_caller else None

    print("================")

    if text or fn_name:
        print(text or fn_name)
        _div(print_caller=False)


def _decorator_example():
    _div()

    def my_decorator(func: Callable):
        def wrapper(*args, **kwargs):
            print(f"function: {func.__name__}")
            print(f"\t*args: {args}")
            print(f"\t*kwargs: {kwargs}")
            result = func(*args, **kwargs)
            print(f"\tresult: {result}")

            return result

        return wrapper

    @my_decorator
    def my_sum(a, b, /):
        return a + b

    my_sum(1, 2)

    _cr()


def _decorator_without_wraps():
    _div()

    def my_decorator(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapper

    @my_decorator
    def my_sum(a: float, b: float, /):
        """my_sum.

        :param a:
        :param b:
        """
        return a + b

    name_string = "my_sum.__name__"
    doc_string = "my_sum.__doc__"
    help_string = "help(my_sum)"

    print(f"my_sum's metadata is lost when our decorator doesn't use @wraps:")
    print(f"{name_string}:\n\t{eval(name_string)}")
    print(f"{doc_string}:\n\t{eval(doc_string)}")
    print(f"{help_string}:\n\t{eval(help_string)}")

    _cr()


def _decorator_with_wraps():
    _div()

    def my_decorator(func):
        # decorate our wrapper with @wraps
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapper

    @my_decorator
    def my_sum(a: float, b: float, /):
        """my_sum.

        :param a:
        :param b:
        """
        return a + b

    name_string = "my_sum.__name__"
    doc_string = "my_sum.__doc__"
    help_string = "help(my_sum)"

    print(f"my_sum's metadata is retained when our decorator uses @wraps:")
    print(f"{name_string}:\n\t{eval(name_string)}")
    print(f"{doc_string}:\n\t{eval(doc_string)}")
    print(f"{help_string}:\n\t{eval(help_string)}")

    _cr()


if __name__ == "__main__":
    _decorator_example()
    _decorator_without_wraps()
    _decorator_with_wraps()

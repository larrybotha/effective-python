from functools import wraps
from itertools import repeat


def _print_fn(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        fn_name = fn.__name__.replace("_", " ")
        indent = 2
        div = "".join(repeat("=", len(fn_name) + indent * 2))
        title = "\n".join([div, f"{''.join(repeat(' ', indent))}{fn_name}", div])
        print(title)
        fn(*args, **kwargs)
        print("\n")

    return wrapper


@_print_fn
def _yield_evaluates_to_none():
    def my_gen(length: int):
        for i in range(length):
            result = yield i
            print(f"{'my_gen yielded:':>26} {i}")
            print(f"{'my_gen yield evaluated to:':>26} {result}\n")

    it = my_gen(2)

    while True:
        try:
            string = "next(it)"
            print(f"{string}: {eval(string)}")
        except StopIteration:
            break


@_print_fn
def _yield_can_be_assigned_with_send():
    def my_gen(length: int):
        for i in range(length):
            assigned_yield = yield i
            print(f"assigned yield: {assigned_yield}")

    it = my_gen(3)
    output = it.send(None)

    print(f"output: {output}")

    while True:
        try:
            output = next(it)
            output = it.send("foo")
            print(f"output: {output}")
        except StopIteration:
            break


if __name__ == "__main__":
    _yield_evaluates_to_none()
    _yield_can_be_assigned_with_send()

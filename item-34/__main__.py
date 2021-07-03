import traceback
from functools import wraps
from itertools import repeat
from typing import Iterator, List


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
def _first_value_sent_must_be_none():
    def my_gen(length: int):
        for x in range(length):
            yield x

    it = my_gen(1)
    xs = [0]

    for x in xs:
        try:
            it.send(x)
        except TypeError as error:
            print(error)
            print(f"cause: {error.__cause__}")
            print("-----------------------------------")
            traceback.print_tb(error.__traceback__)
            print("-----------------------------------")


@_print_fn
def _send_advances_yield():
    def my_gen(length: int):
        for i in range(length):
            value_of_yield = yield i
            print(f"value of yield: {value_of_yield}")

    it = my_gen(3)
    output = it.send(None)

    print(f"output: {output}")

    while True:
        try:
            # output = next(it)
            yielded_value = it.send("foo")
            print(f"yielded_value: {yielded_value}")
        except StopIteration:
            break


@_print_fn
def _send_does_not_persist_yield_value():
    def my_gen(length: int):
        for i in range(length):
            value_of_yield = yield i
            print(f"value of yield: {value_of_yield}")

    it = my_gen(3)
    send_it = iter(["foo", None, None])
    output = it.send(None)

    print(f"output: {output}")

    while True:
        try:
            # output = next(it)
            yielded_value = None
            send_value = next(send_it)
            if send_value is not None:
                yielded_value = it.send("foo")
            else:
                yielded_value = next(it)

            print(f"yielded_value: {yielded_value}")
        except StopIteration:
            break


@_print_fn
def _send_can_inject_data_into_iterators():
    def my_product_gen(xs: List[int]):
        # scalar must be set using `send`, before doing the actual iteration
        scalar = yield
        print(f"scalar before iteration: {scalar}\n")

        for (i, x) in enumerate(xs):
            print(f"scalar in iteration {i}: {scalar}")
            # set the value of scalar on the
            scalar = yield x * scalar

    it = my_product_gen([1, 2, 3])
    # set the first value to None
    scalars = [None] + [x * 10 for (x, _) in enumerate(range(2), 1)]

    for scalar in scalars:
        product = it.send(scalar)
        print(f"scalar: {scalar}")
        print(f"product: {product}\n")


@_print_fn
def _avoid_send_by_passing_in_an_iterator():
    def my_product_gen(xs: List[int], scalar_it: Iterator[int]):
        for x in xs:
            yield x * next(scalar_it)

    xs = [x for (x, _) in enumerate(range(3), 1)]
    scalar_it = (x * 10 for (x, _) in enumerate(range(3), 1))
    it = my_product_gen(xs, scalar_it)

    for i in it:
        print(f"product: {i}")


if __name__ == "__main__":
    _yield_evaluates_to_none()
    _first_value_sent_must_be_none()
    _send_advances_yield()
    _send_does_not_persist_yield_value()
    _send_can_inject_data_into_iterators()
    _avoid_send_by_passing_in_an_iterator()

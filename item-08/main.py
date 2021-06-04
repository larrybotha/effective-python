from itertools import zip_longest
from random import randint
from typing import Optional


def cr():
    print("")


def div(text: Optional[str] = ""):
    print("================")
    if text:
        print(text)
        div()


def _zip_result():
    div("_zip_result")
    xs = [randint(0, 10) for _ in list(range(3))]
    ys = [n ** 2 for n in xs]
    zs = zip(xs, ys)

    print(f"xs: {xs}")
    print(f"ys: {ys}")

    print(f"zs:")
    for _, z in enumerate(zs):
        print(f"{z!r:>10}")
    cr()


def _parallel_iteration():
    div("_parallel_iteration")
    xs = [randint(0, 10) for _ in range(3)]
    ys = [n ** 2 for n in xs]

    for x, y in zip(xs, ys):
        print(f"{x}^2 = {y}")


def _discarded_values():
    div("_discarded_values")
    xs = [randint(0, 10) for _ in list(range(3))]
    string = "hello"
    zs = zip(xs, string)

    print(f"xs: {xs!r:>13}")
    print(f"string: {string}")

    print(f"zs:")
    for _, z in enumerate(zs):
        print(f"{z!r:>10}")
    cr()


def _zip_longest():
    div("_zip_longest")
    xs = [randint(0, 10) for _ in list(range(3))]
    string = "hello"
    zs = zip_longest(xs, string)

    print(f"xs: {xs!r:>13}")
    print(f"string: {string}")

    print("zs: ")
    for _, z in enumerate(zs):
        print(f"{z!r:>15}")


if __name__ == "__main__":
    _zip_result()
    _parallel_iteration()
    _discarded_values()
    _zip_longest()

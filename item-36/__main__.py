from functools import wraps
from itertools import (
    accumulate,
    chain,
    count,
    cycle,
    dropwhile,
    repeat,
    takewhile,
    tee,
    zip_longest,
)


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
def _count():
    counter = count()

    for _ in range(3):
        print(f"count: {next(counter)}")


@_print_fn
def _cycle():
    list_cycler = cycle([1, 2])

    for _ in range(4):
        print(f"list cycle: {next(list_cycler)}")

    print()
    string_cycler = cycle("cat")

    for _ in range(6):
        print(f"string cycle: {next(string_cycler)}")

    print()
    tuple_cycler = cycle((1, 2))

    for _ in range(4):
        print(f"tuple cycle: {next(tuple_cycler)}")

    print()
    set_cycler = cycle({1, 2})

    for _ in range(4):
        print(f"set cycle: {next(set_cycler)}")

    print()
    gen_cycler = cycle((x for x in range(2)))

    for _ in range(4):
        print(f"gen cycle: {next(gen_cycler)}")


@_print_fn
def _repeat():
    repeater = repeat("repeated value", 3)

    for x in repeater:
        print(f"repeat: {x}")


@_print_fn
def _zip_longest():
    xs = list(range(3))
    ys = [x + len(xs) for x in range(len(xs) * 2)]

    print(f"xs: {xs}")
    print(f"ys: {ys}\n")

    zs = zip_longest(xs, ys, fillvalue="my fill value")

    for z in zs:
        print(z)


@_print_fn
def _chain():
    xs = [1, 2, 3]
    ys = [x + len(xs) for x in xs]

    print(f"xs: {xs}")
    print(f"ys: {ys}\n")

    chained = chain(xs, ys)

    for x in chained:
        print(x)


@_print_fn
def _chain_from_iterable():
    xxs = ["hello", "there"]

    print(f"xxs: {xxs}\n")

    chained = chain.from_iterable(xxs)

    for x in chained:
        print(x)


@_print_fn
def _tee():
    xs = [1, 2, 3]

    ys, zs = tee(xs, 2)

    print(f"xs: {xs}")

    print("\nys")
    for y in ys:
        print(y)

    print("\nzs")
    for z in zs:
        print(z)


@_print_fn
def _dropwhile():
    xs = list(range(10))

    lte5 = lambda x: x < 5
    dropper = dropwhile(lte5, xs)

    print(f"xs: {xs}\n")

    print("drop while less than 5")

    for x in dropper:
        print(x)


@_print_fn
def _takewhile():
    xs = list(range(10))

    lte5 = lambda x: x < 5
    taker = takewhile(lte5, xs)

    print(f"xs: {xs}\n")

    print("take while less than 5")

    for x in taker:
        print(x)


@_print_fn
def _accummulate():
    xs = [1, 2, 3]

    print(f"xs: {xs}\n")

    sum_squares = lambda acc, x: acc + x ** 2
    accumulator = accumulate(xs, sum_squares)

    for x in accumulator:
        print(x)


if __name__ == "__main__":
    _count()
    _cycle()
    _repeat()
    _zip_longest()
    _chain()
    _chain_from_iterable()
    _tee()
    _dropwhile()
    _takewhile()
    _accummulate()

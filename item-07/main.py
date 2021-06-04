from typing import Optional


def cr():
    print("")


def div(text: Optional[str] = ""):
    print("================")
    if text:
        print(text)
        div()


def _use_enumerate():
    div("use_enumerate")
    xs = [1, 2, 3]

    # clumsy iteration
    print("clumsy iteration with len and range")
    for i in range(len(xs)):
        print(f"{i}: {xs[i]}")
    cr()

    print("terse iteration with enumerate")
    for i, x in enumerate(xs):
        print(f"{i}: {x}")

    cr()


def _manual_iteration():
    div("_manual_iteration")
    xs = [1, 2, 3]
    iterator = enumerate(xs)

    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    cr()


def _starting_value():
    div("_starting_value")
    xs = ["a", "b", "c"]
    start_index = 1

    for i, char in enumerate(xs, start_index):
        print(f"{i} => {char}")


if __name__ == "__main__":
    _use_enumerate()
    _manual_iteration()
    _starting_value()

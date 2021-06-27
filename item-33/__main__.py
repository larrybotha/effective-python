import timeit
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
def _verbose_multiple_generators_example():
    def move(duration: int, speed: float, /):
        for _ in range(duration):
            yield "move", speed

    def pause(duration: int, /):
        for _ in range(duration):
            yield "pause", 0

    # this is repetetive
    def animate():
        for action, delta in move(3, 5.0):
            yield action, delta
        for action, delta in pause(2):
            yield action, delta
        for action, delta in move(2, 2.0):
            yield action, delta

    def loop(fn):
        for action, delta in fn():
            print(f"action: {action} => {delta}")

    loop(animate)


@_print_fn
def _terse_with_yield_from():
    def move(duration: int, speed: float, /):
        for _ in range(duration):
            yield "move", speed

    def pause(duration: int, /):
        for _ in range(duration):
            yield "pause", 0

    # much clearer with yield from
    def animate():
        yield from move(3, 5.0)
        yield from pause(2)
        yield from move(2, 2.0)

    def loop(fn):
        for action, delta in fn():
            print(f"action: {action} => {delta}")

    loop(animate)


def _large_gen():
    for i in range(1_000_000):
        yield i


def _iterate_with_for_loop(iterator):
    for i in iterator:
        yield i


def _iterate_with_yield_from(iterator):
    yield from iterator


@_print_fn
def _yield_from_has_better_performance_than_for_loops():
    print("benchmarking...")

    for_loop_time = timeit.timeit(
        globals=globals(),
        number=50,
        stmt="for _ in _iterate_with_for_loop(_large_gen()): pass",
    )

    print(f"{'for loop:':<15} {for_loop_time:.2f}s")

    yield_from_time = timeit.timeit(
        globals=globals(),
        number=50,
        stmt="for _ in _iterate_with_yield_from(_large_gen()): pass",
    )

    print(f"{'yield from:':<15} {yield_from_time:.2f}s")

    result = -(yield_from_time - for_loop_time) / for_loop_time

    print(f"{'result:':<15} {result:.1%} faster")


if __name__ == "__main__":
    _verbose_multiple_generators_example()
    _terse_with_yield_from()
    _yield_from_has_better_performance_than_for_loops()

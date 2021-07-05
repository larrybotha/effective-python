import traceback
from functools import wraps
from itertools import count, cycle, repeat


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


class _MyGenError(Exception):
    pass


@_print_fn
def _throwing_inside_a_generator_will_stop_iteration():
    def timer_gen(period: int):
        for i in count():
            # sleep period
            yield i

    timer = timer_gen(1)

    print(f"iterate:  {next(timer)}")

    try:
        print("\nthrowing using timer.throw")
        print(timer.throw(_MyGenError("some error!")))
    except _MyGenError as error:
        print(f"\nError: {error}")
        print("-----------------------------------")
        traceback.print_tb(error.__traceback__)
        print("-----------------------------------\n")

    try:
        print("try iterate again")
        print(next(timer))
    except StopIteration as error:
        print("error thrown, iteration was stopped")


@_print_fn
def _generators_can_handle_exceptions():
    def my_gen(period: int):
        for x in count():
            try:
                # sleep period
                yield x
            except _MyGenError:
                # this yield will do nothing
                yield -1

                print("errored!")

    it = my_gen(1)

    print(f"iterate: {next(it)}")

    it.throw(_MyGenError("naughty"))

    print(f"iterate: {next(it)}")


@_print_fn
def _exceptions_to_manage_state_in_generators():
    class ResetGenException(Exception):
        pass

    def counter_gen():
        count = 0

        for _ in cycle([None]):
            try:
                yield count
                count = count + 1
            except ResetGenException:
                count = -1

    it = counter_gen()

    for _ in range(3):
        print(f"count: {next(it)}")

    print("\nresetting counter using throw\n")
    # this right here looks like a code smell
    it.throw(ResetGenException("reset!"))

    for _ in range(2):
        print(f"count: {next(it)}")


@_print_fn
def _use_a_class_with_iter_to_manage_state():
    class Counter:
        def __init__(self, start: int = 0, /):
            self.start = start
            self.count = self.start

        def reset(self):
            self.count = self.start

        def __iter__(self):
            while True:
                self.count = self.count + 1
                yield self.count

    counter = Counter()
    counter_it = iter(counter)

    for _ in range(6):
        print(f"count: {next(counter_it)}")

    print("\nresetting counter using method\n")
    counter.reset()

    for _ in range(2):
        print(f"count: {next(counter_it)}")


if __name__ == "__main__":
    _throwing_inside_a_generator_will_stop_iteration()
    _generators_can_handle_exceptions()
    _exceptions_to_manage_state_in_generators()
    _use_a_class_with_iter_to_manage_state()

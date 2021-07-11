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
def _multiple_inheritance_initialization_order():
    class BaseClass:
        def __init__(self, value):
            self.value = value

    class AddTwo:
        def __init__(self):
            self.value += 2

    class TimesTwo:
        def __init__(self):
            self.value *= 2

    class AddThenTimes(BaseClass, AddTwo, TimesTwo):
        def __init__(self, value):
            BaseClass.__init__(self, value)
            AddTwo.__init__(self)
            TimesTwo.__init__(self)

    class TimesThenAdd(BaseClass, TimesTwo, AddTwo):
        def __init__(self, value):
            BaseClass.__init__(self, value)
            # bug - order of these needs to switched, which can be difficult to
            # find
            AddTwo.__init__(self)
            TimesTwo.__init__(self)

    value = 10
    add_then_times = AddThenTimes(value)
    times_then_add = TimesThenAdd(value)

    print(f"add_then_times: {add_then_times.value}")
    print(f"times_then_add: {times_then_add.value}")

@_print_fn
def _diamond_inheritance():
    class BaseClass:
        def __init__(self, value):
            self.value = value

    class AddTwo:
        def __init__(self, value):
            BaseClass.__init__(self, value)
            self.value += 2

    class TimesTwo:
        def __init__(self, value):
            BaseClass.__init__(self, value)
            self.value *= 2

    class AddThenTimes(BaseClass, AddTwo, TimesTwo):
        def __init__(self, value):
            BaseClass.__init__(self, value)
            AddTwo.__init__(self)
            TimesTwo.__init__(self)

    class TimesThenAdd(BaseClass, TimesTwo, AddTwo):
        def __init__(self, value):
            BaseClass.__init__(self, value)
            # bug - order of these needs to switched, which can be difficult to
            # find
            AddTwo.__init__(self)
            TimesTwo.__init__(self)


if __name__ == "__main__":
    _multiple_inheritance_initialization_order()
    _diamond_inheritance():

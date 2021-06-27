import os
from functools import wraps
from itertools import count, repeat


def _print_fn(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        fn_name = fn.__name__.replace("_", " ")
        indent = 2
        div = "".join(repeat("=", len(fn_name) + indent * 2))
        print(div)
        print(f"{''.join(repeat(' ', indent))}{fn_name}")
        print(div)
        fn(*args, **kwargs)
        print("\n")

    return wrapper


@_print_fn
def _list_comprehensionn_to_read_files():
    path = f"{os.path.dirname(__file__)}/example.txt"
    lines = [line.replace("\n", "") for line in open(path, "r")]
    print(f"lines: {lines}")


@_print_fn
def _generator_expression_to_read_files():
    path = f"{os.path.dirname(__file__)}/example.txt"
    it = (line for line in open(path))

    while True:
        try:
            line = next(it)
            print(f"line: {line}")
        except StopIteration:
            print("done reading lines")
            break


@_print_fn
def _generator_expression_can_be_composed():
    ord_a = ord("a")
    ord_iterator = (x for x in count(0))
    chr_iterator = (chr(ord_a + x) for x in ord_iterator)

    print(f"advance chr_iterator: {next(chr_iterator)}")
    print(f"advance ord_iterator: {next(ord_iterator)}")
    print(f"advance chr_iterator: {next(chr_iterator)}")


if __name__ == "__main__":
    _list_comprehensionn_to_read_files()
    _generator_expression_to_read_files()
    _generator_expression_can_be_composed()

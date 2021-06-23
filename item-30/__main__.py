import os
from inspect import stack
from io import TextIOWrapper
from typing import Optional


def _cr():
    print("")


def _div(text: Optional[str] = "", print_caller: bool = True):
    fn_name = stack()[1][3] if print_caller else None

    print("================")

    if text or fn_name:
        print(text or fn_name)
        _div(print_caller=False)


def _returning_a_list():
    _div()

    def get_word_indexes(line: str):
        indexes = []

        if line:
            indexes = indexes + [0]

            for index, letter in enumerate(line):
                if letter == " ":
                    indexes = indexes + [index + 1]

        return indexes

    text = "lorem ipsum"
    word_indexes = get_word_indexes(text)

    print(f"text: {text}")
    print(f"word_indexes: {word_indexes}")

    _cr()


def _creating_a_generator():
    _div()

    def get_word_indexes_iter(line: str):
        if text:
            yield 0

        for index, letter in enumerate(line):
            if letter == " ":
                yield index + 1

    text = "lorem ipsum"
    gen = get_word_indexes_iter(text)

    string = "next(gen)"
    print(f"{string}: {eval(string)}")
    print(f"{string}: {eval(string)}")

    _cr()


def _list_comprehension_over_iterator():
    _div()

    def get_items_iter(length: int = 5):
        for i in range(length):
            print(f"yielding {i}")
            yield i

    gen = get_items_iter()
    xs = [x for x in gen]

    print(f"xs: {xs}")
    _cr()


def _loop_over_generator():
    _div()

    def get_items_iter(length: int = 5):
        for i in range(length):
            print(f"yielding {i}")
            yield i

    # the list is built lazily, despite the generator being instantiated here
    gen = get_items_iter()
    xs = []

    for i in gen:
        print(f"got {i} from gen")
        xs = xs + [i]

    print(f"xs: {xs}")
    _cr()


def _generator_raises_stop_iteration():
    _div()

    def my_gen(length: int = 3, /):
        for i in range(length):
            yield i

    gen = my_gen()

    while True:
        try:
            print(f"next: {next(gen)}")
        except StopIteration:
            print("gen is done")
            break

    _cr()


def _file_reading_generator():
    _div()

    def my_file_gen(handle: TextIOWrapper, /):
        for line in handle:
            yield line

    path = f"{os.path.dirname(__file__)}/example.txt"
    file_handle = open(path, "r")
    file_iter = my_file_gen(file_handle)

    print(f"reading: {path}\n")

    while True:
        try:
            print(f"next line: {next(file_iter)}")
        except StopIteration:
            print("file has been read")
            break

    _cr()


if __name__ == "__main__":
    _returning_a_list()
    _creating_a_generator()
    _loop_over_generator()
    _list_comprehension_over_iterator()
    _generator_raises_stop_iteration()
    _file_reading_generator()

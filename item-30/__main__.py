from inspect import stack
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


if __name__ == "__main__":
    _returning_a_list()
    _creating_a_generator()

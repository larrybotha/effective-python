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


def _catch_all_unpacking():
    _div()
    xs = list(range(10))
    first, *middle, last = xs
    print(f'{"original":>10} {xs}\n')
    print(f'{"first":>10} {first}')
    print(f'{"middle":>10} {middle}')
    print(f'{"last":>10} {last}')
    _cr()


def _generate_csv_data():
    yield ("header 1", "header 2", "header 3")
    yield ("row 1 value 1", "row 1 value 2", "row 1 value 3")
    yield ("row 2 value 1", "row 2 value 2", "row 2 value 3")


def _unpacking_iterators():
    _div()
    headers, *rows = _generate_csv_data()
    print(f'{"headers":>10} {headers}')
    print(f'{"rows":>10} {rows}')
    _cr()


if __name__ == "__main__":
    _catch_all_unpacking()
    _unpacking_iterators()

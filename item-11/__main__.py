import math
from enum import Enum
from inspect import stack
from itertools import islice
from typing import Iterable, Optional


class Type(Enum):
    LIST = list.__name__
    TUPLE = tuple.__name__
    SET = set.__name__


def _cr():
    print("")


def _div(text: Optional[str] = "", print_caller: bool = True):
    fn_name = stack()[1][3] if print_caller else None

    print("================")

    if text or fn_name:
        print(text or fn_name)
        _div(print_caller=False)


def _slice_to_type(type: Type, slice: islice):
    if type == Type.LIST:
        return list(slice)
    elif type == Type.SET:
        return set(slice)
    elif type == Type.TUPLE:
        return tuple(slice)


def _get_dict():
    l = list(range(5))
    s = set(l)
    t = tuple(l)
    values = {
        Type.LIST: l,
        Type.SET: s,
        Type.TUPLE: t,
    }

    return values


def _copy():
    _div()
    sequences_dict = _get_dict()

    for (type, value) in sequences_dict.items():
        slice = islice(value, None, None)
        print(f"{type}")
        print(f"\t{'original:':>10} {value}")
        print(f"\t{'sliced:':>10} {_slice_to_type(type, slice)}")
        _cr()

    _cr()


def _reverse():
    _div()
    sequences_dict = _get_dict()

    for (type, value) in sequences_dict.items():
        slice = list(value)[::-1]
        new_value: Iterable[int] = slice

        if type == Type.SET:
            new_value = set(new_value)
        elif type == Type.TUPLE:
            new_value = tuple(new_value)

        print(f"{type}")
        print(f"\t{'original:':>10} {value}")
        print(f"\t{'sliced:':>10} {_slice_to_type(type, new_value)}")
        _cr()


def _start_value(start: int = 2):
    _div()
    print(f"start = {start}")
    _cr()
    sequences_dict = _get_dict()

    for (type, value) in sequences_dict.items():
        slice = islice(value, start, None)

        print(f"{type}")
        print(f"\t{'original:':>10} {value}")
        print(f"\t{'sliced:':>10} {_slice_to_type(type, slice)}")
        _cr()


def _stop_value(stop: int = 2):
    _div()
    print(f"stop = {stop}")
    _cr()
    sequences_dict = _get_dict()

    for (type, value) in sequences_dict.items():
        slice = islice(value, None, stop)

        print(f"{type}")
        print(f"\t{'original:':>10} {value}")
        print(f"\t{'sliced:':>10} {_slice_to_type(type, slice)}")
        _cr()


def _step_value(step: int = 2):
    _div()
    print(f"step = {step}")
    _cr()
    sequences_dict = _get_dict()

    for (type, value) in sequences_dict.items():
        slice = islice(value, None, None, step)

        print(f"{type}")
        print(f"\t{'original:':>10} {value}")
        print(f"\t{'sliced:':>10} {_slice_to_type(type, slice)}")
        _cr()


def _list_start_negative():
    _div()
    xs = list(range(10))
    start = -math.floor(len(xs) / 2)

    print(f"xs[{start}:]")
    print(f"\t{'original:':>10} {xs}")
    print(f"\t{'sliced:':>10} {xs[start:]}")
    _cr()


def _list_stop_negative():
    _div()
    xs = list(range(10))
    stop = -math.floor(len(xs) / 2)

    print(f"xs[:{stop}]")
    print(f"\t{'original:':>10} {xs}")
    print(f"\t{'sliced:':>10} {xs[:stop]}")
    _cr()


def _list_reverse_stepped():
    _div()
    xs = list(range(10))
    step = -2

    print(f"xs[::{step}]")
    print(f"\t{'original:':>10} {xs}")
    print(f"\t{'sliced:':>10} {xs[::step]}")
    _cr()


def _assignment():
    _div()
    xs = list(range(10))
    print(f"\t{'original:':>10} {xs}")
    xs[2:-2] = [y ** 2 for y in xs[2:-2]]
    print(f"\t{'assigned:':>10} {xs}")
    _cr()


if __name__ == "__main__":
    _copy()
    _reverse()
    _start_value()
    _stop_value()
    _step_value()
    _list_start_negative()
    _list_stop_negative()
    _list_reverse_stepped()
    _assignment()

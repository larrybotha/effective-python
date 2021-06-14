from inspect import stack
from random import randint
from typing import Optional


def _cr():
    print("")


def _div(text: Optional[str] = "", print_caller: bool = True):
    fn_name = stack()[1][3] if print_caller else None

    print("================")

    if text or fn_name:
        print(text or fn_name)
        _div(print_caller=False)


def _get_items():
    def _get_name(index: int):
        ord_a = ord("a")
        return chr(ord_a + index)

    return [
        {
            "name": _get_name(
                v,
            ),
            "rank": randint(
                0,
                50,
            )
            / 10,
        }
        for v in list(range(5))
    ]


def _sort_using_key():
    _div()
    items = _get_items()
    print(f"{'items:':>10} {items}")
    # use  a lambda to specify the name of the key
    print(f"{'sorted:':>10} {sorted(items, key=lambda x: x['rank'])}")
    _cr()


def _sort_with_mapping():
    _div()
    places = ["Paris", "Amsterdam", "Rotterdam"]
    print(f"{'items:':>10} {places}")
    print(f"{'sorted:':>10} {sorted(places, key=lambda x: x.lower())}")
    _cr()


def _sort_order():
    _div()
    items = [
        {"name": "aa", "rank": 2},
        {"name": "ab", "rank": 1},
        {"name": "ac", "rank": 2},
    ]
    print(f"{'items:':>10} {items}")

    # sort first bt rank, then name
    key_sort = lambda x: (x["rank"], x["name"])
    print(f"{'sorted:':>10} {sorted(items, key=key_sort)}")

    _cr()


if __name__ == "__main__":
    _sort_using_key()
    _sort_with_mapping()
    _sort_order()

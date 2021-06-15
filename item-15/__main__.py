import random
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


def _get_items():
    ord_a = ord("a")
    item_map = {chr(ord_a + k): random.randint(0, 100) for k in range(5)}

    return item_map


def _show_sort_order_is_preserved():
    _div()
    item_map = _get_items()
    print(item_map)
    _cr()


def _use_sort_and_keys_to_sort():
    _div()
    item_map = _get_items()
    names = list(item_map.keys())
    sorted_names = sorted(names, key=item_map.get)
    sorted_ranks = sorted(item_map.values())
    print(f'{"names: ":>10} {names}')
    print(f'{"sorted: ":>10} {sorted_names}')
    print(f'{"ranks: ":>10} {sorted_ranks}')


if __name__ == "__main__":
    _show_sort_order_is_preserved()
    _use_sort_and_keys_to_sort()

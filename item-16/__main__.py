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


def _get_item_map():
    ord_a = ord("a")
    item_map = {chr(ord_a + k): random.randint(0, 100) for k in range(5)}

    return item_map


def _get_defaults_to_none():
    _div()
    my_dict = {}
    print(f"my_dict: {my_dict}")
    print(f'my_dict.get("foo"): {my_dict.get("foo")}')
    _cr()


def _raise_key_error():
    _div()
    d = {}

    print(f"attempting to access d['foo']")

    try:
        print(d["foo"])
    except KeyError as e:
        print(f"KeyError raised {e}")
    _cr()


def _terse_access():
    _div()
    item_map = _get_item_map()

    # using .get
    count = item_map.get("foo", 0)
    print(f"got count using .get: {count}")

    # vs try / except
    if "z" in item_map:
        print(f'contains z: {item_map["z"]}')
    else:
        print(f"doesn't contain z - do something default")

    _cr()


def _with_assignment_expression():
    _div()
    item_map = _get_item_map()
    ranks = []

    if char := item_map.get("z"):
        ranks[char] = char = 0

    _cr()


def _using_setdefault():
    _div()
    my_dict = _get_item_map()

    print("before")
    print(f"my_dict: {my_dict}")
    _cr()

    my_dict.setdefault("z", random.randint(0, 100))

    print("after my_dict.setdefault('z', #)")
    print(f"my_dict: {my_dict}")

    _cr()


def _setdefault_assigns_by_reference():
    _div()
    my_dict = {}
    key = "foo"
    xs = []

    my_dict.setdefault(key, xs)

    print("before")
    print(f"my_dict: {my_dict}")
    _cr()

    xs.append(1)

    print(f"after appending to {key}")
    print(f"my_dict: {my_dict}!!!")
    _cr()


if __name__ == "__main__":
    _get_defaults_to_none()
    _raise_key_error()
    _terse_access()
    _with_assignment_expression()
    _using_setdefault()
    _setdefault_assigns_by_reference()

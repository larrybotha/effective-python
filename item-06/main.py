from typing import Optional


def cr():
    print("")


def div(text: Optional[str] = ""):
    print("================")
    if text:
        print(text)
        div()


def tuple_intro():
    div("tuple_intro")
    my_dict = {"a": 100, "b": 8, "c": 10}
    # similar to Javascript's Object.items(someObj), dict.items()
    # turns a dict into list[Tuple[type, type]]
    # tuple(xs) creates a tuple from a list
    items = tuple(my_dict.items())
    print(f"tuple(some_dict.items()):\n {items}")
    print(f"tuple([1,2,3]): {tuple([1,2,3])}")
    cr()


def tuple_item_access():
    div("tuple_item_access - array-like")
    my_tuple = ("item 1", "item 2")
    print(f"my_tuple[0]: {my_tuple[0]}")
    print(f"my_tuple[1]: {my_tuple[1]}")
    cr()


def tuple_value_assignment():
    div("tuple_value_assignment")
    t = (1, 2, 3)
    try:
        print(t)
        print(f"t[0] = 4")
        t[0] = 4
    except TypeError:
        print("=> type error - setitem not defined on tuple")

    cr()


def tuple_unpacking():
    div("tuple_unpacking")
    t = (1, 2, 3)
    first, second, third = t
    print(f"first,second,third = (1,2,3): {first,second,third}")
    cr()


def tuple_unpacking_again():
    div("tuple_unpacking_again")
    d = {
        "foo": ("bar", 1),
        "baz": ("quux", 2),
    }
    (
        (first_name, (first_key, first_val)),
        (second_name, (second_key, second_val)),
    ) = d.items()
    print(first_name, first_key, first_val)
    print(second_name, second_key, second_val)
    cr()


def swapping_values():
    div("swapping_values")
    t = [1, 2]
    print(f"before: {t}")
    t[1], t[0] = t
    print(f"after: {t}")
    cr()


def bubble_sort(xs: list):
    div("bubble_sort")
    print(f"xs before: {xs}")

    for _ in range(len(xs)):
        for i in range(1, len(xs)):
            if xs[i] < xs[i - 1]:
                # swapping values is similar to Javascript
                xs[i - 1], xs[i] = xs[i], xs[i - 1]

    print(f"xs after: {xs}")
    cr()


def unpacking_in_loops():
    div("unpacking_in_loops")

    print("dictionary")
    d = {
        "foo": ("bar", 1),
        "baz": ("quux", 2),
    }

    for name, (x, y) in d.items():
        print(f"{name}: ({x}, {y})")

    for index, (name, (x, y)) in enumerate(d.items(), 1):
        print(f"{index} => {name}: ({x}, {y})")

    cr()
    print("list")
    l = [("foo", 1), ("bar", 2)]

    for name, value in l:
        print(f"{name}: {value}")

    for index, (name, value) in enumerate(l, 1):
        print(f"{index} => {name}: {value}")
    cr()


def array_unpacking():
    div("array_unpacking")
    xs = list(range(10))
    first, *rest, last = xs
    print(f"xs: {xs}")
    print(f"first: {first}")
    print(f"rest: {rest}")
    print(f"last: {last}")


if __name__ == "__main__":
    tuple_intro()
    tuple_item_access()
    tuple_value_assignment()
    tuple_unpacking()
    tuple_unpacking_again()
    swapping_values()
    bubble_sort(["foo", "bar", "baz"])
    unpacking_in_loops()
    array_unpacking()

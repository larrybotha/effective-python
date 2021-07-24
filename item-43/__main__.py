from collections.abc import Sequence
from functools import wraps
from itertools import repeat
from typing import Any, List


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
def _subclassing_extends_containers():
    class FrequencyList(list):
        def __init__(self, xs: List[Any]):
            super().__init__(xs)

        def frequency(self):
            counts = {}

            for x in self:
                counts[x] = counts.get(x, 0) + 1

            return counts

    xs = [1, 1, 1, 2, 2, 3]
    frequency_list = FrequencyList(xs)

    print(f"xs: {xs}")
    print(f"frequency: {frequency_list.frequency()}\n")

    print(f"pop: {frequency_list.pop()}")
    print(f"frequency: {frequency_list.frequency()}\n")

    print(f"append(5)")
    print(f"frequency: {frequency_list.frequency()}\n")


class _BinaryNode:
    def __init__(self, value, *, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# if the child class does not define __init__, it does not need to call
# super().__init__
class _IndexableNode(_BinaryNode):
    def _traverse(self):
        if self.left is not None:
            yield from self.left._traverse()

        yield self

        if self.right is not None:
            yield from self.right._traverse()

    # define __getitem__ to allow for accessing items by index
    def __getitem__(self, index: int):
        for i, item in enumerate(self._traverse()):
            if i == index:
                return item.value

        raise IndexError(f"Index {index} is out of range")


@_print_fn
def _manually_implementing_container_is_error_prone():
    root = _IndexableNode(
        6,
        left=_IndexableNode(3, left=_IndexableNode(1), right=_IndexableNode(5)),
        right=_IndexableNode(9, left=_IndexableNode(8), right=_IndexableNode(10)),
    )

    for _, item in enumerate(root._traverse()):
        print(item.value)

    print(f"root.left.value: {root.left.left.value}")
    print(f"root[0]: {root[0]}")

    try:
        print(f"\ntrying len(root)\n")
        len(root)
    except TypeError as error:
        print(f"error: {error.__class__.__name__}")
        print(error)

    print(
        """
        \nIndexableNode implements __getitem__, but not __len__, __setitem__, etc.
        """
    )


@_print_fn
def _astract_class_will_throw_if_not_implemented():
    class BadImplementation(Sequence):
        pass

    print("use abstract class Sequence as base class without implementation...\n")

    try:
        BadImplementation()
    except TypeError as error:
        print(error.__class__.__name__)
        print(error)


@_print_fn
def _use_collections_abc_abstract_classes_to_implement_containers():
    class BetterIndexableNode(_IndexableNode, Sequence):
        pass

        def __len__(self):
            count = 0

            for _ in self._traverse():
                count = count + 1

            return count

    root = BetterIndexableNode(
        6,
        left=BetterIndexableNode(
            3, left=BetterIndexableNode(1), right=BetterIndexableNode(5)
        ),
        right=BetterIndexableNode(
            9, left=BetterIndexableNode(8), right=BetterIndexableNode(10)
        ),
    )

    for _, item in enumerate(root._traverse()):
        print(item.value)

    print(f"root.left.value: {root.left.left.value}")
    print(f"root[0]: {root[0]}")
    print(f"len(root): {len(root)}")
    print(f"root.count(3): {root.count(3)}")


if __name__ == "__main__":
    _subclassing_extends_containers()
    _manually_implementing_container_is_error_prone()
    _astract_class_will_throw_if_not_implemented()
    _use_collections_abc_abstract_classes_to_implement_containers()

import json
from functools import wraps
from itertools import repeat
from typing import Any


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


class _ToDictMixin:
    def to_dict(self):
        return self._traverse_dict(self.__dict__)

    def _traverse_dict(self, instance_dict):
        output = {}

        for key, value in instance_dict.items():
            output[key] = self._traverse(key, value)

        return output

    def _traverse(self, key, value):
        # if the value is an instance of this mixin, use the mixin to get a dict
        if isinstance(value, _ToDictMixin):
            return value.to_dict()

        # if it's a dict, use the internal method to return a dict
        elif isinstance(value, dict):
            return self._traverse_dict(value)

        # if it's a list, loop over each value, invoking this method
        elif isinstance(value, list):
            return [self._traverse(key, i) for i in value]

        # if the value implements __dict__, pass that value to the mixin's
        # internal method
        elif hasattr(value, "__dict__"):
            return self._traverse_dict(value.__dict__)

        # otherwise return the value
        else:
            return value


class _JsonMixin(_ToDictMixin):
    @classmethod
    def from_json(cls, data):
        kwargs = json.loads(data)

        return cls(**kwargs)

    def to_json(self):
        # _JsonMixin depends on _ToDictMixin to dump json
        return json.dumps(self.to_dict())


@_print_fn
def _use_mixin_to_create_dict_of_class():
    class BinaryTree(_ToDictMixin):
        def __init__(
            self, value: Any, *, left: "BinaryTree" = None, right: "BinaryTree" = None
        ):
            self.value = value
            self.left = left
            self.right = right

    tree = BinaryTree(
        10,
        left=BinaryTree(7, right=BinaryTree(9)),
        right=BinaryTree(13, left=BinaryTree(11)),
    )

    print(tree.to_dict())


@_print_fn
def _mixin_method_can_be_overridden():
    class MyMixin:
        def print_me(self):
            print(self._get_name())

        def _get_name(self):
            return self.__class__.__name__

    class MyClass(MyMixin):
        def __init__(self):
            pass

    class MyClassWithOverridenMixinMethod(MyMixin):
        def __init__(self):
            pass

        def _get_name(self):
            return "foo"

    cls_1 = MyClass()
    cls_2 = MyClassWithOverridenMixinMethod()

    cls_1.print_me()
    cls_2.print_me()


@_print_fn
def _mixins_can_include_classmethods():
    class MyClass(_JsonMixin):
        def __init__(self, value: str):
            self.value = value

    json = '{"value": "foo"}'
    instance = MyClass.from_json(json)

    print(instance)


@_print_fn
def _mixins_can_be_composed():
    # This class only needs to use _JsonMixin as a mixin - _JsonMixin is
    # mixed-in with _ToDictMixin already
    class MyClass(_JsonMixin):
        def __init__(self, value: dict):
            self.value = value

    instance = MyClass({"a": 1})
    print(instance.to_json())


if __name__ == "__main__":
    _use_mixin_to_create_dict_of_class()
    _mixin_method_can_be_overridden()
    _mixins_can_include_classmethods()
    _mixins_can_be_composed()

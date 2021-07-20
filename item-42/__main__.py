from functools import wraps
from itertools import repeat


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
def _accessing_private_method_raises_exception():
    class MyClass:
        def __init__(self):
            self.public = "foo"
            self.__private = "bar"

    instance = MyClass()
    print(instance.public)

    try:
        print(instance.__private)
    except AttributeError:
        print("raised AttributeError accessing __private")


@_print_fn
def _private_attributes_can_be_accessed_via_new_name():
    class MyClass:
        def __init__(self):
            self.public = "foo"
            self.__private = "bar"

    instance = MyClass()
    print(f"instance._MyClass__private: {instance._MyClass__private}")


@_print_fn
def _class_methods_can_access_private_attributes():
    class MyClass:
        def __init__(self):
            self.public = "foo"
            self.__private = "bar"

        @classmethod
        def get_private_attribute(cls, instance):
            return instance.__private

    instance = MyClass()
    print(MyClass.get_private_attribute(instance))


@_print_fn
def _subclass_cannot_access_parent_private_attribute():
    class ParentClass:
        def __init__(self):
            self.__private = "foo"

    class ChildClass(ParentClass):
        def __init__(self):
            super().__init__()
            self.public = "foo"

    instance = ChildClass()
    print(instance.public)

    try:
        print(instance.__private)
    except AttributeError:
        print("raised AttributeError accessing __private")


if __name__ == "__main__":
    _accessing_private_method_raises_exception()
    _private_attributes_can_be_accessed_via_new_name()
    _class_methods_can_access_private_attributes()
    _subclass_cannot_access_parent_private_attribute()

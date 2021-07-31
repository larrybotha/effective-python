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
def _prefer_public_attributes_over_getters_and_setters():
    class MyClassWithSetterAndGetter:
        def __init__(self):
            self._some_value = 5

        def get_some_value(self):
            return self._some_value

        def set_some_value(self, value):
            self._some_value = value

            return self._some_value

    class MyClassWithPublicAttributes:
        def __init__(self):
            self.some_value = 5

    instance_1 = MyClassWithSetterAndGetter()
    string_1 = "instance_1.get_some_value()"
    string_2 = "instance_1.set_some_value(10)"

    print(f"{string_1}: {eval(string_1)}")
    print(f"{string_2}: {eval(string_2)}")

    instance_2 = MyClassWithPublicAttributes()
    string_1 = "instance_2.some_value"
    string_2 = "instance_2.some_value = 10"

    print(f"{string_1}: {eval(string_1)}")
    instance_2.some_value = 10
    print(f"{string_2}: {instance_2.some_value}")


@_print_fn
def _starting_with_public_attributes_allows_one_to_migrate_to_property_decorator():
    class MyClass:
        def __init__(self, value):
            self.value = value

    print("MyClass with public attribute")
    instance_1 = MyClass(5)
    string_1 = "instance_1.value"
    print(f"{string_1}: {eval(string_1)}")

    instance_1.value = 10
    string_2 = "instance_1.value"

    print(f"{string_2}: {eval(string_2)}")

    # later in time...
    class MyClass:
        def __init__(self, value):
            self._value = value

        @property
        def value(self):
            return self._value

        @value.setter
        def value(self, value):
            self._value = value

    print("\nMyClass with @property attribute")
    instance_1 = MyClass(5)
    string_1 = "instance_1.value"
    print(f"{string_1}: {eval(string_1)}")

    instance_1.value = 10
    string_2 = "instance_1.value"

    print(f"{string_2}: {eval(string_2)}")


@_print_fn
def _property_decorator_allows_for_side_effects():
    class PropertyAndSideEffect:
        def __init__(self, value):
            self._value = value
            self.something = self._value * 2

        @property
        def value(self):
            return self._value

        @value.setter
        def value(self, value):
            self._value = value
            # side effect
            print("side effect after setting value!")
            self.something = self._value * 2

    instance = PropertyAndSideEffect(5)

    string_1 = "instance.value"
    string_2 = "instance.something"
    print(f"{string_1}: {eval(string_1)}")
    print(f"{string_2}: {eval(string_2)}\n")

    instance.value = 10
    print(f"{string_1}: {eval(string_1)}")
    print(f"{string_2}: {eval(string_2)}")


@_print_fn
def _setter_property_can_be_used_for_validation():
    class Natural:
        def __init__(self, value=1, /):
            # use the setter to set the value
            self.value = value

        @property
        def value(self):
            return self._value

        @value.setter
        def value(self, value: int):
            if value < 1:
                raise ValueError("cannot be less than 1")

            self._value = value

    natural = Natural()

    string_1 = "natural.value"
    print(f"{string_1}: {eval(string_1)}")

    try:
        print("\nattempt to set value < 1")
        natural.value = 0
    except ValueError as error:
        print(f"\nError: {error.__class__.__name__}")
        print(error)

    try:
        print("\ninstantiate with value < 1")
        natural = Natural(0)
    except ValueError as error:
        print(f"\nError: {error.__class__.__name__}")
        print(error)


@_print_fn
def _property_can_be_used_to_make_parent_attribute_immutable():
    class Parent:
        def __init__(self, value):
            self.value = value

    class ImmutableChild(Parent):
        @property
        def value(self):
            return self._value

        @value.setter
        def value(self, value):
            # this will be false on initialisation, resulting in the value
            # passed into __init__ being assigned
            if hasattr(self, "_value"):
                raise AttributeError("value is immutable")

            self._value = value

    print("instantiating ImmutableChild - value will be set\n")
    immutable = ImmutableChild(5)

    try:
        print(
            "attribute is set at instantiation, now immutable - error will be raised\n"
        )
        immutable.value = 10
    except AttributeError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    _prefer_public_attributes_over_getters_and_setters()
    _starting_with_public_attributes_allows_one_to_migrate_to_property_decorator()
    _property_decorator_allows_for_side_effects()
    _setter_property_can_be_used_for_validation()
    _property_can_be_used_to_make_parent_attribute_immutable()

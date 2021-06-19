from datetime import datetime
from inspect import stack
from time import sleep
from typing import Optional


def _cr():
    print("")


def _div(text: Optional[str] = "", print_caller: bool = True):
    fn_name = stack()[1][3] if print_caller else None

    print("================")

    if text or fn_name:
        print(text or fn_name)
        _div(print_caller=False)


def _dynamic_parameters_are_instantiated_only_once():
    _div()

    def fn_with_dynamic_default_arg(when: datetime = datetime.now()):
        """fn_with_dynamic_default_arg.

        when will always be the same value

        :param when:
        :type when: datetime
        """
        return when

    t1 = fn_with_dynamic_default_arg()
    print(f"assigned t1: {t1}")
    sleep(0.25)
    print(f"sleeping .25s")
    t2 = fn_with_dynamic_default_arg()
    print(f"assigned t2: {t2}")

    string = "t1 == t2"
    print(f"{string}: {eval(string)}")

    _cr()


def _use_none_and_docstring_for_default_dynamic_values():
    _div()

    def fn_with_dynamic_default_arg(when: datetime = None):
        """_use_none_and_docstring_for_default_dynamic_values

        Args:
            when: time to return. defaults to current time

        :param when:
        :type when: datetime
        """
        if when is None:
            when = datetime.now()
        return when

    t1 = fn_with_dynamic_default_arg()
    print(f"assigned t1: {t1}")
    sleep(0.25)
    print(f"sleeping .25s")
    t2 = fn_with_dynamic_default_arg()
    print(f"assigned t2: {t2}")

    string = "t1 == t2"
    print(f"{string}: {eval(string)}")

    _cr()


def _dont_assign_mutable_values_as_defaults():
    _div()

    def fn_with_default_arg(json={}):
        try:
            raise ValueError("oh no!")
        except ValueError:
            return json

    j1 = fn_with_default_arg()
    print(j1)
    print(f"j1: {j1}")

    print("assign key to j1")
    j1.setdefault("foo", "bar")
    print(j1)
    print(f"j1: {j1}")

    j2 = fn_with_default_arg()
    print(f"j2: {j2}")

    string = "id(j1) == id(j2)"
    print(f"{string}: {eval(string)}")

    _cr()


def _use_none_and_docstring_for_mutabble_defaults():
    _div()

    def fn_with_default_arg(json=None):
        try:
            raise ValueError("oh no!")
        except ValueError:
            if json is None:
                json = {}

        return json

    j1 = fn_with_default_arg()
    print(j1)
    print(f"j1: {j1}")

    print("assign key to j1")
    j1.setdefault("foo", "bar")
    print(j1)
    print(f"j1: {j1}")

    j2 = fn_with_default_arg()
    print(f"j2: {j2}")

    string = "id(j1) == id(j2)"
    print(f"{string}: {eval(string)}")

    _cr()


if __name__ == "__main__":
    _dynamic_parameters_are_instantiated_only_once()
    _use_none_and_docstring_for_default_dynamic_values()
    _dont_assign_mutable_values_as_defaults()
    _use_none_and_docstring_for_mutabble_defaults()

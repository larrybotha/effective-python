import random
import traceback
from inspect import stack
from typing import Callable, Optional


def _cr():
    print("")


def _div(text: Optional[str] = "", print_caller: bool = True):
    fn_name = stack()[1][3] if print_caller else None

    print("================")

    if text or fn_name:
        print(text or fn_name)
        _div(print_caller=False)


def _max_str_length(*args):
    return max([len(x) for x in args])


def _my_sum(first: int, second: int):
    return first + second


def _any_keywords(**kwargs):
    print("------------------------------------")
    print(f"_any_keywords received:\n\t{kwargs}")
    print("------------------------------------")


def _try_print(error_class, fn: Callable) -> None:
    try:
        _ = fn()
    except error_class:
        _cr()
        print("---------------------------------------")
        print(f"caught {error_class.__name__}:\n\n {traceback.format_exc(limit=0)}")


def _positioned_or_keywords():
    _div()

    string1 = "_my_sum(1, 2)"
    string2 = "_my_sum(first = 1, second = 2)"

    str_width = _max_str_length(string1, string2)

    print(f"{string1:<{str_width}} => {eval(string1)}")
    print(f"{string2:<{str_width}} => {eval(string2)}")

    _cr()


def _order_of_keyword_arguments_doesnt_matter():
    _div()

    string1 = "_my_sum(first = 1, second = 2)"
    string2 = "_my_sum(second = 2, first = 1)"

    str_width = _max_str_length(string1, string2)

    print(f"{string1:<{str_width}} => {eval(string1)}")
    print(f"{string2:<{str_width}} => {eval(string2)}")

    _cr()


def _keyword_arguments_always_after_positioned_arguments():
    _div()

    string = "_my_sum(1, second = 2)"

    print(f"{string} => {eval(string)}")

    _cr()


def _keywords_before_positioned_will_raise():
    _div()

    string = "_my_sum(first = 1, 2)"

    print(f"attempting: {string}")
    print(f"{string} => {eval(string)}")

    _cr()


def _keywords_may_only_be_specified_once():
    _div()

    string = "_my_sum(first = 1, first = 2, second = 2)"

    print(f"attempting: {string}")
    print(f"{string} => {eval(string)}")

    _cr()


def _kwargs_as_argument():
    _div()

    my_kwargs = {"first": 1, "second": 2}
    string = "_my_sum(**my_kwargs)"

    print(f"my_kwargs: {my_kwargs}")
    print(f"{string} => {eval(string)}")

    _cr()


def _mixed_kwargs_and_keywords():
    _div()

    my_kwargs = {"first": 1}
    string = "_my_sum(**my_kwargs, second = 2)"

    print(f"my_kwargs: {my_kwargs}")
    print(f"{string} => {eval(string)}")

    _cr()


def _multiple_kwargs():
    _div()

    kwargs_1 = {"first": 1}
    kwargs_2 = {"second": 2}
    string = "_my_sum(**kwargs_1, **kwargs_2)"

    print(f"kwargs_1: {kwargs_1}")
    print(f"kwargs_2: {kwargs_2}")
    print(f"{string} => {eval(string)}")

    _cr()


def _kwargs_may_not_overlap_keywords():
    _div()

    kwargs = {"first": 1, "second": 2}
    string = "_my_sum(**kwargs, second = 2)"

    print(f"kwargs: {kwargs}")
    print(f"attempting: {string}")
    print(f"{string} => {eval(string)}")

    _cr()


def _kwargs_may_not_overlap_kwargs():
    _div()

    kwargs_1 = {"first": 1}
    kwargs_2 = {"first": 1, "second": 2}
    string = "_my_sum(**kwargs_1, **kwargs_2)"

    print(f"kwargs_1: {kwargs_1}")
    print(f"kwargs_2: {kwargs_2}")
    print(f"attempting: {string}")
    print(f"{string} => {eval(string)}")

    _cr()


def _accepting_arbitrary_keyword_arguments_as_keyword_arguments():
    _div()

    string = "_any_keywords(first = 1, second = 2)"

    print(f"calling: {string}")
    eval(string)

    _cr()


def _accepting_arbitrary_keyword_arguments_as_dict():
    _div()

    ord_a = ord("a")
    my_dict = {chr(ord_a + random.randint(0, 26)): k for k in range(5)}

    string = "_any_keywords(**my_dict)"

    print(f"my_dict: {my_dict}")
    print(f"calling: {string}")
    eval(string)

    _cr()


def _using_default_values_for_keyword_arguments():
    _div()

    def _my_func(first: int = 1, second: int = 2):
        return _my_sum(first, second)

    string = "_my_func(second = 2)"

    print(f"{string}: {eval(string)}")

    _cr()


if __name__ == "__main__":
    _positioned_or_keywords()
    _order_of_keyword_arguments_doesnt_matter()
    _keyword_arguments_always_after_positioned_arguments()
    _try_print(SyntaxError, _keywords_before_positioned_will_raise)
    _try_print(SyntaxError, _keywords_may_only_be_specified_once)
    _kwargs_as_argument()
    _mixed_kwargs_and_keywords()
    _multiple_kwargs()
    _try_print(TypeError, _kwargs_may_not_overlap_keywords)
    _try_print(TypeError, _kwargs_may_not_overlap_kwargs)
    _accepting_arbitrary_keyword_arguments_as_keyword_arguments()
    _accepting_arbitrary_keyword_arguments_as_dict()
    _using_default_values_for_keyword_arguments()

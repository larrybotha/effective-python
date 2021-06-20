import traceback
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


def _handle_overflow(error: OverflowError, ignore: Optional[bool]):
    if ignore:
        return 0
    else:
        raise error


def _handle_div_by_zero(error: ZeroDivisionError, allow: Optional[bool]):
    if allow:
        return float("inf")
    else:
        raise error


def _safe_divide_mixed():
    _div()

    # all arguments must be passed, always
    # can be confusing when calling using positional arguments which boolean is
    # at which position
    def divide(
        numerator: float,
        denominator: float,
        allow_zero_denominator: bool,
        ignore_overflow: bool,
    ):
        try:
            return numerator / denominator
        except OverflowError as error:
            _handle_overflow(error, ignore_overflow)

        except ZeroDivisionError as error:
            _handle_div_by_zero(error, allow_zero_denominator)

    string = "divide(1, 0, False, True)"
    try:
        print(f"attempting: {string}")
        print(f"{string} => {eval(string)}")

    except ZeroDivisionError:
        print("\nerror raised:")
        print(traceback.format_exc(limit=0))

    _cr()


def _safe_divide_default_throw():
    _div()

    # flags are now optional, and  users can override them if they want
    #
    # users can still, however, use keywords, or positional arguments
    def divide(
        numerator: float,
        denominator: float,
        allow_zero_denominator: bool = False,
        ignore_overflow: bool = False,
    ):
        try:
            return numerator / denominator
        except OverflowError as error:
            _handle_overflow(error, ignore_overflow)

        except ZeroDivisionError as error:
            _handle_div_by_zero(error, allow_zero_denominator)

    string = "divide(1, 0)"
    try:
        print(f"attempting: {string}")
        print(f"{string} => {eval(string)}")

    except ZeroDivisionError:
        print("\nerror raised:")
        print(traceback.format_exc(limit=0))

    _cr()


def _safe_divide_enforce_keywords():
    _div()

    # flags are optional, but only overridable using keywords
    def divide(
        numerator: float,
        denominator: float,
        *,
        allow_zero_denominator: bool = False,
        ignore_overflow: bool = False,
    ):
        try:
            return numerator / denominator
        except OverflowError as error:
            _handle_overflow(error, ignore_overflow)

        except ZeroDivisionError as error:
            _handle_div_by_zero(error, allow_zero_denominator)

    string = "divide(1, 0, False, True)"
    try:
        print(f"attempting: {string}")
        print(f"{string} => {eval(string)}")

    except ZeroDivisionError:
        print("\nerror raised:")
        print(traceback.format_exc(limit=0))

    except TypeError:
        print("\nerror raised:")
        print(traceback.format_exc(limit=0))

    _cr()


def _safe_divide_enforce_position_and_keywords():
    _div()

    # flags are optional, but only overridable using keywords
    def divide(
        numerator: float,
        denominator: float,
        /,
        *,
        allow_zero_denominator: bool = False,
        ignore_overflow: bool = False,
    ):
        try:
            return numerator / denominator
        except OverflowError as error:
            _handle_overflow(error, ignore_overflow)

        except ZeroDivisionError as error:
            _handle_div_by_zero(error, allow_zero_denominator)

    string = "divide(numerator = 1, denominator = 0)"
    try:
        print(f"attempting: {string}")
        print(f"{string} => {eval(string)}")

    except ZeroDivisionError:
        print("\nerror raised:")
        print(traceback.format_exc(limit=0))

    except TypeError:
        print("\nerror raised:")
        print(traceback.format_exc(limit=0))

    _cr()


if __name__ == "__main__":
    _safe_divide_mixed()
    _safe_divide_default_throw()
    _safe_divide_enforce_keywords()
    _safe_divide_enforce_position_and_keywords()

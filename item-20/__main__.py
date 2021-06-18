import traceback
from inspect import stack
from typing import Optional, Tuple


def _cr():
    print("")


def _div(text: Optional[str] = "", print_caller: bool = True):
    fn_name = stack()[1][3] if print_caller else None

    print("================")

    if text or fn_name:
        print(text or fn_name)
        _div(print_caller=False)


def _avoid_returning_none_as_falsy():
    _div()

    def _zero_division_falsy(num: float, den: float) -> Tuple[bool, float]:
        """_zero_division_falsy.

        This should raise an exception. None is not float - don't return none when
        someone expects float - raise an error

        A return signature helps here, too

        :param num:
        :type num: float
        :param den:
        :type den: float
        """
        try:
            return True, num / den
        except ZeroDivisionError:
            return False, None

    q1Valid, q1 = _zero_division_falsy(2, 0)
    print(f"q1: {q1Valid, q1} from 2 / 0")

    if not q1:
        print(f'evaluating "not q1 ({q1})" gets us here')

    _cr()

    q2Valid, q2 = _zero_division_falsy(0, 2)
    print(f"q2: {q2Valid, q2} from 0 / 2")

    if not q2:
        print(f'evaluating "not q2 ({q2})" gets us here')

    _cr()


def _raise_errors_for_special_cases():
    _div()

    def _zero_division_raises(x: float, y: float) -> float:
        """_zero_division_raises.

        Raises:
          ValueError: When dividing by zero

        :param x:
        :type x: float
        :param y:
        :type y: float
        :rtype: float
        """
        try:
            return x / y
        except ZeroDivisionError:
            raise ValueError("Invalid inputs")

    try:
        result = _zero_division_raises(2, 0)
    except ValueError:
        # this  error should likely be raised, otherwise anything consuming this
        # function will not know there was an issue, making it very difficult to
        # debug
        print("Invalid inputs")
    else:
        print(result)

    _cr()


def _raise_without_explicit_exception_chaining():
    _div()

    def _zero_division_raises_not_chained(x: float, y: float) -> float:
        try:
            return x / y
        except ZeroDivisionError:
            raise ValueError("Invalid inputs")

    _zero_division_raises_not_chained(2, 0)
    _cr()


def _raise_with_explicit_exception_chaining():
    _div()

    def _zero_division_raises_chained(x: float, y: float) -> float:
        try:
            return x / y
        except ZeroDivisionError as error:
            raise ValueError("Invalid inputs") from error

    _zero_division_raises_chained(2, 0)
    _cr()


if __name__ == "__main__":
    _avoid_returning_none_as_falsy()
    _raise_errors_for_special_cases()

    try:
        _raise_with_explicit_exception_chaining()
    except ValueError as error:
        print(error)
        print(f"cause: {error.__cause__}")
        print("error.__cause__ information is retained")
        print("-----------------------------------")
        traceback.print_tb(error.__traceback__)
        print("-----------------------------------")

    _cr()

    try:
        _raise_without_explicit_exception_chaining()
    except ValueError as error:
        print(error)
        print(f"cause: {error.__cause__}")
        print("error.__cause__ information is lost")
        print("-----------------------------------")
        tb = traceback.print_tb(error.__traceback__)
        print("-----------------------------------")

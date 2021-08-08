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
def _property_not_good_for_reuse():
    class Homework:
        def __init__(self):
            self._grade = 0

        @property
        def grade(self):
            return self._grade

        @grade.setter
        def grade(self, value: int, /):
            """grade.

            validate that the homework's grade is between 0 and 100

            :param value:
            :type value: int
            """
            if not (0 <= value <= 100):
                raise ValueError("grade must be between 0 and 100")

            self._grade = value

        def __repr__(self):
            return f"Homework(grade={self.grade})"

    kid_a_homework = Homework()
    kid_a_homework.grade = 60

    print(kid_a_homework)


if __name__ == "__main__":
    _property_not_good_for_reuse()

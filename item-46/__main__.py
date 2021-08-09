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
def _property_ok_for_single_use():
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


@_print_fn
def _property_not_good_for_general_use():
    class Exam:
        def __init__(self):
            self._writing_grade = 0
            self._math_grade = 0

        def __repr__(self):
            return f"Exame(writing_grade={self.writing_grade}, math_grade={self.math_grade})"

        @staticmethod
        def check_grade(grade: int, /):
            if not (0 <= grade <= 100):
                raise ValueError("grade must be between 0 and 100")

        # using @property we repeat the getters and setters here - this is
        # tedious for an arbitrary number of items
        @property
        def writing_grade(self):
            return self._writing_grade

        @writing_grade.setter
        def writing_grade(self, grade: int, /):
            self.check_grade(grade)
            self._writing_grade = grade

        @property
        def math_grade(self):
            return self._math_grade

        @math_grade.setter
        def math_grade(self, grade: int, /):
            self.check_grade(grade)
            self._math_grade = grade

    kid_a_exam = Exam()
    kid_a_exam.writing_grade = 60
    kid_a_exam.math_grade = 50

    print(kid_a_exam)

    print(f"\nlots of repetition here to define different subjects")


if __name__ == "__main__":
    _property_ok_for_single_use()
    _property_not_good_for_general_use()

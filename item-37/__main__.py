import random
from collections import defaultdict, namedtuple
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
def _complex_nested_dicts():
    class ComplexNestedGradeBook:
        def __init__(self):
            """make _grades private"""
            self._grades = {}

        def add_student(self, name: str, /):
            """
            here we have a nested dict - this should be a warning sign that a
            class should be used instead
            """
            self._grades[name] = defaultdict(list)

            return self

        def add_grade(
            self, *, name: str, subject_name: str, grade: float, weight: float
        ):
            subject = self._grades[name][subject_name]
            """tuples are positional
            If we need more data with this tuple, we'd have to append the item
            to the end of the tuple, and refactor other locations in the code
            using this value with positional arguments

            Consider using a namedtuple if the value is never going to be
            accessed by anyone else, otherwise use a class to describe the new
            object
            """
            subject.append((grade, weight))

            return self

        def get_average_grade(self, name: str, /):
            subject_grades = self._grades[name].values()
            grades = []

            """loop within a loop - O(n^2), and difficult to read"""
            for (i, xs) in enumerate(subject_grades):
                print(f"subject: {list(self._grades[name].keys())[i]}")

                subject_totals = []

                for (grade, weight) in xs:
                    subject_totals = subject_totals + [(grade * weight)]

                print(f"subject grades: {subject_totals}\n")
                grades = grades + subject_totals

            return sum(grades) / len(grades)

    ord_a = ord("a")
    student_name = "foo"
    grades = [
        (chr(x % 2 + ord_a), random.randint(0, 100), random.randint(1, 100) / 100)
        for x in range(4)
    ]
    grade_book = ComplexNestedGradeBook()
    grade_book.add_student(student_name)

    print(f"student: {student_name}")
    print(f"grades: {grades}\n")

    for (subject, grade, weight) in grades:
        grade_book.add_grade(
            name=student_name, subject_name=subject, grade=grade, weight=weight
        )

    student_average = grade_book.get_average_grade(student_name)

    print(f"student average: {student_average}")


@_print_fn
def _named_tuple():
    """this namedtuple could be mistaken for a class"""
    MyTuple = namedtuple("MyTuple", ["value_a", "value_b"])
    a = MyTuple(1, 2)

    print(a)
    print(f"a.value: {a.value_a}")
    print(f"b.value: {a.value_b}")


if __name__ == "__main__":
    _complex_nested_dicts()
    _named_tuple()

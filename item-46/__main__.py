from functools import wraps
from itertools import repeat
from random import randint
from weakref import WeakKeyDictionary


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
            return f"Exam(writing_grade={self.writing_grade}, math_grade={self.math_grade})"

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


@_print_fn
def _descriptor_example():
    class MyDescriptor:
        def __init__(self, value=0, /):
            self._value = value

        def __get__(self, instance, instance_type):
            print("getting value")
            print(f"instance: {instance}")
            print(f"instance_type: {instance_type.__name__}\n")

            return self._value

        def __set__(self, instance, value):
            print(f"setting value: {value}")
            print(f"instance: {instance}\n")
            self._value = value

    class MyClass:
        some_value = MyDescriptor()

    instance = MyClass()

    print(f"instance.some_value: {instance.some_value}\n")

    instance.some_value = 5


@_print_fn
def _careful_of_class_attributes_sharing_values():
    class MyDescriptor:
        def __init__(self, value: str = "foo", /):
            self._value = value

        def __get__(self, *_):
            return self._value

        def __set__(self, _, value: str):
            self._value = value

    class MyClass:
        class_attr = MyDescriptor()

        def __repr__(self):
            return f"{self.__class__.__name__}(class_attr: {self.class_attr})"

    instance_1 = MyClass()
    instance_2 = MyClass()

    print(f"instance_1: {instance_1}")
    print(f"instance_2: {instance_2}\n")

    print("setting instance_1.class_attr = 'bar'\n")
    instance_1.class_attr = "bar"

    print(f"instance_1: {instance_1.class_attr}")
    print(f"instance_2: {instance_2.class_attr}\n")

    print("instance_2.class_attr changed!")


@_print_fn
def _memory_leaking_implementation_with_dict():
    class Grade:
        def __init__(self):
            # create a dict that we can dynamically assign grades for each
            # instance to
            self._values = {}

        def __get__(self, instance, _):
            # if there's no instance, return the descriptor
            if instance is None:
                return self

            # from the descriptor's _values attribute, get the value at the key
            # `instance`, otherwise 0
            return self._values.get(instance, 0)

        def __set__(self, instance, value):
            if not (0 <= value <= 100):
                return ValueError("grade must be between 0 and 100")

            # Set the grade on the _values dict using the instance as the key
            # _values will hold a reference to each instance, even after the
            # instance is no longer needed. This prevents the garbage collector
            # from cleaning up, resulting in a memory leak - the instances will
            # persist for the duration of the application running
            print(
                "reference to instance created in descriptor - memory leak introduced"
            )
            self._values[instance] = value

    class Student:
        math_grade = Grade()

    student_1 = Student()
    student_2 = Student()

    student_1.math_grade = randint(0, 100)
    student_2.math_grade = randint(0, 100)

    print(f"\nstudent 1 math: {student_1.math_grade}")
    print(f"student 2 math: {student_2.math_grade}")


@_print_fn
def _memory_safe_implementation_with_weakkeydictionary():
    class Grade:
        def __init__(self):
            print("WeakKeyDictionary instantiated - values will be garbage collected")
            self._values = WeakKeyDictionary()

        def __get__(self, instance, _):
            if instance is None:
                return self

            self._values.get(instance, 0)

        def __set__(self, instance, value):
            if not (0 <= value <= 100):
                raise ValueError("grade must be between 0 and 100")

            self._values[instance] = value

    class Student:
        math_grade = Grade()

    student_1 = Student()
    student_2 = Student()

    student_1.math_grade = randint(0, 100)
    student_2.math_grade = randint(0, 100)

    print(f"\nstudent 1 math: {student_1.math_grade}")
    print(f"student 2 math: {student_2.math_grade}")


if __name__ == "__main__":
    _property_ok_for_single_use()
    _property_not_good_for_general_use()
    _descriptor_example()
    _careful_of_class_attributes_sharing_values()
    _memory_leaking_implementation_with_dict()
    _memory_safe_implementation_with_weakkeydictionary()

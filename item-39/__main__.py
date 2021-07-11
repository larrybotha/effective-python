import os
import random
from functools import wraps
from itertools import repeat
from threading import Thread
from typing import Generic, List, Type, TypeVar


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


class _InputData:
    """_InputData.

    An interface for reading data from different sources
    """

    def read(self):
        raise NotImplementedError


class _PathInputData(_InputData):
    """_PathInputData.

    A class for reading input data from a file
    """

    def __init__(self, path: str, /):
        super().__init__()
        self.path = path

    def read(self) -> str:
        with open(self.path) as f:
            return f.read()


class _GenericInputData:
    def read(self):
        raise NotImplementedError

    @classmethod
    def generate_inputs(cls, config):
        raise NotImplementedError


class _PathInputDataFromGeneric(_GenericInputData):
    def __init__(self, path: str, /):
        super().__init__()
        self.path = path

    def read(self) -> str:
        with open(self.path) as f:
            return f.read()

    @classmethod
    def generate_inputs(cls, config):
        data_dir = config["data_dir"]

        for name in os.listdir(data_dir):
            yield cls(os.path.join(data_dir, name))


class _MapReduceWorker:
    """_MapReduceWorker.

    An interface for mapping and reducing data from an _InputData source
    """

    def __init__(self, input_data: _InputData, /):
        self.input_data = input_data
        self.result = None

    def map(self):
        raise NotImplementedError

    def reduce(self, other: "_MapReduceWorker"):
        raise NotImplementedError


class _GenericMapReduceWorker:
    def __init__(self, input_data: _InputData, /):
        self.input_data = input_data
        self.result = None

    def map(self):
        raise NotImplementedError

    def reduce(self, other: "_GenericMapReduceWorker"):
        raise NotImplementedError

    @classmethod
    def create_workers(cls, input_class: Type[_GenericInputData], config):
        workers = []

        for input_data in input_class.generate_inputs(config):
            workers.append(cls(input_data))

        return workers


class _LineCounterMapReduceWorker(_MapReduceWorker):
    def map(self):
        data = self.input_data.read()
        # this is class expects the concrete class implements that _InputData
        # interface too return a string... we have a tight coupling
        self.result = data.count("\n")

    # right here we're expecting to receive another instance of this class
    def reduce(self, other: "_LineCounterMapReduceWorker", /):
        self.result = self.result + other.result


class _LineCounterFromGenericMapReduceWorker(_GenericMapReduceWorker):
    def map(self):
        data = self.input_data.read()
        self.result = data.count("\n")

    def reduce(self, other: "_LineCounterFromGenericMapReduceWorker", /):
        self.result = self.result + other.result


def _generate_inputs(dir_path: str):
    """_generate_inputs.

    This function is tightly coupled with _PathInputData, which is a class
    derived from another class. We can't use instances of other classes in this
    function. We could either allow this function to handle arbitrary classes,
    or allow these classes to generically handle creation of themselves using a
    classmethod / factory function approach

    :param dir_path:
    :type dir_path: str
    """
    for name in os.listdir(dir_path):
        yield _PathInputData(os.path.join(dir_path, name))


def _create_map_reducers(input_data_list: List[_InputData]):
    """_create_map_reducers.

    This function is tightly coupled with the _LineCounterMapReduceWorker class.
    Either that class should be passed in to create workers, or this function can
    be removed after adding a classmethod to _LineCounterMapReduceWorker that
    allows the class to instantiate a list of workers itself

    :param input_data_list:
    :type input_data_list: List[_InputData]
    """
    workers = []

    for input_data in input_data_list:
        workers.append(_LineCounterMapReduceWorker(input_data))

    return workers


def _execute_workers(workers: List[_MapReduceWorker], /):
    threads = [Thread(target=worker.map) for worker in workers]

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    first, *rest = workers
    for worker in rest:
        first.reduce(worker)

    return first.result


def _write_test_files(path: str):
    if not os.path.exists(path):
        os.makedirs(path)

    for x in range(10):
        file = os.path.join(path, f"{x}.txt")

        with open(file, "w") as handle:
            handle.write("\n" * random.randint(1, 10))


def _generate_test_files(path: str):
    files_dir = os.path.join(os.path.dirname(__file__), path)
    _write_test_files(files_dir)


def _get_abs_path(path: str):
    return os.path.join(os.path.dirname(__file__), path)


@_print_fn
def _without_classmethod_polymorphism():
    def mapreduce(data_dir: str):
        input_data_list = _generate_inputs(data_dir)
        workers = _create_map_reducers(list(input_data_list))

        return _execute_workers(workers)

    data_dir = _get_abs_path("test-files")

    _generate_test_files(data_dir)

    result = mapreduce(data_dir)

    print(f"There are {result} newlines in the files in {os.path.curdir}/{dir}")


@_print_fn
def _with_classmethod_polymorphism():
    def mapreduce(
        worker_class: Type[_GenericMapReduceWorker],
        input_class: Type[_GenericInputData],
        data_dir,
        /,
    ):
        config = {"data_dir": data_dir}
        workers = worker_class.create_workers(input_class, config)

        return _execute_workers(workers)

    data_dir = _get_abs_path("test-files")

    _generate_test_files(data_dir)
    result = mapreduce(
        _LineCounterFromGenericMapReduceWorker,
        _PathInputDataFromGeneric,
        data_dir,
    )

    print(f"There are {result} newlines in the files in {os.path.curdir}/{dir}")


T = TypeVar("T")


@_print_fn
def _create_instances_with_classmethod():
    class MyClass(Generic[T]):
        def __init__(self, value: T, /):
            self.value = value
            print(f"{self.__class__.__name__} instance created with __init__")

        @classmethod
        def generate(cls, values: List[T], /):
            for value in values:
                print(f"{cls.__name__} instance created with .generate")
                yield cls(value)

    print("normal instantiation")
    instance = MyClass("foo")
    print(instance.value)

    print("\nclassmethod instantiation")
    instances = MyClass.generate(["bar", "baz"])

    for inst in instances:
        print(inst.value)


if __name__ == "__main__":
    _create_instances_with_classmethod()
    _without_classmethod_polymorphism()
    _with_classmethod_polymorphism()

# Item 39 - Constructing objects generically using `@classmethod` polymorphism

```shell
$ python3 ./
```

- for type annotations containing types that are not yet defined, such as a
    class referring to itself, one can use a string to represent the type:

    ```python
    class Tree:
        def __init__(self, left: 'Tree', right: 'Right'):
            self.left = left
            self.right = right
    ```
    - this is known as a [Forward References][forward-reference]
- for type annotations of functions that accept classes, `Type` must be used:

    ```python
    from typing import Type

    class MyClass:
        pass

    def my_func(cls: Type[MyClass]):
        pass
    ```
- work can be distributed across threads using `Thread`:

    ```python
    from threading import Thread

    threads = [
        Thread(target=some_obj.some_method) for some_obj in my_objects
    ]

    for thread in threads: thread.start()
    for thread in threads: thread.join()
    ```
- interfaces for classes can be created using `NotImplementedError` for methods
    that need to be implemented by concrete classes:

    ```python
    class MyInterface:
        def do_something(self):
            raise NotImplementedError

    class MyConcreteClass(MyInterface):
        def __init__(self):
            super().__init__()

        def do_something(self):
            print('doing something!')
    ```

    - this is instance method polymorphism
- Python only allows for a single `__init__` method in classes
- `@classmethod` allows for a method to be called on a class or an instance. If
    it is called on the class, the first argument inside the method represents
    the class itself (as opposed to the instance for instance methods)
    - `@classmethod` is not the same as a static method in other languages -
        there's a separate `@staticmethod` decorator for creating static methods
        as in other languages
- `@classmethod` can be used to instantiate objects with a function other than
    the `__init__` constructor, similar to a factory function:

    ```python
    class MyClass:
        def __init__(self, value):
            self.value = value

        @classmethod
        def create_multple(cls, xs):
            for x in xs:
                yield cls(x)

    instance = MyClass("foo")
    instances = MyClass.create(['foo', 'bar'])
    ```
- a `@classmethod` defined on a base class, and called on a derived class, will
    pass the derived class as a parameter

## Resources

- [Forward References][forward-reference]

<!-- LINKS -->
[forward-reference]:
    https://www.python.org/dev/peps/pep-0484/#forward-references
    "Forward references"

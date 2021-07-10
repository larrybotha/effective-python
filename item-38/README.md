# Item 38 - Accept functions instead of classes for simple interfaces

```shell
$ python3 ./
```

- methods like `List.sort` accept sorting functions as parameters:

    ```python
    from random import shuffle

    xs = shuffle(['abc', 'a', 'ab'])

    # sort by length
    xs.sort(key=len)
    # ['a', 'ab', 'abc']
    ```
- `collections.defaultdict` requires its first argument to be a function that
    accepts no arguments, and returns a default value when key access on
    non-existent keys occurs:

    ```python
    from collections import defaultdict

    def get_default():
        return 0

    some_obj = {'a': 1, 'b': 2}
    my_obj = default_dict(get_default, some_obj)

    my_obj['c']
    # c => 0
    ```
- one can manage state from side effects using a class:

    ```python
    from collections import defaultdict

    class CountMissing():
        def __init__(self, default, /):
            self.count = 0
            self.default = default

        def missing(self):
            self.count = self.count + 1

            return self.default

    count_missing_thing = CountMissing('foo')
    my_dict = defaultdict(count_missing_thing.missing)
    print(my_dict['a'])
    print(my_dict['b'])

    print(count_missing_thing.count)
    # 2
    ```

    - this is awkward, though - what is a `CountMissing`? Without using
        `defaultdict` this class is difficult to understand what it's for, and
        difficult to name meaningfully
- Python allows for instances of classes to be callable. This is done using the
    `__call__` method:

    ```python
    class MyCallableClass:
        def __call__(self):
            print('called!')

    my_callable = MyCalllableClass()

    my_callable()
    # called!

    my_callable()
    # called!
    ```
- Python has a builtin function, `callable`, which returns `True` for objects
    that can be called like functions. Using the `__call__` special method in
    classes makes them callable:

    ```python
    class MyCallable():
        def __call__():
            pass

    c = MyCallable()

    callable(c)
    # True
    ```
- when you need to manage side effects or state in callbacks, consider using a
    callable class

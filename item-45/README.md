# Item 45 - Use `@property` to add behaviour to attributes without breaking changes

```shell
$ python3 ./
```

- the Javascript equivalent of `Date.now()` in Python is
    `datetime.datetime.now()`
- `datetime.timedelta` is useful for managing time deltas, rather than relying
    on an integer
- `getattr` and `setattr` can be used to dynamically get or set values on a
    class:

    ```python
    class MyClass:
        def __init__(self):
            self.some_value = 0

        def print(self):
            print(getattr(self, 'some_value'))
    ```
- one can use `@property` to patch classes:

    ```python
    class MyBadClass:
        def __init__(self, value: int, /):
            self.value = value
            # only set when initialised
            self._value_squared = self.value ** 2

    class MyPatchedClass(MyBadClass):
        def __init__(self, value: int, /):
            super().__init__(value)
            self._value = value

        @property
        def value(self):
            return self._value

        @value.setter
        def value(self, value: int, /):
            self._value = value
            # set _value_squared when value is changed
            # NOTE: this is a side effect - it would be better to use a method
            # to do this
            self._value_squared = self.value ** 2
    ```
- repeated use of `@property` in a class likely indicates the class should be
    rewritten
- `@property` is useful for incrementally adding behaviour to a class

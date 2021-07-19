# Item 40 - `super` for initialising parent classes

```shell
$ python3 ./
```

- multiple inheritance should be avoided (favour composition over inheritance)
- classes making use of multiple inheritance have multiple values in the class
    definition:

    ```python
    class One:
        pass

    class Two:
        pass

    class Multiple(One, Two):
        pass
    ```
- diamon inheritance is when a multiple inheritance results in a subclass
    inheriting from 2 or more classes that share a parent

    ```python
    class BaseClass:
        def __init__(self, value):
            self.value = value

    class LeftClass(BaseClass):
        def __init__(self, value):
            self.left = value

    class RightClass(BaseClass):
        def __init__(self, value);
            self.right = value

    class Both(LeftClass, RightClass):
        def __init__(self, value):
            super().__init__(value)
    ```
- the order of initialisation of inherited classes is defined by MRO - method
    resolution order. To see a class's MRO:

    ```python
    mro_string = "\n".join(repr(cls) for cls in SomeClass.mro())
    print(mro_string)
    ```
- common class methods are resolved right to left for classes that use multiple
    inheritance:

    ```python
    class BaseClass:
        def __init__(self, value):
            self.value = value
            print(f"BaseClass.__init__ called")

    class LeftClass(BaseClass):
        def __init__(self, value):
            super().__init__(value)
            self.left = value
            print(f"LeftClass.__init__ called")

    class RightClass(BaseClass):
        def __init__(self, value):
            super().__init__(value)
            self.right = value
            print(f"RightClass.__init__ called")

    class Both(LeftClass, RightClass):
        def __init__(self, value):
            super().__init__(value)
            print(f"Both.__init__ called")

    mro_string = "\n".join(repr(cls) for cls in Both.mro())
    print(mro_string)
    # <class '__main__.Both'>
    # <class '__main__.LeftClass'>
    # <class '__main__.RightClass'>
    # <class '__main__.BaseClass'>
    # <class 'object'>

    Both(5)
    # BaseClass.__init__ called
    # RightClass.__init__ called
    # LeftClass.__init__ called
    # Both.__init__ called
    ```

    - the MRO output shows that the initialization functions are evaluated in the
        following order: `Both`, `LeftClass`, `RightClass`, `BaseClass`. They
        are then called in the reverse order

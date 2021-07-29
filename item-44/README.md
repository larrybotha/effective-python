# Item 44 - Plain attributes over getters and setters

```shell
$ python3 ./
```

- avoid using getters and setters for attributes in classes - start with public
    attributes by default
    - this makes incrementing / decrementing attributes simple
    - this also allows one to migrate to the `@property` decorator at a later
        stage without breaking the implementation:

        ```python
        class MyClass:
          def __init__(self, value):
            self.value = value

        instance == MyClass(5)
        print(instance.value) # 5
        instance.value = 10
        print(instance.value) # 10

        # some time, later, when we need to refactor MyClass
        class MyClass:
            def __init__(self, value)
                self._value

            @property
            def value(self):
                return self._value

            @value.setter
            def value(self, value):
                self._value = value

        # interface is preserved
        instance == MyClass(5)
        print(instance.value) # 5
        instance.value = 10
        print(instance.value) # 10
        ```
- the `@property` decorator allows one to define property getters and setters in
    2 parts:

    ```python
    class MyClass:
        @property
        def public_property_name(self):
            return self._some_value

        @public_property_name.setter
        def public_property_name(self, value):
            self._some_value = value
    ```
- `@property` can be used for side effects:

    ```python
    class MyClass:
        @property
        def public_property_name(self):
            return self._some_value

        @public_property_name.setter
        def public_property_name(self, value):
            print('a side effect!')
            self._some_value = value
    ```
- the `setter` property can be used for validation:

    ```python
    class IntValidator:
        def __init__(self, value):
            # use the setter to validate instantiation
            self.value = value

        @property
        def value(self):
            return self._value

        @value.setter(self,value):
            if not isinstance(value, int):
                raise TypeError('only int allowed')

            self._value = value

    int_validator = IntValidator(1) # valid
    int_validator.value = .5 # invalid

    IntValidator(.5) # also invalid
    ```

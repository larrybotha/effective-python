# Item 46 - Descriptors for reusable `@property` methods

```shell
$ python3 ./
```

- `@property` is good for defining getters and setters for a single property
    with validation
- `@property` is not so good for multiple properties that should behave in the
    same manner - i.e. reusing logic `@property` is not possible - the same
    logic must be defined repeatedly
- using a descriptor class to define shared behaviour of properties within a
    class can be superior
- to define a descriptor class, create a class that defines a `__set__` and
    `__get__` method:

    ```python
    def MyDescriptor:
      def __set__(self):
    ```

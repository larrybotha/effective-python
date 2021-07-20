# Item 41 - Composing functionality using mix-ins

```shell
$ python3 ./
```

- mix-ins are a mechanism that allows one to avoid multiple inheritance.
    Multiple inheritance should be avoided - **favour composition over
    inheritance**
- mix-ins are classes that provide a small set of methods, don't have instance
    properties, and don't require `__init__` to be called
- methods in mix-ins can be overridden by the classes inheriting them:

    ```python
    class MyMixin:
        def print_me(self):
            print(self._get_name())

        def _get_name(self):
            return self.__class__.__name__

    class MyClass(MyMixin):
        def __init__(self):
            pass

        def _get_name(self):
            return 'foo'

    cls = MyClass()

    cls.print_me()
    # foo
    ```
- `json.loads` deserializes a JSON string, similar to Javascript's `JSON.parse`
- `json.dumps` deserializes a JSON string, similar to Javascript's
    `JSON.stringify`
- mixins can include `@classmethod`s

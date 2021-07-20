# Item 42 - Prefer public attributes over private attributes

```shell
$ python3 ./
```

- Python has private and public attributes:

    ```python
    class MyClass:
        def __init__(self, private, public):
            self.__private = private
            self.public = public
    ```
- accessing private methods raises `AttributeError`
- classmethods can access private attributes
- subclasses cannot access private attributes of parents
- private attributes are renamed in Python - the values are still accessible as
    follows:

    ```python
    class MyClass:
        def __init__(self, private, public):
            self.__private = private
            self.public = public

    instance = MyClass('foo', 'bar')

    print(instance._MyClass__private)
    ```
- because of this, using private attributes can lead to users accessing
    attributes in unwieldy ways. To avoid this, avoid using private attributes
    as they're always accessible
    - if you decide to move a value from private to public, anyone using the
        `_ClassName__attribute_name` accessor will have a broken implementation
    - this is exacerbated when using multiple inheritance, or changing class
        heirarchy
- prefer protected attributes (attributes with a single underscore), and
    document the dangers of using them
- plan from the beginning to allow subclasses to do more with attributes from
    parent classes

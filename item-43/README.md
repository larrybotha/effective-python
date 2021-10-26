# Item 43 - Inheriting from `collections.abc` for custom container types

```shell
$ python3 ./
```

- by creating classes that are subclasses of existing containers, like lists,
    dicts, tuples, etc., one inherits all of the methods of that container

    ```python
    class MyList(list):
      def __init__(self, xs):
        super().__init__(xs)

      def loud_noises(self):
        for x in self:
          print(f'LOUD NOISES: {x}')

    my_list = MyList()

    my_list.append('AAAAAAAAHHHH')
    my_list.loud_noises()
    my_list.pop()
    ```
- to allow a class to retrieve items by index, like with lists, the class must
    implement `__getitem__`
- partially implementing a container, such as allowing values to be accessed via
    an index using `__getitem__` may lead to expectations that other sequencing
    operations, such as settings items via index are available. Manually
    implementing all of these methods is cumbersome

    ```python
    class IndexableThing:
      def __getitem__(self, index):
        return index

    thing = IndexableThing()

    print(thing[0])
    # 0

    print(len(thing))
    # TypeError
    ```
- to avoid having to remember what to implement, Python's `collections.abc`
    module provides abstract classes allowing one to correctly implement a
    container
    - many of the abstract classes implement functionality for free when the
        minimum requirements of the abstract class are met. e.g. implementing
        `__getitem__` and `__len__` for `Sequence` allows one to use `count` and
        `index` on instances
- creating a class that inherits from an abstract class without implementing the
    required methods will throw if an instance is initialised from that class:

    ```python
    from abc import ABC, abstractmethod

    class MyAbstractInterface(ABC):
        def some_method(self):
            pass

    class ConcreteClass(MyAbstractInterface):
        pass

    try:
        ConcreteClass()
    except TypeError:
        print('throws')

    # throws
    ```
- for simple use-cases, inherit from `list`, `dict`, `tuple` etc

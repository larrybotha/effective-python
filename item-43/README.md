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

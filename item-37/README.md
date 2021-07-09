# Item 37 - Favour composing classes instead of nested built-in types

```shell
$ python3 ./
```

- as soon as one is in the situation where one is tempted to nest dicts inside
    of dicts, use a class
- tuples are useful for simple values, but their positions are fixed. If data in
    a tuple gets more complex, we're left with a long positional value. If a
    tuple exceeds 2 values, consider either a `namedtuple`, or a class
    - another issue with tuples is that when destructuring a tuple, every unused
        value needs to be represented by an `_`. If adding a new item to a
        tuple, every location where that tuple is used will need to be updated
- `namedtuple` is similar to creating immutable classes with little boilerplate

    ```python
    from collections import namedtuple

    Point = namedtuple('Point', ['x', 'y'])
    p = Point(1,2)
    print(p)
    print(p.x)
    print(p.y)
    # Point(x=1, y=2)
    # 1
    # 2
    ```
- `namedtuple`s have a few drawbacks:
    - default argument values can't be specified for `namedtuple`s
    - internal methods of `namedtuple`s may be used by people consuming your
        library, making it difficult to move away if you need to

# Item 37 - Favour composing classes instead of nested built-in types

```shell
$ python3 ./
```

- as soon as one is in the situation where one is tempted to nest dicts inside
    of dicts, use a class
- tuples are useful for simple values, but their positions are fixed. If data in
    a tuple gets more complex, we're left with a long positional value. If a
    tuple exceeds 2 values, consider either a `namedtuple`, or a class

    - `namedtuple` should only be used if you know no-one is going to access the
        tuple directly. `namedtuple`s share properties and interfaces with other
        objects, so users can mistake them for other objects, potentially
        resulting in unexpected behaviour

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

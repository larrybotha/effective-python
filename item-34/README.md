# Item 34 - Avoid using generators' `send` method to inject data

```shell
$ python3 ./
```

- `iter` can be used to convert an iterable into an iterator:

    ```python
    xs = [1,2,3]
    xs_iter = iter(xs)

    print(f'has(attr(xs, "__next__")): {hasattr(xs, "__next__")}')
    print(f'has(attr(xs_iter, "__next__")): {hasattr(xs_iter, "__next__")}')

    # has(attr(xs, "__next__")): False
    # has(attr(xs_iter, "__next__")): True
    ```
- `yield` statements evaluate to `None`

    ```python
    def gen(length: int):
        for i in range(length):
            result = yield i
            print(f'result: {result}')

    it = gen(2)

    while True:
        try:
            output = next(it)
            print(f"yielded: {output}")
        except StopIteration:
            break

    # yielded: 0
    # result: None
    # yielded: 1
    # result: None
    ```
- using `some_iterator.send` values can be assigned to `yield`.
    - the first value sent to an iterator must be `None`, otherwise a `TypeError`
        will be thrown
    - `send` will both assign a value to `yield`, and advance the iterator

        ```python
        def my_gen(length: int):
            for i in range(length):
                sent_value = yield i
                print(f'sent: {sent_value}')

        it = my_gen(2)
        output = it.send(None)
        print(f'initial output: {output}')

        while True:
            try:
                output = it.send('foo')
                print(f'output: {output}')
            except StopIteration:
                break
        ```
    - the value passed at the time of calling `send` will persist for only that
        iteration - any subsequent `next` calls will have `yield` evaluate to
        the default `None`
- using `send` is not particularly intuitive:
    - it's not easy to read
    - the first yielded value of your iterator will be `None`, possibly making
        the types of the yielded values inconsistent
    - it requires that the first value be `None`, which makes the iterables used
        for the send values contain inconsistent types
- the complexity of `send` can be avoided by instead passing an iterator into the
    iterable:

    ```python
    def my_gen(xs: List[int], iterator: Iterator[int]):
        for x in xs:
            yield x * next(iterator)

    # [1,2,3]
    xs = [x for (x, _) in enumerate(range(3), 1)]
    # gen(10, 20, 30)
    scalar_iterator = (x * 10 for (x, _) in enumerate(range(3), 1))
    it = my_gen(xs, scalar_iterator)

    for x in it:
        print(x)

    # 10
    # 40
    # 90

    # or converting a list to an iterator
    scalars = [x * 10 for (x, _) in enumerate(range(3), 1)]
    it = my_gen(xs, iter(scalars))

    for x in it:
        print(x)

    # 10
    # 40
    # 90

    ```

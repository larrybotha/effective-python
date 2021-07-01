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
    will advance an iterator
    iteration. Once the value sent via `send` is consumed, yield will return
    `None` if no other values are sent:

    ```python
    def my_gen(length: int):
        for i in range(length):
            assigned_yield = yield i
            print(f'sent value: {assigned_yield}')

    it = my_gen(3)

    # before anything is yielded, only None may be sent
    it.send(None)

    print(f'next: {next(it)}')
    it.send('foo')

    print(f'next: {next(it)}')
    print(f'next: {next(it)}')
    ```

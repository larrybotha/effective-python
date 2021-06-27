# Item 33 - `yield from` and composing multiple generators

```shell
$ python3 ./
```

- iterating over multiple generators can be verbose:

    ```python
    def iter_1(times: int):
      for _ in range(times):
        yield "iter_1 yielded"

    def iter_2(times: int):
      for _ in range(times):
        yield "iter_2 yielded"

    # this here is verbose
    def iterate_multiple():
        for x in iter_1(2):
            yield x

        for x in iter_2(3):
            yield x

    result = list(iterate_multiple())
    print('\n'.join(result))

    # iter_1 yielded
    # iter_1 yielded
    # iter_2 yielded
    # iter_2 yielded
    # iter_2 yielded
    ```
- instead, we can use the `yield from` statement to handle the looping for us:

    ```python
    def iter_1(times: int):
      for _ in range(times):
        yield "iter_1 yielded"

    def iter_2(times: int):
      for _ in range(times):
        yield "iter_2 yielded"

    # this is much easier to read
    def iterate_multiple():
        yield from iter_1(2)
        yield from iter_2(3)

    # ...
    ```

    or even:

    ```python
    def iter_1(times: int):
      message = "iter_1 yielded"

      return [msg for _ in range(times)]

    def iter_2(times: int):
      message = "iter_2 yielded"

      return [msg for _ in range(times)]

    def iterate_multiple():
        yield from iter_1(2)
        yield from iter_2(3)
    ```
- not only is `yield from` easier to read, but it is more performant than
    iterating over iterators using for loops
- the `timeit.timeit` method can be used to time function execution, similar to
    Javascript's `performance.now()`
